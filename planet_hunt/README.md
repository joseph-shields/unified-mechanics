# CMB-Guided Planet Hunt
### Finding Earth-analogue planets using the cosmic microwave background as a targeting prior

---

## The Idea

The CMB temperature at any sky position is the fossil record of the primordial density perturbation that seeded structure formation there. Regions with identical CMB temperature formed under identical initial cosmological conditions. If Earth formed in a region seeded by a CMB patch at some temperature T, then other sky positions with the same temperature T are candidate sites for Earth-like planetary systems.

This pipeline implements that idea end-to-end: from a cosmological power spectrum derived without free parameters, through a full-sky CMB simulation, to a ranked catalogue of 1,287 unstudied G-type stars in Earth-CMB-matched sky regions.

The top candidate — **Gaia 675329552985501209**, designated the Ouroboros system — is a G5V star at 51 pc with G=8.3, observable with ESPRESSO at La Silla without adaptive optics.

---

## CMB Earth Findings

Earth appears at **rank #0** in its own seed category by construction.

| Parameter | Value |
|-----------|-------|
| Earth CMB direction | RA=242.56°, Dec=−59.68° (Laniakea / Great Attractor) |
| CMB temperature (UM simulation, seed 271828) | **+23.2 µK** (5° disc average) |
| CMB temperature (Planck SMICA real data) | **−141.69 µK** (5° disc average, equatorial) |
| Matched sky fraction (UM simulation) | 1.2% — 575 patches within ΔT < 8 µK |

**Note on the two temperatures:** The UM simulation (healpy synfast, seed 271828) and the real Planck SMICA map are two different realizations drawn from the same underlying power spectrum. They agree statistically — same C_ℓ shape, same variance — but any individual pixel value differs between realizations. The absolute temperature at Earth's CMB direction is realization-dependent; the statistical selection method is not. The pipeline selects regions in the same percentile of the same distribution, regardless of which realization is used.

The Planck SMICA map shows Earth's Laniakea direction sits in a **CMB cold spot** at −141.69 µK. This is a genuine large-scale CMB feature, consistent with the known underdensity in the direction of the Eridanus supervoid and surrounding LSS.

---

## Cosmological Framework

All parameters derived from Unified Mechanics (c²=c+1). No free parameters fitted.

| Parameter | UM Derivation | Planck 2018 |
|-----------|--------------|-------------|
| H0 | 67.40 km/s/Mpc | 67.36 |
| Ωb h² | 0.02237 | 0.02237 |
| Ωc h² | 0.1201 | 0.1200 |
| ns | 0.9635 | 0.9649 |
| As | 2.136×10⁻⁹ | 2.101×10⁻⁹ |
| τ | 0.0590 | 0.0544 |

Chain best-fit (planck_um_chain.txt, 1M points, min −loglike=781.8):
H0=68.16, ombh2=0.02218, omch2=0.12261, ns=0.96353, As=2.116×10⁻⁹

---

## Pipeline

```
01_cmb_pipeline/
  UM/LiMB → CAMB C_ℓ (lmax=3000)
  healpy synfast NSIDE=512, seed=271828
  5° disc average all pixels
  |T − T_Earth| < 8 µK → 575 matched patches, 50 best saved

02_gaia_targets/
  Gaia DR3 TAP query per patch:
    teff_gspphot 5100–6300K
    parallax > 2 mas (within 500 pc)
    parallax_over_error > 8
    RUWE < 1.4
    phot_g_mean_mag < 14
  NASA Exoplanet Archive cross-match (known hosts excluded)
  Habitability score: CMB 40% + Teff 30% + HZ temp 20% + size 10%
  → 1,287 unstudied G-stars, top 100 ranked

03_target_cards/
  Per-target system simulation:
    Stellar parameters → HZ boundaries
    3-planet HZ architecture
    RV signal, transit depth, duration

04_skypy_lss/
  Matter power spectrum CAMB lmax=8000
  Limber C_ℓ (projected matter, Smail n(z))
  healpy synfast NSIDE=2048 matter overdensity map
  Galaxy distribution in top-12 seed patches

05_catalogue/
  MASTER_CATALOGUE.md — full documentation
  exoplanets.json — NASA archive cross-match

06_planck/
  Planck SMICA R3.00 real-sky comparison
  planck_real_targeting.py — real alm targeting
  planck_real_vs_um_targets.png — overlay comparison

07_planet_concept/
  Ouroboros system — full architecture and renders
  All 9 bodies: star + 8 planets
```

---

## Top 10 Targets

| # | Gaia ID | RA | Dec | Teff | Dist | G | CMB ΔT |
|---|---------|----|----|------|------|---|--------|
| 1 | 675329552985501209 | 298.874 | −29.097 | 5664K | 51pc | 8.3 | 0.10µK |
| 2 | 675172432344067212 | 297.243 | −29.729 | 5799K | 100pc | 9.7 | 0.10µK |
| 3 | 290067141679412787 | 83.271 | −34.495 | 5751K | 75pc | 9.1 | 0.07µK |
| 4 | 494856356929219110 | 40.841 | −41.852 | 5730K | 109pc | 10.0 | 0.10µK |
| 5 | 420654804990989696 | 1.969 | 55.577 | 5867K | 49pc | 7.7 | 0.05µK |
| 6 | 393289891154301580 | 186.922 | 14.259 | 5656K | 82pc | 9.5 | 0.13µK |
| 7 | 675191801358525747 | 297.098 | −29.528 | 5667K | 74pc | 9.4 | 0.10µK |
| 8 | 447716348950177318 | 276.762 | 6.273 | 5724K | 99pc | 9.8 | 0.07µK |
| 9 | 482312368929392396 | 81.242 | −34.205 | 5495K | 38pc | 7.9 | 0.07µK |
| 10 | 290172643256082982 | 82.275 | −33.429 | 5645K | 107pc | 10.2 | 0.07µK |

---

## The Ouroboros System — Rank #1

**Gaia 675329552985501209** · RA=298.874° · Dec=−29.097° · 51 pc · G=8.3 · Teff=5664K

| Name | AU | Period | Size | Teq |
|------|----|--------|------|-----|
| Nabu (b) | 0.28 | 56d | 0.45 Re | 497K |
| Ishtar (c) | 0.55 | 155d | 0.92 Re | 354K |
| **Gaya (d)** | **0.962** | **351d** | **1.00 Re** | **254K** |
| Vritra (e) | 1.30 | 550d | 1.40 Re | 219K |
| Ares (f) | 1.75 | 863d | 1.10 Re | 188K |
| Indra (g) | 4.80 | 10.9yr | 10.5 Re | 120K |
| Kronos (h) | 9.80 | 31.8yr | 9.0 Re | 84K |
| Skadi (i) | 19.5 | 89yr | 3.8 Re | 60K |

Gaya predicted RV signal K=0.093 m/s, transit depth 87 ppm, 12.8hr duration.
Combined 3-planet RV peak 0.34 m/s — within ESPRESSO capability at G=8.3.

---

## Renders

| File | Description |
|------|-------------|
| `00_earth_reference/cmb_fullsky.png` | Full-sky CMB mollview, Earth marked, top-50 patches |
| `00_earth_reference/earth_cmb_patch.png` | 30°×30° zoom on Earth's CMB seed region |
| `00_earth_reference/earth_reference_card.png` | Solar system RV + transit profiles |
| `02_gaia_targets/full_catalogue_map.png` | All 1,287 G-stars on CMB sky |
| `04_skypy_lss/skypy_highl_patches.png` | Matter overdensity NSIDE=2048, 12 patches |
| `04_skypy_lss/matter_power_spectrum_highl.png` | P(k) lmax=8000 |
| `04_skypy_lss/cl_cmb_vs_matter.png` | CMB TT vs projected matter C_ℓ |
| `06_planck/planck_real_vs_um_targets.png` | Planck real sky vs UM simulation targets |
| `06_planck/planck_earth_patch_real.png` | Earth's CMB patch in Planck real data |
| `07_planet_concept/gaya.png` | Gaya (Ouroboros d) — image gen |
| `07_planet_concept/system_overview.png` | Full Ouroboros system |

---

## Requirements

```
python >= 3.12
camb
healpy
numpy >= 2.0
scipy
matplotlib
astropy
astroquery
lightkurve
```

UM/LiMB: `/home/joe/Desktop/UNIFIED_MECHANICS_v2`

---

*Joseph Shields · Unified Mechanics · 2026*
