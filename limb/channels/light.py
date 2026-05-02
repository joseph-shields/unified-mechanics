# LiMB — Light instigating Matter Barrier
# Copyright (c) 2026 Joseph Shields — LGPL v3+  (see limb/LICENSE)
"""
LiMB **L**ight channel — radiation-sector source terms.

In the trivial-channel limit (UM → GR), this returns zero and
LiMB-LCDM reduces to standard linear-perturbation cosmology.
UM photon/neutrino corrections enter here.
"""
from __future__ import annotations

import jax.numpy as jnp


def source_fn(state, tau, k, cosmo):
    """Light-channel contribution to the perturbation RHS.

    Parameters
    ----------
    state : jnp.ndarray
        Full perturbation state vector at conformal time ``tau`` for
        wavenumber ``k``. Layout matches the vendored DISCO-EB
        synchronous-gauge hierarchy (see
        synchronous-gauge perturbation hierarchy.
    tau : float
        Conformal time, Mpc.
    k : float
        Wavenumber, 1/Mpc.
    cosmo : Cosmology
        Cosmology instance.

    Returns
    -------
    jnp.ndarray
        Same shape as ``state``. Trivial-channel limit returns zeros.
    """
    return jnp.zeros_like(state)
