"""Conceptual render — HZ-1 around Gaia 675329552985501209."""
import sys, warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
from scipy.ndimage import gaussian_filter

np.random.seed(8675309)

# ── Target parameters ─────────────────────────────────────────────────
STAR_TEFF   = 5664.0    # K  (vs Sun 5778K)
STAR_RADIUS = 0.93      # Rsun  (estimated from Teff/logg)
STAR_LOGG   = 4.42
STAR_DIST   = 51.0      # pc
STAR_GMAG   = 8.3

P_AU        = 0.962     # semi-major axis
P_DAYS      = 350.9
P_RE        = 1.00      # Earth radii
P_TEQ       = 254.0     # K  (no greenhouse)
P_TEQ_GH    = 288.0     # K  estimated with Earth-like greenhouse
P_TRANSIT   = 87.0      # ppm
P_RV        = 0.093     # m/s

# ── Blackbody colour of star (approx RGB from Teff) ───────────────────
def teff_to_rgb(T):
    # Krystek/Lindbloom approximation
    T_k = T / 100.0
    if T_k <= 66:
        r = 1.0
        g = np.clip((99.4708025861*np.log(T_k) - 161.1195681661)/255, 0, 1)
        b = 0 if T_k <= 19 else np.clip((138.5177312231*np.log(T_k-10) - 305.0447927307)/255, 0, 1)
    else:
        r = np.clip((329.698727446*(T_k-60)**-0.1332047592)/255, 0, 1)
        g = np.clip((288.1221695283*(T_k-60)**-0.0755148492)/255, 0, 1)
        b = 1.0
    return np.array([r, g, b])

star_rgb = teff_to_rgb(STAR_TEFF)
sun_rgb  = teff_to_rgb(5778.0)

# ── Procedural planet surface ──────────────────────────────────────────
def make_planet_surface(N=512):
    """Ocean-continent surface with clouds — orthographic projection."""
    x = np.linspace(-1, 1, N)
    X, Y = np.meshgrid(x, x)
    R2 = X**2 + Y**2
    sphere = R2 <= 1.0

    # Base terrain — fractal-ish noise
    terrain = np.zeros((N, N))
    for scale, amp in [(0.08, 1.0), (0.04, 0.5), (0.02, 0.25), (0.01, 0.12)]:
        noise = np.random.randn(N, N)
        terrain += amp * gaussian_filter(noise, sigma=N*scale)
    terrain /= terrain[sphere].std()

    # Ocean (below threshold) / land
    sea_level = -0.2   # slightly more ocean than Earth
    land_mask = (terrain > sea_level) & sphere
    sea_mask  = (terrain <= sea_level) & sphere

    # Colour map: deep ocean → shelf → lowland → highland → snow
    rgb = np.zeros((N, N, 3))

    # Ocean
    depth = np.clip((sea_level - terrain) / 2.5, 0, 1)
    rgb[:,:,0] = np.where(sea_mask, 0.02 + 0.08*depth, 0)
    rgb[:,:,1] = np.where(sea_mask, 0.15 + 0.25*(1-depth), 0)
    rgb[:,:,2] = np.where(sea_mask, 0.40 + 0.45*(1-depth), 0)

    # Land
    elev = np.clip((terrain - sea_level) / 2.0, 0, 1)
    # lowland green → brown highlands → snow caps
    r_land = 0.18 + 0.50*elev**1.5
    g_land = 0.35 - 0.20*elev
    b_land = 0.10 + 0.20*elev**2
    # Snow above ~75% elevation
    snow = elev > 0.72
    r_land = np.where(snow, 0.88, r_land)
    g_land = np.where(snow, 0.90, g_land)
    b_land = np.where(snow, 0.95, b_land)
    rgb[:,:,0] = np.where(land_mask, r_land, rgb[:,:,0])
    rgb[:,:,1] = np.where(land_mask, g_land, rgb[:,:,1])
    rgb[:,:,2] = np.where(land_mask, b_land, rgb[:,:,2])

    # Ice caps (polar)
    lat = np.degrees(np.arcsin(np.clip(Y, -1, 1)))
    ice = (np.abs(lat) > 62) & sphere
    rgb[:,:,0] = np.where(ice, 0.90, rgb[:,:,0])
    rgb[:,:,1] = np.where(ice, 0.93, rgb[:,:,1])
    rgb[:,:,2] = np.where(ice, 0.97, rgb[:,:,2])

    # Cloud layer
    cloud_noise = np.zeros((N, N))
    for sc, am in [(0.12, 1.0), (0.06, 0.6), (0.03, 0.3)]:
        cloud_noise += am * gaussian_filter(np.random.randn(N,N), sigma=N*sc)
    cloud_noise /= cloud_noise.std()
    cloud = np.clip((cloud_noise - 0.3) / 1.2, 0, 1)**1.5
    for c in range(3):
        rgb[:,:,c] = np.where(sphere, rgb[:,:,c]*(1-cloud*0.7) + cloud*0.94, 0)

    # Limb darkening
    limb = np.sqrt(np.maximum(1 - R2, 0))
    limb_factor = 0.4 + 0.6 * limb
    for c in range(3):
        rgb[:,:,c] *= np.where(sphere, limb_factor, 1)

    # Atmosphere halo (scattering ring)
    halo = np.exp(-np.maximum(np.sqrt(R2)-1.0, 0) / 0.03) * (R2 > 1.0)
    atm_col = np.array([0.4, 0.65, 1.0]) * star_rgb / sun_rgb
    atm_col = np.clip(atm_col, 0, 1)
    for c in range(3):
        rgb[:,:,c] += halo * atm_col[c] * 0.35

    # Mask outside sphere+halo
    outside = (R2 > 1.12)
    for c in range(3):
        rgb[:,:,c] = np.where(outside, 0, rgb[:,:,c])

    return np.clip(rgb, 0, 1)

# ── Star angular size from HZ-1 ───────────────────────────────────────
# Angular diameter of star as seen from HZ-1
sun_angular_from_earth = 0.533  # degrees
star_angular = sun_angular_from_earth * (STAR_RADIUS / 1.0) / P_AU  # degrees

# ── Build figure ──────────────────────────────────────────────────────
fig = plt.figure(figsize=(20, 14))
fig.patch.set_facecolor("#03030f")

# Grid: planet (large, left), right column (star, stats, orbit)
from matplotlib.gridspec import GridSpec
gs = GridSpec(3, 3, figure=fig,
              left=0.02, right=0.98, top=0.93, bottom=0.04,
              wspace=0.08, hspace=0.35)

ax_planet = fig.add_subplot(gs[:, :2])   # planet spans all rows, left 2 cols
ax_star   = fig.add_subplot(gs[0, 2])
ax_stats  = fig.add_subplot(gs[1, 2])
ax_orbit  = fig.add_subplot(gs[2, 2])

# ── Panel 1: Planet ────────────────────────────────────────────────────
ax_planet.set_facecolor("#03030f")
surf = make_planet_surface(N=600)
ax_planet.imshow(surf, origin="upper",
                 extent=[-1.15, 1.15, -1.15, 1.15],
                 interpolation="lanczos")

# Star glow behind planet (top-left illumination)
from matplotlib.patches import Circle, FancyArrowPatch
glow = plt.Circle((-0.6, 0.6), 0.9, color=star_rgb, alpha=0.04, zorder=0)
ax_planet.add_patch(glow)
glow2 = plt.Circle((-0.6, 0.6), 0.5, color=star_rgb, alpha=0.07, zorder=0)
ax_planet.add_patch(glow2)

ax_planet.set_xlim(-1.18, 1.18)
ax_planet.set_ylim(-1.18, 1.18)
ax_planet.set_aspect("equal")
ax_planet.axis("off")
ax_planet.set_title(
    "HZ-1  ·  Gaia 675329552985501209\n"
    "1.00 R⊕  ·  Teq = 254 K (288 K with greenhouse)  ·  Period = 350.9 d  ·  0.962 AU",
    color="white", fontsize=13, fontweight="bold", pad=10)

# Compass annotation
ax_planet.text(0.02, 0.04, f"CMB ΔT = 0.10 µK  ·  {STAR_DIST} pc  ·  G={STAR_GMAG}",
               transform=ax_planet.transAxes,
               color="#88FFAA", fontsize=10, alpha=0.8)

# ── Panel 2: Star disc ────────────────────────────────────────────────
ax_star.set_facecolor("#03030f")
theta = np.linspace(0, 2*np.pi, 300)
# Limb-darkened star disc
N_s = 200
xs = np.linspace(-1, 1, N_s)
Xs, Ys = np.meshgrid(xs, xs)
Rs2 = Xs**2 + Ys**2
star_img = np.zeros((N_s, N_s, 3))
limb_s = np.sqrt(np.maximum(1 - Rs2, 0))
ld = 0.3 + 0.7 * limb_s   # limb darkening coefficient
for c, col in enumerate(star_rgb):
    star_img[:,:,c] = np.where(Rs2 <= 1.0, col * ld, 0)
# Corona glow
corona = np.exp(-np.maximum(np.sqrt(Rs2)-1.0, 0)/0.15) * (Rs2 > 1.0)
for c, col in enumerate(star_rgb):
    star_img[:,:,c] += corona * col * 0.3
star_img = np.clip(star_img, 0, 1)
ax_star.imshow(star_img, origin="upper", extent=[-1.2, 1.2, -1.2, 1.2])
ax_star.set_xlim(-1.5, 1.5); ax_star.set_ylim(-1.5, 1.5)
ax_star.set_aspect("equal"); ax_star.axis("off")
ax_star.set_title(
    f"Host star  Teff={STAR_TEFF:.0f} K\n"
    f"Angular size from HZ-1: {star_angular:.3f}°  (Sun: 0.533°)",
    color="#FFDDAA", fontsize=9, pad=6)

# ── Panel 3: Stats comparison ─────────────────────────────────────────
ax_stats.set_facecolor("#03030f")
ax_stats.axis("off")

rows = [
    ("",              "HZ-1",          "Earth"),
    ("Radius",        "1.00 R⊕",       "1.00 R⊕"),
    ("Orbital dist",  "0.962 AU",      "1.000 AU"),
    ("Period",        "350.9 d",       "365.25 d"),
    ("Teq (bare)",    "254 K",         "255 K"),
    ("Teq (GH est.)", "~288 K",        "288 K"),
    ("Host Teff",     "5664 K",        "5778 K"),
    ("Host dist",     "51 pc",         "0 pc"),
    ("RV signal",     "0.093 m/s",     "0.090 m/s"),
    ("Transit depth", "87 ppm",        "84 ppm"),
    ("CMB ΔT",        "0.10 µK",       "0.00 µK"),
]

col_x = [0.0, 0.42, 0.78]
y0 = 0.96; dy = 0.083
for i, row in enumerate(rows):
    y = y0 - i * dy
    clr = "#88FFAA" if i == 0 else ("white" if i % 2 == 0 else "#ccccdd")
    for j, cell in enumerate(row):
        weight = "bold" if i == 0 else "normal"
        ax_stats.text(col_x[j], y, cell, transform=ax_stats.transAxes,
                      color=clr, fontsize=8.5, fontweight=weight, va="top")

ax_stats.set_title("HZ-1 vs Earth", color="#88FFAA", fontsize=9, pad=4)

# ── Panel 4: Orbit diagram ────────────────────────────────────────────
ax_orbit.set_facecolor("#03030f")
theta_orb = np.linspace(0, 2*np.pi, 300)

# Draw 3 HZ planet orbits
orbits = [
    (0.962, "HZ-1", "#44FF88", 1.00),
    (1.299, "HZ-2", "#FFAA44", 1.40),
    (1.753, "HZ-3", "#88AAFF", 1.10),
]
# Earth orbit for reference
ax_orbit.plot(np.cos(theta_orb), np.sin(theta_orb),
              color="#555566", lw=0.8, ls="--", alpha=0.5, label="Earth ref")

for a, name, col, rp in orbits:
    ax_orbit.plot(a*np.cos(theta_orb), a*np.sin(theta_orb),
                  color=col, lw=1.2, alpha=0.8)
    # Planet dot at 45°
    ang = np.radians(45 + orbits.index((a, name, col, rp)) * 90)
    ax_orbit.scatter([a*np.cos(ang)], [a*np.sin(ang)],
                     s=max(20, rp**2*40), color=col, zorder=5)
    ax_orbit.text(a*np.cos(ang)+0.07, a*np.sin(ang)+0.07,
                  name, color=col, fontsize=7)

# HZ band
hz_inner, hz_outer = 0.85, 1.85
from matplotlib.patches import Wedge
hz_patch = plt.Circle((0,0), hz_outer, color="#44FF44", alpha=0.04, zorder=0)
ax_orbit.add_patch(hz_patch)
hz_hole  = plt.Circle((0,0), hz_inner, color="#03030f", alpha=1.0, zorder=1)
ax_orbit.add_patch(hz_hole)

# Star
ax_orbit.scatter([0], [0], s=120,
                 color=star_rgb.tolist(), zorder=10,
                 edgecolors="#FFDDAA", linewidths=0.8)

ax_orbit.set_xlim(-2.1, 2.1); ax_orbit.set_ylim(-2.1, 2.1)
ax_orbit.set_aspect("equal"); ax_orbit.axis("off")
ax_orbit.set_title("3-planet HZ system", color="#88FFAA", fontsize=9, pad=4)

# ── Supertitle ────────────────────────────────────────────────────────
fig.suptitle(
    "Planet HZ-1 — Conceptual Portrait\n"
    "CMB-seeded G-type target  ·  Unified Mechanics planet hunt  ·  "
    f"RA=298.874°  Dec=−29.097°",
    color="white", fontsize=14, fontweight="bold", y=0.98)

out = "/home/joe/Desktop/PLANET_HUNT/07_planet_concept/hz1_planet_concept.png"
import os; os.makedirs("/home/joe/Desktop/PLANET_HUNT/07_planet_concept", exist_ok=True)
fig.savefig(out, dpi=160, bbox_inches="tight", facecolor="#03030f")
plt.close(fig)
print(f"Concept render → {out}")
