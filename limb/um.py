# LiMB — Light instigating Matter Barrier
# Copyright (c) 2026 Joseph Shields — LGPL v3+  (see limb/LICENSE)
"""
LiMB-UM cosmology — full three-channel extension.

Sums the L / M / B source terms and routes them through the existing
``Cosmology.extra_source_fn`` hook so the rest of the solver pipeline
(IRIS kernel) is untouched.

In the trivial-channel limit (every channel returns zero), this is
bit-for-bit identical to ``LiMBLCDMCosmology`` — that's the
self-consistency unit test.
"""
from __future__ import annotations

from limb.cosmology import Cosmology
from limb.lcdm import build_LiMBLCDMCosmology
from limb.channels import light, matter, barrier


def _limb_um_source_fn(state, tau, k, cosmo):
    """Three-channel sum: L + M + B."""
    return (light.source_fn(state, tau, k, cosmo)
            + matter.source_fn(state, tau, k, cosmo)
            + barrier.source_fn(state, tau, k, cosmo))


def build_LiMBUMCosmology() -> Cosmology:
    """Construct a UM-derived cosmology with the L+M+B perturbation
    extension attached via ``extra_source_fn``.

    In the trivial-channel limit (every ``source_fn`` returns zero),
    this is bit-for-bit identical to ``build_LiMBLCDMCosmology()`` —
    the same Cosmology dataclass plus a no-op extra_source_fn.
    """
    base = build_LiMBLCDMCosmology()
    import dataclasses
    return dataclasses.replace(base, extra_source_fn=_limb_um_source_fn)


# Backwards-compatible aliases
LiMBUMCosmology = build_LiMBUMCosmology
