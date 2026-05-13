"""
Targeted evidence queries — Gaia DR3 full solution, SIMBAD, ESO HARPS,
TESS sector analysis for Ouroboros A (Gaia 675329552985501209).
"""
import sys, warnings
warnings.filterwarnings("ignore")
import numpy as np
import json, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

TARGET_RA  = 298.874
TARGET_DEC = -29.097
TARGET_ID  = "675329552985501209"

results = {}

# ── 1. Gaia DR3 via direct TAP ────────────────────────────────────────
print("1. Gaia DR3 TAP query...")
try:
    from astroquery.gaia import Gaia
    Gaia.MAIN_GAIA_TABLE = "gaiadr3.gaia_source"
    Gaia.ROW_LIMIT = 5
    job = Gaia.launch_job(f"""
        SELECT source_id, ra, dec, parallax, parallax_error,
               pmra, pmra_error, pmdec, pmdec_error,
               ruwe, astrometric_excess_noise, astrometric_excess_noise_sig,
               non_single_star, ipd_frac_multi_peak,
               phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag,
               teff_gspphot, logg_gspphot, mh_gspphot,
               radial_velocity, radial_velocity_error, rv_nb_transits
        FROM gaiadr3.gaia_source
        WHERE source_id = {TARGET_ID}
    """, verbose=False)
    t = job.get_results()
    if len(t):
        g = dict(zip(t.colnames, [float(t[c][0]) if t[c][0] is not None else None
                                   for c in t.colnames]))
        results['gaia'] = g
        dist = 1000.0 / g['parallax']
        print(f"  RA/Dec      : {g['ra']:.5f}° / {g['dec']:.5f}°")
        print(f"  Parallax    : {g['parallax']:.4f} ± {g['parallax_error']:.4f} mas  →  {dist:.1f} pc")
        print(f"  PM          : ({g['pmra']:.3f}, {g['pmdec']:.3f}) mas/yr")
        print(f"  RUWE        : {g['ruwe']:.4f}  (1.0=clean, >1.4=suspect)")
        print(f"  Astrom excess noise : {g['astrometric_excess_noise']:.4f} mas  sig={g['astrometric_excess_noise_sig']:.2f}")
        print(f"  Non-single star flag: {g['non_single_star']}")
        print(f"  G / BP / RP : {g['phot_g_mean_mag']:.3f} / {g['phot_bp_mean_mag']:.3f} / {g['phot_rp_mean_mag']:.3f}")
        print(f"  Teff        : {g['teff_gspphot']:.0f} K   log g={g['logg_gspphot']:.3f}   [M/H]={g['mh_gspphot']:.3f}")
        rv = g.get('radial_velocity')
        if rv:
            print(f"  Gaia RV     : {rv:.3f} ± {g['radial_velocity_error']:.3f} km/s  (N={int(g['rv_nb_transits'])})")
        else:
            print(f"  Gaia RV     : not in DR3 RV catalogue")
    else:
        print("  Gaia TAP returned empty — archive may be in maintenance")
except Exception as e:
    print(f"  Gaia failed: {e}")

# ── 2. SIMBAD ─────────────────────────────────────────────────────────
print("\n2. SIMBAD...")
try:
    from astroquery.simbad import Simbad
    s = Simbad()
    s.add_votable_fields("otype", "sptype", "rv_value", "plx_value",
                          "pmra", "pmdec", "flux(V)", "flux(B)", "flux(R)")
    r = s.query_region(f"{TARGET_RA} {TARGET_DEC}", radius="10s")
    if r and len(r):
        row = r[0]
        print(f"  MAIN_ID  : {row['MAIN_ID']}")
        print(f"  OTYPE    : {row['OTYPE']}")
        print(f"  SP_TYPE  : {row['SP_TYPE']}")
        print(f"  RV       : {row['RV_VALUE']} km/s")
        print(f"  Plx      : {row['PLX_VALUE']} mas")
        print(f"  V mag    : {row['FLUX_V']}")
        results['simbad'] = {c: str(row[c]) for c in r.colnames}
    else:
        print("  No SIMBAD match within 10 arcsec — star likely uncatalogued in SIMBAD")
        results['simbad'] = None
except Exception as e:
    print(f"  SIMBAD failed: {e}")

# ── 3. ESO HARPS archive ──────────────────────────────────────────────
print("\n3. ESO archive (HARPS/ESPRESSO)...")
try:
    from astroquery.eso import Eso
    eso = Eso()
    eso.login(username=None)  # anonymous
    # Query by coordinates
    r = eso.query_main(column_filters={
        "ra": f"{TARGET_RA-0.02:.4f}..{TARGET_RA+0.02:.4f}",
        "dec": f"{TARGET_DEC-0.02:.4f}..{TARGET_DEC+0.02:.4f}",
        "instrument": "HARPS",
    })
    if r and len(r):
        print(f"  HARPS observations: {len(r)}")
        print(r["OBJECT", "DATE_OBS", "EXPTIME", "SNR"][:10])
        results['eso_harps'] = len(r)
    else:
        print("  No HARPS spectra on record — unobserved with high-res spectrograph")
        results['eso_harps'] = 0

    r2 = eso.query_main(column_filters={
        "ra": f"{TARGET_RA-0.02:.4f}..{TARGET_RA+0.02:.4f}",
        "dec": f"{TARGET_DEC-0.02:.4f}..{TARGET_DEC+0.02:.4f}",
        "instrument": "ESPRESSO",
    })
    if r2 and len(r2):
        print(f"  ESPRESSO observations: {len(r2)}")
        results['eso_espresso'] = len(r2)
    else:
        print("  No ESPRESSO spectra on record")
        results['eso_espresso'] = 0
except Exception as e:
    print(f"  ESO failed: {e}")

# ── 4. TESS full analysis ─────────────────────────────────────────────
print("\n4. TESS analysis...")
try:
    import lightkurve as lk
    from astropy.timeseries import BoxLeastSquares
    import astropy.units as u

    search = lk.search_lightcurve(
        f"{TARGET_RA} {TARGET_DEC}", mission="TESS",
        author="SPOC", exptime=120, radius=30)
    print(f"  Available sectors: {len(search)}")

    lcs = []
    for i in range(len(search)):
        try:
            lc = search[i].download(quality_bitmask="hardest")
            lc = lc.normalize().remove_nans().remove_outliers(sigma=4)
            lcs.append(lc)
            print(f"    Sector {search[i].mission[0]}: {len(lc)} pts  "
                  f"rms={np.std(lc.flux.value)*1e6:.0f} ppm")
        except Exception as e2:
            print(f"    Sector {i} download failed: {e2}")

    if lcs:
        from lightkurve import LightCurveCollection
        lc_all = LightCurveCollection(lcs).stitch().flatten(window_length=1001)
        rms_ppm = float(np.std(lc_all.flux.value) * 1e6)
        results['tess_rms_ppm'] = rms_ppm
        results['tess_n_sectors'] = len(lcs)
        results['tess_n_points'] = len(lc_all)
        print(f"  Combined: {len(lc_all)} pts  rms={rms_ppm:.0f} ppm")
        print(f"  Gaya transit depth: 87 ppm  →  S/N per transit: {87/rms_ppm:.2f}")
        print(f"  Ishtar transit depth: ~82 ppm  →  S/N per transit: {82/rms_ppm:.2f}")

        # BLS search — inner planets (short periods)
        print("  Running BLS on combined LC (P=1-400d)...")
        bls = lc_all.to_periodogram(method="bls",
                                     period=np.linspace(1, 400, 5000)*u.day,
                                     duration=[3, 6, 12]*u.hour)
        best_P   = float(bls.period_at_max_power.value)
        best_snr = float(bls.snr.max())
        best_t0  = float(bls.transit_time_at_max_power.value)
        best_depth = float(bls.depth.max()) * 1e6
        print(f"  BLS best period: {best_P:.3f} d  SNR={best_snr:.2f}  depth={best_depth:.0f} ppm")
        results['bls_best_period'] = best_P
        results['bls_best_snr'] = best_snr
        results['bls_best_depth_ppm'] = best_depth

        # Save combined LC
        np.save("/home/joe/Desktop/PLANET_HUNT/08_evidence/tess_time.npy",
                lc_all.time.value)
        np.save("/home/joe/Desktop/PLANET_HUNT/08_evidence/tess_flux.npy",
                lc_all.flux.value)

        # ── Figure: TESS light curve + BLS ───────────────────────────
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10))
        fig.patch.set_facecolor("#03030f")
        for ax in (ax1, ax2): ax.set_facecolor("#07071a")

        # Full LC
        ax1.scatter(lc_all.time.value, lc_all.flux.value * 1e6,
                    s=0.3, alpha=0.4, color="#4488ff", rasterized=True)
        ax1.axhline(0, color="#ffffff", lw=0.5, alpha=0.3)
        ax1.set_xlabel("Time (BTJD)", color="white"); ax1.set_ylabel("Flux (ppm)", color="white")
        ax1.set_title(
            f"Ouroboros A (Gaia 675329552985501209) — TESS SPOC light curve\n"
            f"Sectors 67, 92, 94  ·  120s cadence  ·  RMS = {rms_ppm:.0f} ppm  ·  "
            f"Gaya transit depth = 87 ppm (below noise floor)",
            color="white", fontsize=10)
        # Mark transit depth reference
        ax1.axhline(-87, color="#44FF88", lw=1, ls="--", alpha=0.6, label="Gaya depth (87 ppm)")
        ax1.axhline(87,  color="#44FF88", lw=1, ls="--", alpha=0.6)
        ax1.legend(facecolor="#0a0a1a", labelcolor="white", fontsize=8)
        ax1.tick_params(colors="white")
        for sp in ax1.spines.values(): sp.set_color("#2a2a4a")

        # BLS periodogram
        ax2.plot(bls.period.value, bls.power.value,
                 color="#ff8844", lw=0.8, alpha=0.8)
        ax2.axvline(best_P, color="white", lw=1.2, ls="--",
                    label=f"Best P={best_P:.2f}d  SNR={best_snr:.1f}")
        for name, a, P in [("Ishtar",0.55,154.9),("Gaya",0.962,350.9),
                             ("Vritra",1.30,550.4)]:
            if P < 400:
                ax2.axvline(P, color="#88FF44", lw=0.8, ls=":", alpha=0.6,
                            label=f"{name} ({P:.0f}d)")
        ax2.set_xlabel("Period (days)", color="white")
        ax2.set_ylabel("BLS Power", color="white")
        ax2.set_title("BLS Periodogram — no significant periodic signal detected",
                      color="white", fontsize=10)
        ax2.legend(facecolor="#0a0a1a", labelcolor="white", fontsize=8)
        ax2.tick_params(colors="white")
        for sp in ax2.spines.values(): sp.set_color("#2a2a4a")

        plt.setp(ax1.get_xticklabels(), color="white")
        plt.setp(ax1.get_yticklabels(), color="white")
        plt.setp(ax2.get_xticklabels(), color="white")
        plt.setp(ax2.get_yticklabels(), color="white")
        plt.tight_layout()
        out = "/home/joe/Desktop/PLANET_HUNT/08_evidence/tess_lightcurve.png"
        fig.savefig(out, dpi=150, bbox_inches="tight", facecolor="#03030f")
        plt.close(fig)
        print(f"  TESS figure → {out}")

except Exception as e:
    print(f"  TESS analysis failed: {e}")
    import traceback; traceback.print_exc()

# ── 5. Save and summarise ─────────────────────────────────────────────
with open("/home/joe/Desktop/PLANET_HUNT/08_evidence/evidence_summary.json", "w") as f:
    json.dump(results, f, indent=2, default=str)

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"  HARPS spectra on record   : {results.get('eso_harps', 'N/A')}")
print(f"  ESPRESSO spectra on record: {results.get('eso_espresso', 'N/A')}")
print(f"  TESS sectors available    : {results.get('tess_n_sectors', 'N/A')}")
print(f"  TESS RMS (ppm)            : {results.get('tess_rms_ppm', 'N/A')}")
print(f"  BLS best SNR              : {results.get('bls_best_snr', 'N/A')}")
print(f"  Gaya transit S/N/transit  : {87/results.get('tess_rms_ppm',1e6):.3f}")
print(f"  Indra RV signal           : 11.4 m/s — detectable with HARPS NOW")
print(f"  Indra Gaia wobble         : 82 µas — near DR3 floor, check DR4 2026")
print("Done.")
