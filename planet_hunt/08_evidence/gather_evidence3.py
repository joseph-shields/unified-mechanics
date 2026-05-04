"""
Three additional tests for Ouroboros A (Gaia 675329552985501209):
  1. Hipparcos-Gaia PMa (Brandt 2021, VizieR J/ApJS/254/42)
  2. TESS Lomb-Scargle rotation period → gyrochronological age
  3. 2MASS / WISE photometry — IR excess / binary contamination
"""
import warnings; warnings.filterwarnings("ignore")
import numpy as np
import json
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import astropy.units as u

TARGET_RA  = 298.874
TARGET_DEC = -29.097
TARGET_ID  = "675329552985501209"
OUT_DIR    = "/home/joe/Desktop/PLANET_HUNT/08_evidence"

results = {}

# ── 1. Hipparcos–Gaia proper motion anomaly (PMa) ─────────────────────
print("=" * 60)
print("1. Hipparcos-Gaia PMa  (Brandt 2021  J/ApJS/254/42)")
print("=" * 60)
try:
    from astroquery.vizier import Vizier
    coord = SkyCoord(ra=TARGET_RA, dec=TARGET_DEC, unit="deg")
    v = Vizier(columns=["*"], row_limit=5)

    # Brandt 2021 — Hip-Gaia catalog
    r = v.query_region(coord, radius=30*u.arcsec, catalog="J/ApJS/254/42")
    if r and len(r) > 0:
        t = r[0]
        print(f"  Columns: {t.colnames[:20]}")
        for row in t:
            print(f"  HIP={row.get('HIP','?')}  pmRA_Hip={row.get('pmRA','?')}  "
                  f"pmRA_G={row.get('pmRA_G','?')}  "
                  f"dpmRA={row.get('dpmRA','?')}  sig_dpmRA={row.get('e_dpmRA','?')}")
        results['pma_brandt2021'] = {c: str(t[c][0]) for c in t.colnames}
    else:
        print("  No match in Brandt 2021 (star not in Hipparcos — expected for G=8.3 south)")
        results['pma_brandt2021'] = None

    # Try HGCA (Hipparcos-Gaia Catalog of Accelerations) alternate ID
    r2 = v.query_region(coord, radius=30*u.arcsec, catalog="J/ApJS/254/42/table1")
    if r2 and len(r2) > 0:
        print(f"  table1 match: {len(r2[0])} rows")
        results['pma_table1'] = str(r2[0])
    else:
        print("  table1: no match")

except Exception as e:
    print(f"  PMa query failed: {e}")
    results['pma_brandt2021'] = f"error: {e}"

# ── 2. TESS Lomb-Scargle rotation period ──────────────────────────────
print("\n" + "=" * 60)
print("2. TESS Lomb-Scargle — stellar rotation period")
print("=" * 60)
try:
    import lightkurve as lk

    search = lk.search_lightcurve(
        f"{TARGET_RA} {TARGET_DEC}", mission="TESS",
        author="SPOC", exptime=120, radius=30)
    print(f"  Sectors available: {len(search)}")

    lcs = []
    for i in range(len(search)):
        try:
            lc = search[i].download(quality_bitmask="hardest")
            lc = lc.normalize().remove_nans().remove_outliers(sigma=4)
            lcs.append(lc)
        except Exception as e2:
            print(f"  Sector {i} failed: {e2}")

    if lcs:
        from lightkurve import LightCurveCollection
        lc_all = LightCurveCollection(lcs).stitch()
        # Do NOT flatten — we want the stellar modulation signal
        lc_rot = lc_all.remove_outliers(sigma=3)
        t = lc_rot.time.value
        f = lc_rot.flux.value

        # Lomb-Scargle over 5–40 day rotation period window
        from astropy.timeseries import LombScargle
        freq, power = LombScargle(t, f).autopower(
            minimum_frequency=1/40.0,
            maximum_frequency=1/5.0)
        periods_ls = 1.0 / freq

        best_idx = np.argmax(power)
        P_rot = periods_ls[best_idx]
        FAP = LombScargle(t, f).false_alarm_probability(power[best_idx])

        print(f"  LS rotation period: {P_rot:.2f} d")
        print(f"  LS power: {power[best_idx]:.4f}  FAP={FAP:.4f}")

        # Gyrochronological age (Mamajek & Hillenbrand 2008)
        # P_rot = a * (B-V - 0.495)^b * t^c   with a=0.407, b=0.325, c=0.566
        # For Teff=5664K → B-V ≈ 0.70 (solar-type)
        BV = 0.70
        a_gyro, b_gyro, c_gyro = 0.407, 0.325, 0.566
        try:
            age_gyr = ((P_rot / (a_gyro * (BV - 0.495)**b_gyro))**(1/c_gyro)) / 1000.0
            print(f"  Gyrochronological age (B-V=0.70): {age_gyr:.2f} Gyr")
        except Exception:
            age_gyr = None
            print("  Gyrochronological age: could not compute (check P_rot/B-V)")

        results['tess_prot_days'] = float(P_rot)
        results['tess_ls_power'] = float(power[best_idx])
        results['tess_ls_fap'] = float(FAP)
        results['gyro_age_gyr'] = float(age_gyr) if age_gyr else None

        # Figure: LS periodogram
        fig, axes = plt.subplots(2, 1, figsize=(14, 9))
        fig.patch.set_facecolor("#03030f")
        for ax in axes: ax.set_facecolor("#07071a")

        axes[0].plot(t, (f-1)*1e6, lw=0.4, color="#4488ff", alpha=0.7)
        axes[0].set_ylabel("Flux (ppm)", color="white")
        axes[0].set_xlabel("Time (BTJD)", color="white")
        axes[0].set_title(
            "Ouroboros A — TESS raw flux (not flattened) — stellar rotation signal",
            color="white", fontsize=10)
        axes[0].tick_params(colors="white")
        for sp in axes[0].spines.values(): sp.set_color("#2a2a4a")
        plt.setp(axes[0].get_xticklabels(), color="white")
        plt.setp(axes[0].get_yticklabels(), color="white")

        axes[1].plot(periods_ls, power, color="#ff8844", lw=0.7)
        axes[1].axvline(P_rot, color="white", lw=1.5, ls="--",
                        label=f"P_rot = {P_rot:.2f} d  (FAP={FAP:.3f})")
        axes[1].axvline(27.0, color="#88FF44", lw=0.8, ls=":", alpha=0.6,
                        label="Solar P_rot = 27d")
        axes[1].set_xlabel("Period (days)", color="white")
        axes[1].set_ylabel("LS Power", color="white")
        age_str = f"{age_gyr:.2f} Gyr" if age_gyr else "N/A"
        axes[1].set_title(
            f"Lomb-Scargle rotation periodogram · P_rot = {P_rot:.2f} d · "
            f"Gyrochronological age ≈ {age_str}",
            color="white", fontsize=10)
        axes[1].legend(facecolor="#0a0a1a", labelcolor="white", fontsize=9)
        axes[1].tick_params(colors="white")
        for sp in axes[1].spines.values(): sp.set_color("#2a2a4a")
        plt.setp(axes[1].get_xticklabels(), color="white")
        plt.setp(axes[1].get_yticklabels(), color="white")

        plt.tight_layout(pad=2.0)
        fig.savefig(f"{OUT_DIR}/tess_rotation.png", dpi=150,
                    bbox_inches="tight", facecolor="#03030f")
        plt.close(fig)
        print(f"  Figure → {OUT_DIR}/tess_rotation.png")
    else:
        print("  No sectors downloaded — cannot run LS")

except Exception as e:
    print(f"  LS rotation failed: {e}")
    import traceback; traceback.print_exc()

# ── 3. 2MASS + WISE photometry ─────────────────────────────────────────
print("\n" + "=" * 60)
print("3. 2MASS / WISE photometry — IR excess & binary check")
print("=" * 60)
try:
    from astroquery.vizier import Vizier
    coord = SkyCoord(ra=TARGET_RA, dec=TARGET_DEC, unit="deg")
    v = Vizier(columns=["*"], row_limit=5)

    # 2MASS (II/246)
    r2mass = v.query_region(coord, radius=10*u.arcsec, catalog="II/246")
    if r2mass and len(r2mass) > 0:
        t2 = r2mass[0]
        print(f"  2MASS columns: {t2.colnames}")
        row = t2[0]
        J = row.get('Jmag', None); H = row.get('Hmag', None); K = row.get('Kmag', None)
        print(f"  2MASS J={J}  H={H}  Ks={K}")
        results['2mass'] = {'J': str(J), 'H': str(H), 'Ks': str(K)}

        # Check for IR excess: compare (J-H) and (H-K) to main-sequence expectations
        # For Teff=5664K: J-H ≈ 0.35, H-Ks ≈ 0.06 (Pecaut & Mamajek 2013)
        if J is not None and H is not None and K is not None:
            try:
                JH = float(J) - float(H)
                HK = float(H) - float(K)
                JH_ms = 0.35; HK_ms = 0.06
                dJH = JH - JH_ms; dHK = HK - HK_ms
                print(f"  J-H = {JH:.3f}  (MS expectation {JH_ms:.2f}  Δ={dJH:+.3f})")
                print(f"  H-Ks = {HK:.3f}  (MS expectation {HK_ms:.2f}  Δ={dHK:+.3f})")
                if abs(dJH) < 0.05 and abs(dHK) < 0.05:
                    print("  2MASS: colours consistent with bare main-sequence G dwarf — no near-IR excess")
                else:
                    print(f"  2MASS: colour anomaly — investigate (ΔJH={dJH:+.3f}, ΔHK={dHK:+.3f})")
                results['2mass']['JH'] = JH; results['2mass']['HK'] = HK
                results['2mass']['excess_flag'] = abs(dJH) > 0.05 or abs(dHK) > 0.05
            except Exception as e2:
                print(f"  Colour calc error: {e2}")
    else:
        print("  No 2MASS match within 10 arcsec")
        results['2mass'] = None

    # WISE (II/328/allwise)
    rwise = v.query_region(coord, radius=10*u.arcsec, catalog="II/328/allwise")
    if rwise and len(rwise) > 0:
        tw = rwise[0]
        row = tw[0]
        W1 = row.get('W1mag', None); W2 = row.get('W2mag', None)
        W3 = row.get('W3mag', None); W4 = row.get('W4mag', None)
        print(f"  WISE W1={W1}  W2={W2}  W3={W3}  W4={W4}")
        results['wise'] = {'W1': str(W1), 'W2': str(W2), 'W3': str(W3), 'W4': str(W4)}

        # W3/W4 excess check — debris disc indicator (W3-W4 > 0.5 for debris discs)
        if W3 is not None and W4 is not None:
            try:
                W3W4 = float(W3) - float(W4)
                print(f"  W3-W4 = {W3W4:.3f}  (>0.5 suggests debris disc)")
                results['wise']['W3W4'] = W3W4
                results['wise']['disc_flag'] = W3W4 > 0.5
                if W3W4 > 0.5:
                    print("  WISE: W3-W4 excess — possible debris disc (warrants follow-up)")
                else:
                    print("  WISE: no mid-IR excess — no debris disc, no binary contamination")
            except Exception as e3:
                print(f"  W3-W4 calc error: {e3}")
    else:
        print("  No AllWISE match within 10 arcsec")
        results['wise'] = None

except Exception as e:
    print(f"  2MASS/WISE query failed: {e}")
    results['2mass'] = f"error: {e}"
    results['wise'] = f"error: {e}"

# ── Save results ───────────────────────────────────────────────────────
with open(f"{OUT_DIR}/evidence_extra.json", "w") as fh:
    json.dump(results, fh, indent=2, default=str)

print("\n" + "=" * 60)
print("SUMMARY — extra tests")
print("=" * 60)
pma = results.get('pma_brandt2021')
print(f"  PMa (Brandt 2021)  : {'Match found' if pma and pma != None and 'error' not in str(pma) else 'No Hipparcos match (expected)'}")
print(f"  P_rot (TESS LS)    : {results.get('tess_prot_days', 'N/A'):.2f} d" if results.get('tess_prot_days') else "  P_rot (TESS LS)    : N/A")
age = results.get('gyro_age_gyr')
print(f"  Gyro age           : {age:.2f} Gyr" if age else "  Gyro age           : N/A")
print(f"  2MASS excess       : {results.get('2mass', {}).get('excess_flag', 'N/A') if results.get('2mass') else 'N/A'}")
print(f"  WISE disc flag     : {results.get('wise', {}).get('disc_flag', 'N/A') if results.get('wise') else 'N/A'}")
print("Done.")
