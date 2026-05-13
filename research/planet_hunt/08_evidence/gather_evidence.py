"""
Gather all available archival evidence for Gaia 675329552985501209
(Ouroboros A) — Gaia DR3 full solution, TESS, SIMBAD, ESO, VizieR RV.
"""
import sys, warnings
warnings.filterwarnings("ignore")
import numpy as np
import json, os

TARGET_RA   = 298.874
TARGET_DEC  = -29.097
TARGET_ID   = "675329552985501209"
TARGET_DIST = 51.0   # pc

os.makedirs("/home/joe/Desktop/PLANET_HUNT/08_evidence", exist_ok=True)

evidence = {}

# ── 1. Gaia DR3 full astrometric solution ─────────────────────────────
print("=" * 60)
print("1. Gaia DR3 — full astrometric solution")
print("=" * 60)
try:
    from astroquery.gaia import Gaia
    Gaia.MAIN_GAIA_TABLE = "gaiadr3.gaia_source"
    q = f"""
    SELECT source_id, ra, dec, parallax, parallax_error,
           pmra, pmra_error, pmdec, pmdec_error,
           ruwe, astrometric_excess_noise, astrometric_excess_noise_sig,
           astrometric_chi2_al, astrometric_n_good_obs_al,
           non_single_star, ipd_frac_multi_peak,
           phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag,
           teff_gspphot, logg_gspphot, mh_gspphot,
           radial_velocity, radial_velocity_error,
           rv_nb_transits, rv_expected_sig_to_noise
    FROM gaiadr3.gaia_source
    WHERE source_id = {TARGET_ID}
    """
    job = Gaia.launch_job(q)
    r = job.get_results()
    if len(r) > 0:
        row = r[0]
        print(f"  source_id        : {row['source_id']}")
        print(f"  RA / Dec         : {row['ra']:.6f}° / {row['dec']:.6f}°")
        print(f"  Parallax         : {row['parallax']:.4f} ± {row['parallax_error']:.4f} mas")
        print(f"  Distance         : {1000/row['parallax']:.1f} pc")
        print(f"  PM RA            : {row['pmra']:.4f} ± {row['pmra_error']:.4f} mas/yr")
        print(f"  PM Dec           : {row['pmdec']:.4f} ± {row['pmdec_error']:.4f} mas/yr")
        print(f"  RUWE             : {row['ruwe']:.4f}")
        print(f"  Astrom excess noise: {row['astrometric_excess_noise']:.4f} mas  sig={row['astrometric_excess_noise_sig']:.2f}")
        print(f"  Non-single star  : {row['non_single_star']}")
        print(f"  IPD frac multi   : {row['ipd_frac_multi_peak']}")
        print(f"  N good obs AL    : {row['astrometric_n_good_obs_al']}")
        print(f"  G / BP / RP      : {row['phot_g_mean_mag']:.3f} / {row['phot_bp_mean_mag']:.3f} / {row['phot_rp_mean_mag']:.3f}")
        print(f"  Teff             : {row['teff_gspphot']:.0f} K")
        print(f"  log g            : {row['logg_gspphot']:.3f}")
        print(f"  [M/H]            : {row['mh_gspphot']:.3f}")
        rv = row['radial_velocity']
        rv_err = row['radial_velocity_error']
        rv_n   = row['rv_nb_transits']
        print(f"  Gaia RV          : {rv} ± {rv_err} km/s  (N_transits={rv_n})")
        evidence['gaia_dr3'] = {k: float(row[k]) if row[k] is not None else None
                                 for k in row.colnames}
    else:
        print("  No result returned.")
except Exception as e:
    print(f"  Gaia query failed: {e}")

# ── 2. SIMBAD cross-match ──────────────────────────────────────────────
print("\n" + "=" * 60)
print("2. SIMBAD")
print("=" * 60)
try:
    from astroquery.simbad import Simbad
    Simbad.add_votable_fields("otype", "sp", "rv_value", "z_value",
                               "plx", "pm", "flux(V)", "flux(B)")
    result = Simbad.query_region(
        f"{TARGET_RA} {TARGET_DEC}", radius="5s")
    if result is not None and len(result) > 0:
        for row in result:
            print(f"  MAIN_ID   : {row['MAIN_ID']}")
            print(f"  OTYPE     : {row['OTYPE']}")
            print(f"  SP_TYPE   : {row['SP_TYPE']}")
            print(f"  RV        : {row['RV_VALUE']} km/s")
            print(f"  V mag     : {row['FLUX_V']}")
            evidence['simbad'] = {c: str(row[c]) for c in result.colnames}
    else:
        print("  No SIMBAD match within 5 arcsec.")
        evidence['simbad'] = None
except Exception as e:
    print(f"  SIMBAD query failed: {e}")

# ── 3. VizieR — existing RV catalogues ───────────────────────────────
print("\n" + "=" * 60)
print("3. VizieR — RV catalogues")
print("=" * 60)
try:
    from astroquery.vizier import Vizier
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    coord = SkyCoord(ra=TARGET_RA, dec=TARGET_DEC, unit="deg")
    # RAVE, GALAH, APOGEE, GCS radial velocity catalogues
    cats = ["III/283", "J/MNRAS/478/4513", "III/273", "I/339"]
    Vizier.ROW_LIMIT = 10
    for cat in cats:
        try:
            r = Vizier.query_region(coord, radius=10*u.arcsec, catalog=cat)
            if r and len(r) > 0:
                print(f"  Catalogue {cat}: {len(r[0])} match(es)")
                print(f"    {r[0]}")
                evidence[f'vizier_{cat}'] = str(r[0])
            else:
                print(f"  Catalogue {cat}: no match")
        except Exception as e2:
            print(f"  Catalogue {cat}: {e2}")
except Exception as e:
    print(f"  VizieR query failed: {e}")

# ── 4. TESS observations ───────────────────────────────────────────────
print("\n" + "=" * 60)
print("4. TESS — available observations")
print("=" * 60)
try:
    import lightkurve as lk
    search = lk.search_lightcurve(
        f"{TARGET_RA} {TARGET_DEC}",
        mission="TESS", author="SPOC", radius=30)
    if len(search) > 0:
        print(f"  TESS SPOC products: {len(search)}")
        print(search.table["mission", "exptime", "year"][:20])
        evidence['tess_search'] = len(search)

        # Download and analyse best sector
        print("  Downloading shortest-cadence sector...")
        lc_col = search.download_all(quality_bitmask="hardest")
        lc = lc_col.stitch().remove_outliers(sigma=4)
        lc = lc.flatten(window_length=401)

        # Basic statistics
        rms = float(np.std(lc.flux.value) * 1e6)
        print(f"  Light curve RMS: {rms:.0f} ppm")
        print(f"  Transit depth needed (Gaya): 87 ppm")
        print(f"  Detection S/N per transit: {87/rms:.2f}")
        evidence['tess_rms_ppm'] = rms

        # Save LC
        np.save("/home/joe/Desktop/PLANET_HUNT/08_evidence/tess_lc_time.npy",
                lc.time.value)
        np.save("/home/joe/Desktop/PLANET_HUNT/08_evidence/tess_lc_flux.npy",
                lc.flux.value)
        print(f"  LC saved ({len(lc)} points)")
    else:
        print("  No TESS SPOC data for this target.")
        # Try FFI
        search_ffi = lk.search_lightcurve(
            f"{TARGET_RA} {TARGET_DEC}",
            mission="TESS", author="TESS-SPOC", radius=30)
        print(f"  FFI search: {len(search_ffi)} products")
        evidence['tess_search'] = 0
except Exception as e:
    print(f"  TESS query failed: {e}")

# ── 5. ESO archive check ───────────────────────────────────────────────
print("\n" + "=" * 60)
print("5. ESO archive — existing spectra")
print("=" * 60)
try:
    from astroquery.eso import Eso
    eso = Eso()
    result = eso.query_surveys("HARPS", target=f"{TARGET_RA} {TARGET_DEC}",
                                cache=False)
    if result is not None and len(result) > 0:
        print(f"  ESO/HARPS spectra found: {len(result)}")
        print(result[:5])
        evidence['eso_harps'] = len(result)
    else:
        print("  No existing HARPS spectra on record.")
        evidence['eso_harps'] = 0
except Exception as e:
    print(f"  ESO query failed: {e}")

# ── 6. Predicted instrument signals ───────────────────────────────────
print("\n" + "=" * 60)
print("6. Predicted signals — current instruments")
print("=" * 60)

# RV signals
planets = [
    ("Nabu",   0.28,  56.2,   0.45, 0.014),
    ("Ishtar", 0.55,  154.9,  0.92, 0.075),
    ("Gaya",   0.962, 350.9,  1.00, 0.093),
    ("Vritra", 1.30,  550.4,  1.40, 0.160),
    ("Ares",   1.75,  863.3,  1.10, 0.084),
    ("Indra",  4.80,  3983.0, 10.5*3.15, 11.4),
    ("Kronos", 9.80,  11620., 9.0*2.55,  6.1),
    ("Skadi",  19.5,  32610., 3.8*0.058, 0.8),
]

print(f"\n  {'Planet':<10} {'a(AU)':>6} {'P(d)':>8} {'K(m/s)':>8} {'ESPRESSO?':>12} {'HARPS?':>8}")
print("  " + "-"*60)
ESPRESSO_FLOOR = 0.10   # m/s
HARPS_FLOOR    = 0.30

for name, a, P, re, K in planets:
    esp = "YES" if K > ESPRESSO_FLOOR else f"marg({K/ESPRESSO_FLOOR:.1f}σ/obs)"
    hps = "YES" if K > HARPS_FLOOR   else "no"
    print(f"  {name:<10} {a:>6.2f} {P:>8.1f} {K:>8.3f} {esp:>12} {hps:>8}")

# Transit probabilities
print(f"\n  Transit probabilities (geometric, edge-on):")
Rstar = 0.93   # Rsun in AU = 0.93 * 0.00465
Rstar_AU = 0.93 * 0.00465
for name, a, P, re, K in planets[:6]:
    Re_AU = re * 4.26e-5  # Earth radii to AU (rough)
    p_transit = (Rstar_AU + Re_AU) / a
    depth_ppm = (re * 0.009168 / (0.93))**2 * 1e6  # rough ppm
    print(f"  {name:<10}  p_transit={p_transit:.3f}  depth~{depth_ppm:.0f}ppm")

# Gaia astrometry for Indra
print(f"\n  Gaia astrometric signal (Indra, gas giant):")
Mp_Mj    = 0.85
Mp_Msun  = Mp_Mj * 9.548e-4
Ms_Msun  = 0.93
a_Indra  = 4.80   # AU
dist_pc  = 51.0
wobble_AU  = (Mp_Msun / Ms_Msun) * a_Indra
wobble_mas = wobble_AU / dist_pc * 1000
print(f"    Stellar wobble: {wobble_AU:.5f} AU = {wobble_mas*1000:.1f} µas")
print(f"    Gaia DR3 floor: ~20-30 µas for G=8.3")
print(f"    Gaia DR4 (2026) floor: ~10 µas — marginal detection possible")

evidence['predicted_rv_ms'] = {name: K for name, a, P, re, K in planets}
evidence['indra_wobble_uas'] = wobble_mas * 1000

# ── Save evidence summary ──────────────────────────────────────────────
with open("/home/joe/Desktop/PLANET_HUNT/08_evidence/evidence_summary.json", "w") as f:
    json.dump(evidence, f, indent=2, default=str)
print("\n\nEvidence summary saved.")
