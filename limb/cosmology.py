# LiMB — Light instigating Matter Barrier
# Copyright (c) 2026 Joseph Shields — LGPL v3+  (see limb/LICENSE)
"""
LiMB Cosmology dataclass.

A minimal frozen parameter container for cosmological inputs.
All fields are set by UM derivations in ``limb.derivations.lcdm_inputs``;
none are free parameters.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional


@dataclass(frozen=True)
class Cosmology:
    """Frozen container for UM-derived cosmological parameters.

    Every field except ``extra_source_fn`` maps directly to a CAMB input.
    All values are set by UM derivations in ``limb.derivations.lcdm_inputs``;
    none are free parameters.

    Fields
    ------
    H0 : float
        Hubble constant, km/s/Mpc. Dimensional anchor (UM derives shape only).
    Omega_b, Omega_c, Omega_k : float
        Baryon, cold-dark-matter, curvature density fractions.
    T_cmb : float
        CMB monopole temperature, K. FIRAS anchor.
    tau_reio : float
        Reionisation optical depth.
    N_eff : float
        Effective neutrino species count.
    m_nu_eV : float
        Sum of neutrino masses, eV.
    Y_He : float
        Primordial helium mass fraction.
    n_s : float
        Scalar spectral index.
    A_s : float
        Scalar amplitude at k_pivot.
    k_pivot : float
        Pivot scale, 1/Mpc.
    w0, wa : float
        Dark-energy equation-of-state parameters (CPL form).
    extra_source_fn : callable or None
        Perturbation-RHS extension hook for the future JAX Boltzmann solver
        (LiMB-UM mode). Unused by the CAMB backend. Signature:
        ``fn(state, tau, k, cosmo) -> array``.
    """
    H0:       float = 67.4
    Omega_b:  float = 0.0
    Omega_c:  float = 0.0
    Omega_k:  float = 0.0
    T_cmb:    float = 2.7255
    tau_reio: float = 0.054
    N_eff:    float = 3.046
    m_nu_eV:  float = 0.06
    Y_He:     float = 0.245
    n_s:      float = 0.9649
    A_s:      float = 2.1e-9
    k_pivot:  float = 0.05
    w0:       float = -1.0
    wa:       float = 0.0
    extra_source_fn: Optional[Callable] = field(default=None, compare=False, hash=False)
