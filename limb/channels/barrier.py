# LiMB — Light instigating Matter Barrier
# Copyright (c) 2026 Joseph Shields — LGPL v3+  (see limb/LICENSE)
"""
LiMB **B**arrier channel — recombination, decoupling, and the
light↔matter coupling at the decoupling surface.

This is the channel that LiMB names itself after: the *limb* in
cosmology is the photon-matter decoupling surface, where photons stop
being tightly coupled to baryons and become free-streaming
contributions to the CMB. UM treats this as a structural channel, not
a passive consequence of recombination physics.

In the trivial-channel limit, this reduces to standard Thomson
coupling via a Saha + Peebles three-level recombination history.
"""
from __future__ import annotations

import jax.numpy as jnp


def source_fn(state, tau, k, cosmo):
    """Barrier-channel contribution to the perturbation RHS."""
    return jnp.zeros_like(state)
