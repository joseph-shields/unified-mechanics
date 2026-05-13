"""Ouroboros system map — full architecture render."""
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Ellipse, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap

fig, ax = plt.subplots(figsize=(24, 13))
fig.patch.set_facecolor("#02020c")
ax.set_facecolor("#02020c")

# ── Stellar/planet data ───────────────────────────────────────────────
planets = [
    # name,   AU,     period,   Re,    Teq,   color,          type
    ("Nabu",   0.28,  "56d",   0.45,   497,  "#c8935a",      "rock"),
    ("Ishtar", 0.55,  "155d",  0.92,   354,  "#e8d870",      "venus"),
    ("Gaya",   0.962, "351d",  1.00,   254,  "#3a8fcc",      "earth"),
    ("Tiamat", 1.30,  "550d",  1.40,   219,  "#2255aa",      "ocean"),
    ("Ares",   1.75,  "863d",  1.10,   188,  "#b04020",      "mars"),
    ("Indra",  4.80,  "10.9yr",10.5,   120,  "#d4a060",      "gas"),
    ("Kronos", 9.80,  "31.8yr", 9.0,    84,  "#e8d8a0",      "saturn"),
    ("Skadi",  19.5,  "89yr",   3.8,    60,  "#7090cc",      "ice"),
]

# Log-scale x axis for AU
AU_MAX = 22.0
def au_to_x(au):
    return np.log10(au / 0.25) / np.log10(AU_MAX / 0.25)

# ── Draw orbits as horizontal lines ───────────────────────────────────
Y_ORBIT = 0.50    # vertical center
ORBIT_HALF = 0.06  # half-height of orbit lane

for name, au, period, re, teq, col, ptype in planets:
    x = au_to_x(au)
    ax.axvline(x, color=col, alpha=0.12, lw=0.8, ymin=0.05, ymax=0.95)

# ── HZ band ───────────────────────────────────────────────────────────
hz_inner_au = 0.85
hz_outer_au = 1.58
x_hz_i = au_to_x(hz_inner_au)
x_hz_o = au_to_x(hz_outer_au)
ax.axvspan(x_hz_i, x_hz_o, alpha=0.07, color="#44ff44", zorder=0)
ax.text((x_hz_i+x_hz_o)/2, 0.93, "Habitable Zone",
        color="#44ff88", fontsize=8, ha="center", transform=ax.transAxes, alpha=0.7)

# ── Snow line ─────────────────────────────────────────────────────────
x_snow = au_to_x(2.41)
ax.axvline(x_snow, color="#aaccff", alpha=0.25, lw=1.0, ls="--")
ax.text(x_snow + 0.005, 0.88, "Snow line\n2.4 AU",
        color="#aaccff", fontsize=7, transform=ax.transAxes, alpha=0.6)

# ── Star ──────────────────────────────────────────────────────────────
x_star = au_to_x(0.05)
star_size = 0.055
from matplotlib.patches import Circle
# Glow
for r, a in [(0.10, 0.04), (0.07, 0.08), (0.045, 0.18), (0.028, 0.5)]:
    c = Circle((x_star, Y_ORBIT), r, color="#ffaa44",
                alpha=a, transform=ax.transAxes, zorder=5)
    ax.add_patch(c)
star_circ = Circle((x_star, Y_ORBIT), star_size*0.38, color="#ffcc55",
                    transform=ax.transAxes, zorder=6,
                    linewidth=0)
ax.add_patch(star_circ)
ax.text(x_star, Y_ORBIT - 0.14, "Ouroboros A\n5664 K · 0.93 R☉",
        color="#ffcc88", fontsize=8, ha="center", transform=ax.transAxes)

# ── Planets ───────────────────────────────────────────────────────────
# Scale planet sizes for display — log radius
def planet_display_r(re):
    return 0.006 + 0.020 * np.log10(max(re, 0.5))

for i, (name, au, period, re, teq, col, ptype) in enumerate(planets):
    x = au_to_x(au)
    r_disp = planet_display_r(re)

    # Planet circle
    p_circ = Circle((x, Y_ORBIT), r_disp, color=col,
                     transform=ax.transAxes, zorder=7, linewidth=0)
    ax.add_patch(p_cisp := p_circ)

    # Saturn rings for Kronos
    if ptype == "saturn":
        ring = Ellipse((x, Y_ORBIT), r_disp*3.8, r_disp*0.35,
                       color="#e8d8a0", alpha=0.5,
                       transform=ax.transAxes, zorder=6)
        ax.add_patch(ring)
    # Thin ring for Indra
    if ptype == "gas":
        ring = Ellipse((x, Y_ORBIT), r_disp*2.8, r_disp*0.25,
                       color="#c0a060", alpha=0.35,
                       transform=ax.transAxes, zorder=6)
        ax.add_patch(ring)

    # Gaya highlight
    if name == "Gaya":
        for r_g, a_g in [(r_disp*2.2, 0.12), (r_disp*1.5, 0.18)]:
            gc = Circle((x, Y_ORBIT), r_g, color="#44ccff",
                        alpha=a_g, transform=ax.transAxes, zorder=6)
            ax.add_patch(gc)

    # Name label above
    ax.text(x, Y_ORBIT + r_disp + 0.065,
            f"{name}",
            color=col, fontsize=9, ha="center",
            transform=ax.transAxes, fontweight="bold" if name=="Gaya" else "normal")

    # Stats below
    ax.text(x, Y_ORBIT - r_disp - 0.06,
            f"{au} AU\n{period}",
            color="#888899", fontsize=6.5, ha="center",
            transform=ax.transAxes)

    # Teq
    ax.text(x, Y_ORBIT - r_disp - 0.135,
            f"{teq}K",
            color="#556677", fontsize=6, ha="center",
            transform=ax.transAxes)

    # Re label
    ax.text(x, Y_ORBIT - r_disp - 0.175,
            f"{re} R⊕",
            color="#445566", fontsize=6, ha="center",
            transform=ax.transAxes)

# ── AU axis ───────────────────────────────────────────────────────────
au_ticks = [0.3, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0]
for au_t in au_ticks:
    x_t = au_to_x(au_t)
    ax.axvline(x_t, color="#1a1a2e", lw=0.5, zorder=1)
    ax.text(x_t, 0.04, f"{au_t} AU",
            color="#333355", fontsize=6.5, ha="center",
            transform=ax.transAxes)

ax.axis("off")
ax.set_xlim(0, 1); ax.set_ylim(0, 1)

fig.suptitle(
    "THE OUROBOROS SYSTEM  ·  Gaia 675329552985501209  ·  51 pc  ·  RA 298.874°  Dec −29.097°\n"
    "Derived from Unified Mechanics CMB seed matching  ·  ΔT = 0.10 µK from Earth",
    color="white", fontsize=12, fontweight="bold", y=0.97)

# Legend
legend_items = [
    mpatches.Patch(color="#3a8fcc", label="Gaya (d) — Earth-twin, 1.00 Re, 351d ← TARGET"),
    mpatches.Patch(color="#2255aa", label="Tiamat (e) — Water super-Earth, 1.40 Re"),
    mpatches.Patch(color="#b04020", label="Ares (f) — Frozen Mars-plus, 1.10 Re"),
    mpatches.Patch(color="#d4a060", label="Indra (g) — Gas giant, 10.5 Re"),
    mpatches.Patch(color="#e8d8a0", label="Kronos (h) — Ringed, 9.0 Re"),
    mpatches.Patch(color="#7090cc", label="Skadi (i) — Ice giant, 3.8 Re"),
]
ax.legend(handles=legend_items, loc="upper right",
          bbox_to_anchor=(0.99, 0.97),
          facecolor="#05050f", labelcolor="white",
          fontsize=7.5, framealpha=0.9)

out = "/home/joe/Desktop/PLANET_HUNT/07_planet_concept/ouroboros_system_map.png"
fig.savefig(out, dpi=160, bbox_inches="tight", facecolor="#02020c")
plt.close(fig)
print(f"System map → {out}")
