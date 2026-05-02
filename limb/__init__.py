# LiMB — Light instigating Matter Barrier
# Copyright (c) 2026 Joseph Shields — LGPL v3+  (see limb/LICENSE)
"""
LiMB — *Light instigating Matter Barrier*.

The UM-derived CAMB-backend solver.

Two operating modes:

* :class:`limb.lcdm.LiMBLCDMCosmology` — zero-free-parameter
  LCDM. Every input value comes from
  :mod:`limb.derivations.lcdm_inputs`. Validation target:
  parity with CAMB on Planck LCDM.
* :class:`limb.um.LiMBUMCosmology` — same parameter container
  plus the three-channel UM source-term extension wired via
  ``Cosmology.extra_source_fn``.

The three channels live under :mod:`limb.channels`:

    L  light    — radiation sector
    M  matter   — baryons + CDM
    B  barrier  — recombination / decoupling threshold + light↔matter
                  coupling

The acronym is the architecture.
"""
from __future__ import annotations

from .lcdm import LiMBLCDMCosmology
from .um import LiMBUMCosmology

__all__ = ["LiMBLCDMCosmology", "LiMBUMCosmology"]
