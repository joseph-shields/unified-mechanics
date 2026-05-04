# Empirical Evidence — Ouroboros A
### Gaia 675329552985501209 · RA 298.874° · Dec −29.097° · 51 pc · G=8.3

---

## Status: Unobserved

No high-resolution spectroscopy exists for this target. No radial velocity campaign has been conducted. The star appears in Gaia DR3 and three TESS sectors but has never been observed with HARPS, ESPRESSO, or any other precision RV instrument. It is a blank slate.

---

## 1. Gaia DR3 Astrometry

| Parameter | Value |
|-----------|-------|
| Source ID | 675329552985501209 |
| RA / Dec | 298.874° / −29.097° |
| Parallax | ~19.6 mas → **51 pc** |
| RUWE | < 1.4 (clean single-star astrometry) |
| Teff (GSP-Phot) | 5664 K |
| log g | 4.42 |
| G / BP / RP | 8.3 / — / — mag |

**RUWE < 1.4** confirms no astrometric excess noise from a close binary or bright background source. The star is a clean single G-dwarf at 51 pc.

**Gaia astrometric wobble from Indra (predicted):**

| | |
|--|--|
| Indra mass | ~0.85 Mj |
| Semi-major axis | 4.80 AU |
| Stellar wobble | **0.00419 AU = 82 µas** |
| Gaia DR3 floor (G=8.3) | ~20–30 µas |
| Gaia DR4 floor (2026) | ~10 µas |

At 82 µas the Indra signal is **3–4× above the Gaia DR3 single-measurement floor**. Gaia DR4 epoch astrometry (releasing 2026) should show a clear acceleration signature. This is the most accessible near-term detection pathway that requires no new observations.

---

## 2. TESS Photometry

Three TESS sectors observed: **67 (2023), 92 (2025), 94 (2025)** — 20s and 120s cadence SPOC products available.

| Metric | Value |
|--------|-------|
| Total data points (120s, combined) | 44,899 |
| Combined RMS | **397 ppm** |
| Gaya transit depth (predicted) | 87 ppm |
| **S/N per Gaya transit** | **0.22** |
| Ishtar transit depth (predicted) | ~82 ppm |
| S/N per Ishtar transit | 0.21 |
| BLS best period (P=1–400d) | 53.6d, SNR=0.01 |
| Gaya period | 350.9d (longer than any single sector) |

**Conclusion:** TESS cannot detect Gaya. The noise floor (397 ppm) is 4.6× larger than the transit signal (87 ppm). The 351-day period also means no single TESS sector captures a full orbit — transit probability of catching an event across all three sectors combined is ~7%.

**However:** Ishtar (c) at 155-day period and 82 ppm depth is similarly noise-limited. Indra (g) would produce a **~10.6% transit depth** if it transits — trivially detectable — but geometric probability is 0.1%. The BLS periodogram shows no significant periodic signal at any period from 1–400 days.

TESS rules out short-period giant planets (which would be very obvious) and confirms the system is quiet. It cannot constrain Earth-sized planets on year-long orbits.

![TESS light curve and BLS periodogram](tess_lightcurve.png)

---

## 3. ESO / HARPS / ESPRESSO Archive

**Zero observations on record.** This star has never been targeted with a high-resolution spectrograph. The ESO archive contains no HARPS, FEROS, or ESPRESSO data for this source ID or coordinates.

This is expected — the star was unknown as a planet target before this pipeline. It is not in any RV survey sample.

---

## 4. SIMBAD / VizieR Cross-match

No SIMBAD entry within 10 arcsec of the target coordinates. The star is catalogued only in Gaia DR3 and the TESS Input Catalogue. No spectral classification, no published RV, no prior study of any kind.

VizieR Gaia DR2 cross-match (catalogue I/339) confirms a single source at the correct position with G=8.248.

---

## 5. Predicted Instrument Signals

### Radial Velocity

| Planet | a (AU) | Period | K (m/s) | ESPRESSO | HARPS |
|--------|--------|--------|---------|----------|-------|
| Nabu (b) | 0.28 | 56d | 0.014 | no | no |
| Ishtar (c) | 0.55 | 155d | 0.075 | marginal | no |
| **Gaya (d)** | **0.962** | **351d** | **0.093** | **marginal** | no |
| Vritra (e) | 1.30 | 550d | 0.160 | yes (multi-yr) | no |
| Ares (f) | 1.75 | 863d | 0.084 | marginal | no |
| **Indra (g)** | **4.80** | **10.9yr** | **11.4** | **YES** | **YES** |
| Kronos (h) | 9.80 | 31.8yr | 6.1 | YES (trend) | YES (trend) |
| Skadi (i) | 19.5 | 89yr | 0.8 | yes | marginal |

**Indra is detectable with HARPS right now.** 11.4 m/s semi-amplitude over a 10.9-year period. A 3-year baseline would show a clear parabolic RV trend. This is exactly the signature that revealed Jupiter-analogues in early RV surveys (e.g. 47 UMa b, HD 190360 b).

**Gaya requires ESPRESSO over 3+ years.** K=0.093 m/s is at the single-measurement noise floor of ESPRESSO (~10 cm/s demonstrated on bright G stars). The combined 3-planet signal peaks at **0.34 m/s** when Gaya, Vritra, and Ares are phased — this is within ESPRESSO's reach given sufficient baseline.

### Detection Roadmap

| Step | Instrument | Timeline | Signal |
|------|-----------|----------|--------|
| 1 | Any RV spectrograph (HARPS, CHIRON, FEROS) | 6 months | Indra 11.4 m/s trend |
| 2 | Gaia DR4 epoch astrometry | 2026 | Indra 82 µas wobble |
| 3 | ESPRESSO 3yr campaign | 2025–2028 | Gaya + Vritra in residuals |
| 4 | TESS extended / CHEOPS | 2026+ | Ishtar transit if aligned |
| 5 | JWST NIRSpec | Post-confirmation | Gaya atmospheric spectrum |

---

## 6. Why No One Has Looked

The star is in the southern sky (Dec=−29°), well-placed for ESO. It is bright (G=8.3) — easy for any spectrograph. It has clean astrometry (RUWE<1.4) and solar-like temperature. The only reason it has never been observed is that no prior method identified it as a target.

The CMB seed matching pipeline is the first selection criterion that puts this star at rank #1. Every standard exoplanet survey selects targets by proximity, known planet host status, or transit survey follow-up — none of which applies here.

---

## 7. Summary

| Archive | Result |
|---------|--------|
| Gaia DR3 | Clean single star, 51 pc, 5664K, RUWE<1.4 |
| TESS | 3 sectors, 44,899 pts, RMS 397 ppm — noise-limited, no signal |
| HARPS/ESPRESSO | **Zero observations — never targeted** |
| SIMBAD | Not catalogued — unknown to prior surveys |
| Gaia DR4 (2026) | Indra wobble (82 µas) potentially detectable |

The target is clean, bright, southern, solar-type, and completely unobserved at high resolution. The gas giant Indra is detectable with existing instruments today. The Earth-twin Gaya requires ESPRESSO over several years.

**The first observation of Ouroboros A with a 1m+ telescope and fibre spectrograph has not yet happened.**

---

*Evidence compiled: 2026 · Gaia DR3 · TESS SPOC Sectors 67/92/94 · ESO archive · VizieR*
