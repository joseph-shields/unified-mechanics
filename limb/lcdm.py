# LiMB — Light instigating Matter Barrier
# Copyright (c) 2026 Joseph Shields — LGPL v3+  (see limb/LICENSE)
"""
LiMB-LCDM — zero-free-parameter LCDM, every value derived from UM.

This is the **trivial-channel limit** of UM. Every LCDM input is a
UM closed form (sourced to Paper 1 / extended/11). Two dimensional
anchors remain: T_CMB (FIRAS, 2.7255 K) and H_0 (CMB-anchored
Friedmann closure, ~67.4 km/s/Mpc). UM derives the SHAPE of both
but not their absolute scale, which is the irreducible cost of
turning a dimensionless recursion into a dimensional cosmology.

If LiMB-LCDM disagrees with a reference LCDM run at the same field
values, the bug is in the LiMB pipeline, not the framework. If
LiMB-LCDM agrees with LCDM but disagrees with Planck observation by
more than the 3% braiding floor at the relevant cycle count, the bug
is either in the UM derivations (drift in the algebra encoding) or in
the framework itself.
"""
from __future__ import annotations

from osiris.cosmology import Cosmology
from osiris.limb.derivations import lcdm_inputs as D


# Dimensional anchors. UM derives the shape of both but not the
# absolute scale (recursion is dimensionless).
H0_DIMENSIONAL_ANCHOR_KM_S_MPC = 67.4   # CMB-anchored Friedmann closure


def build_LiMBLCDMCosmology() -> Cosmology:
    """Construct an ``osiris.Cosmology`` with every field set by UM.

    All derivations from ``osiris.limb.derivations.lcdm_inputs`` must
    be DERIVED or OBSERVATIONAL. Any OPEN derivation raises through.
    Returns a stock ``Cosmology`` instance — usable directly with the
    IRIS pipeline (``osiris.delphi.pipeline.compute_cls_fast`` etc.)
    with no special handling.
    """
    return Cosmology(
        H0      = H0_DIMENSIONAL_ANCHOR_KM_S_MPC,   # dimensional anchor
        Omega_b = D.Omega_b(),                      # r²/2
        Omega_c = D.Omega_c(),                      # 4r²(1-r)
        Omega_k = 0.0,                              # flat (channel sum = 1)
        T_cmb   = D.T_cmb_K(),                      # FIRAS anchor (2.7255)
        N_eff   = D.N_eff(),                        # 3 + r²/2
        Y_He    = D.Y_He(),                         # (1-r)²/2
        n_s     = D.n_s(),                          # 1 - r²/φ²
        A_s     = D.A_s(),                          # r¹⁷
        k_pivot = 0.05,
        w0      = D.w0(),                           # -(r+2)/(8r)
        wa      = D.wa(),                           # 32r⁵(1-r)/Ω_DE
    )


# τ_reio is set at the pipeline level (via ``z_reio`` / ``delta_z``
# in ``compute_cls_fast`` kwargs), not on the Cosmology container.
# UM derivation: τ_reio = 2r³ ≈ 0.0590. This is converted to z_reio
# via the standard reionisation history; central UM value lands
# z_reio ≈ 8.5.
TAU_REIO_UM = 2.0 * (D.R ** 3)   # ≈ 0.0590
Z_REIO_UM_APPROX = 8.5            # convertible from τ_reio via standard
                                  # reionisation model


# Backwards-compatible alias for any test code that imports the class.
LiMBLCDMCosmology = build_LiMBLCDMCosmology
