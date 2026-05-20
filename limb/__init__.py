# LiMB — Light instigating Matter Barrier
# Copyright (c) 2026 Joseph Shields — LGPL v3+  (see limb/LICENSE)
"""
LiMB — *Light instigating Matter Barrier*.

A zero-free-parameter CMB forward solver. All cosmological inputs are
derived from a single boundary condition (φ² = φ + 1) via the golden
ratio φ and its contraction rate r = 1/(2φ).

Quickstart
----------
::

    from limb import compute_limb_lcdm_cls, planck_lcdm_reference_cls
    import numpy as np

    um     = compute_limb_lcdm_cls(lmax=2500)
    planck = planck_lcdm_reference_cls(lmax=2500)

    ell = um["ells"]
    residual = (um["totCl_TT"] - planck["totCl_TT"]) / planck["totCl_TT"]
    print(f"Peak residual: {np.abs(residual[2:]).max()*100:.2f}%")

Pipeline
--------
``derivations`` → ``Cosmology`` → ``CAMBparams`` → C_ℓ

1. :mod:`limb.derivations.lcdm_inputs` — closed-form UM derivations (no deps).
2. :func:`build_LiMBLCDMCosmology` — assemble all values into a frozen
   :class:`~limb.cosmology.Cosmology` parameter container.
3. :func:`cosmology_to_camb_params` — translate ``Cosmology`` → ``CAMBparams``.
4. :func:`compute_limb_lcdm_cls` — run CAMB end-to-end, return C_ℓ dict.

The three channels
------------------
:mod:`limb.channels` holds the L / M / B source-function stubs for the
future JAX Boltzmann solver. In the current trivial-channel limit they
return zero, recovering standard LCDM.
"""
from __future__ import annotations

from limb.cosmology import Cosmology
from limb.lcdm import build_LiMBLCDMCosmology, LiMBLCDMCosmology
from limb.um import build_LiMBUMCosmology, LiMBUMCosmology
from limb.camb_backend import (
    cosmology_to_camb_params,
    build_camb_params,
    compute_limb_lcdm_cls,
    planck_lcdm_reference_cls,
)

__all__ = [
    # Core types
    "Cosmology",
    # Cosmology builders
    "build_LiMBLCDMCosmology",
    "build_LiMBUMCosmology",
    # CAMB pipeline
    "cosmology_to_camb_params",
    "build_camb_params",
    "compute_limb_lcdm_cls",
    "planck_lcdm_reference_cls",
    # Legacy aliases
    "LiMBLCDMCosmology",
    "LiMBUMCosmology",
]
