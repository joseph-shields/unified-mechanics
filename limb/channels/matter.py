# LiMB — Light instigating Matter Barrier
# Copyright (c) 2026 Joseph Shields — LGPL v3+  (see limb/LICENSE)
"""
LiMB **M**atter channel — baryon + CDM source terms.

In the trivial-channel limit (UM → GR), this returns zero. Drop UM
matter-sector corrections in here as derivations land. The matter
channel is the one most likely to fix the Apollo familiarity issues
seen in DGF chains: CMB peak-height ratios and lensing smoothing are
both dominated by matter-sector physics.
"""
from __future__ import annotations

import jax.numpy as jnp


def source_fn(state, tau, k, cosmo):
    """Matter-channel contribution to the perturbation RHS."""
    return jnp.zeros_like(state)
