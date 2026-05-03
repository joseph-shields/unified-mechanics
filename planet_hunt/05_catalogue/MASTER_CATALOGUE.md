# CMB-Guided Planet Hunt — Master Catalogue
**Method:** Unified Mechanics (UM) → LiMB/CAMB power spectrum → CMB realization (seed 271828) → seed-region matching → Gaia DR3 G-star query → habitability scoring

---

## The Idea

The CMB temperature fluctuation at any sky position is the fossil record of the density perturbation that seeded structure formation there. Earth formed in a region seeded by a CMB patch at T ≈ 23 µK (measured in seed 271828, 5° disc average, Laniakea/Great Attractor direction RA=243° Dec=-60°).

Other sky positions with the same CMB temperature formed under the same initial conditions. We should look for Earth-like planets there.

---

## Earth — Reference Target

| Property | Value |
|----------|-------|
| CMB seed direction | RA=243.0° Dec=-60.0° (Laniakea Great Attractor) |
| CMB temperature | 23.2 µK (5° disc, seed 271828) |
| CMB ΔT from self | 0.00 µK |
| Star type | G2V, Teff=5778K |
| HZ planets | Venus (0.72 AU), **Earth (1.00 AU)**, Mars (1.52 AU) |
| Earth transit depth | 84 ppm, 13.0 hr duration |
| Earth RV signal | K = 0.0895 m/s |
| Combined V+E+M RV peak | ~0.19 m/s |

**Renders:** `00_earth_reference/`

---

## CMB Pipeline

| Parameter | Value |
|-----------|-------|
| UM/LiMB CAMB lmax | 3000 |
| HEALPix NSIDE | 512 (high-res) / 64 (targeting) |
| Seed | 271828 |
| Earth CMB temperature | 23.2 µK |
| Match threshold | ΔT < 8 µK |
| Matched sky fraction | 1.2% (575 patches at NSIDE=64) |

**Files:** `01_cmb_pipeline/cmb_targets_{ra,dec,dT}.npy`

---

## Top 50 CMB Seed Positions

Ranked by |T_CMB − T_Earth|. Position #1 is Earth itself.

| # | RA (°) | Dec (°) | ΔT (µK) |
|---|--------|---------|---------|
| 1 | 242.56 | −59.68 | 0.00 ← **Earth** |
| 2 | 42.50 | 76.81 | 0.04 |
| 3 | 2.93 | 55.87 | 0.05 |
| 4 | 9.14 | −31.39 | 0.06 |
| 5 | 137.11 | 38.68 | 0.06 |
| 6 | 82.27 | −34.23 | 0.07 |
| 7 | 277.03 | 6.58 | 0.07 |
| 8 | 113.20 | 1.19 | 0.09 |
| 9 | 40.08 | −41.81 | 0.10 |
| 10 | 298.12 | −29.31 | 0.10 |

---

## Gaia G-Star Catalogue

**1,287 unstudied G-type stars** in Earth-CMB seed regions.

Query parameters:
- Gaia DR3 `teff_gspphot` 5100–6300 K
- Parallax > 2 mas (within 500 pc)
- Parallax S/N > 8
- RUWE < 1.4 (single star, clean astrometry)
- G magnitude < 14
- Cross-matched against NASA exoplanet archive — known hosts excluded

**Files:** `02_gaia_targets/cmb_gstar_targets.json`, `cmb_ranked_targets.json`

---

## Top 10 Priority Targets

Ranked by combined score: CMB match (40%) + solar similarity (30%) + HZ temperature (20%) + planet size (10%)

| # | Gaia Source ID | RA (°) | Dec (°) | Teff (K) | log g | Dist (pc) | G mag | CMB ΔT |
|---|----------------|--------|---------|----------|-------|-----------|-------|--------|
| 1 | 675329552985501209 | 298.874 | −29.097 | 5664 | 4.42 | 51 | 8.3 | 0.10 µK |
| 2 | 675172432344067212 | 297.243 | −29.729 | 5799 | 4.43 | 100 | 9.7 | 0.10 µK |
| 3 | 290067141679412787 | 83.271 | −34.495 | 5751 | 4.34 | 75 | 9.1 | 0.07 µK |
| 4 | 494856356929219110 | 40.841 | −41.852 | 5730 | 4.44 | 109 | 10.0 | 0.10 µK |
| 5 | 420654804990989696 | 1.969 | 55.577 | 5867 | 4.27 | 49 | 7.7 | 0.05 µK |
| 6 | 393289891154301580 | 186.922 | 14.259 | 5656 | 4.45 | 82 | 9.5 | 0.13 µK |
| 7 | 675191801358525747 | 297.098 | −29.528 | 5667 | 4.49 | 74 | 9.4 | 0.10 µK |
| 8 | 447716348950177318 | 276.762 | 6.273 | 5724 | 4.36 | 99 | 9.8 | 0.07 µK |
| 9 | 482312368929392396 | 81.242 | −34.205 | 5495 | 4.41 | 38 | 7.9 | 0.07 µK |
| 10 | 290172643256082982 | 82.275 | −33.429 | 5645 | 4.48 | 107 | 10.2 | 0.07 µK |

---

## Target #1 — Full Simulation

**Gaia 675329552985501209**
RA=298.874° Dec=−29.097° | Teff=5664K | 51pc | G=8.3 | CMB ΔT=0.10µK

Predicted 3-planet HZ architecture:

| Planet | a (AU) | Period (days) | Size | Teq (K) | RV K (m/s) | Transit depth | Duration |
|--------|--------|--------------|------|---------|------------|---------------|---------|
| HZ-1 | 0.962 | 350.9 | 1.00 Re | 254 | 0.093 | 87 ppm | 12.8 hr |
| HZ-2 | 1.299 | 550.4 | 1.40 Re | 219 | 0.160 | 170 ppm | 14.8 hr |
| HZ-3 | 1.753 | 863.3 | 1.10 Re | 188 | 0.084 | 105 ppm | 17.2 hr |

Peak combined RV: **0.337 m/s** — within ESPRESSO capability at G=8.3

**Telescope strategy:**
1. ESPRESSO/HARPS — RV campaign, ~3 yr baseline needed
2. TESS re-observation — watch for single transit events
3. JWST — atmospheric spectroscopy once confirmed

**Render:** `03_target_cards/gaia_target_simulation.png`

---

## Known Candidates (Confirmed + Unconfirmed)

| Planet | Status | Teff (K) | Rp (Re) | Teq (K) | Dist (pc) | CMB ΔT |
|--------|--------|----------|---------|---------|-----------|--------|
| TOI-4503.01 | **Unconfirmed** | 5334 | 2.09 | 244 | unknown | 8.6 µK |
| TOI-700 d | Confirmed | 3459 | 1.07 | 255 | 31 | 8.4 µK |
| Kepler-452 b | Confirmed | 5757 | 1.63 | 265 | 552 | 73.6 µK |
| Kepler-1126 c | Confirmed | 5678 | 1.45 | 305 | 636 | 82.9 µK |
| Kepler-1649 c | Confirmed | 3240 | 1.06 | 234 | 92 | 85.6 µK |

---

## Pipeline Scripts

| Script | Purpose |
|--------|---------|
| `01_cmb_pipeline/` | CMB map generation + seed region finding |
| `02_gaia_targets/` | Gaia query + habitability scoring |
| `03_target_cards/` | Per-target system simulations |
| `04_skypy_lss/skypy_lss_pipeline.py` | SkyPy LSS simulation for seed patches |

---

## Citation / Framework

**Cosmological inputs:** All derived from Unified Mechanics (UM) via LiMB/CAMB backend.
No ΛCDM free parameters — H0, Ωb, Ωc, ns, As all closed-form functions of r from c²=c+1.

**Gaia data:** Gaia DR3 (ESA), queried via astroquery TAP.
**Exoplanet catalogue:** NASA Exoplanet Archive.
**CMB simulation:** healpy synfast, UM-derived Cl, seed 271828.

---

*Joseph Shields · Unified Mechanics · 2026*
