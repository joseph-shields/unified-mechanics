"""
LiMB three-channel structure: **L**ight, **M**atter, **B**arrier.

Each channel module exposes a ``source_fn(state, tau, k, cosmo)``
callable that returns its contribution to the perturbation RHS in
synchronous gauge. The full LiMB-UM extension is the sum:

    extra_source_fn = lambda state, tau, k, cosmo: (
        light.source_fn(state, tau, k, cosmo)
        + matter.source_fn(state, tau, k, cosmo)
        + barrier.source_fn(state, tau, k, cosmo)
    )

Channel responsibilities
------------------------
* ``light``    — radiation sector: photon and neutrino contributions
                that UM modifies relative to GR. Trivial-channel limit
                returns zero.
* ``matter``   — baryon + CDM sector contributions. Trivial-channel
                limit returns zero.
* ``barrier``  — recombination / decoupling threshold and the
                light↔matter coupling at decoupling. Includes the
                photon-baryon Compton coupling and any UM modification
                to it. Trivial-channel limit recovers standard
                Thomson coupling.

The acronym **LiMB** is literal: the *limb* in cosmology is the
photon-matter decoupling surface. UM places it explicitly inside the
solver as a separable channel rather than a passive consequence of
recombination physics.
"""
from __future__ import annotations

from . import light, matter, barrier

__all__ = ["light", "matter", "barrier"]
