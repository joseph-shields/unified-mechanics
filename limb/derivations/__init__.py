"""
LiMB UM derivation registry.

Each function below returns the UM-derived value of a cosmological
quantity that LCDM treats as a free input. The registry is **strict**:
if a derivation has not been written, the function raises
``NotImplementedError`` with a pointer to the open-derivation note.
Nothing in LiMB silently falls back to a LCDM fiducial.

Usage::

    from osiris.limb.derivations import lcdm_inputs as D
    H0 = D.H0()                # 67.x ± 0.x  (UM-derived value)
    Omega_b = D.Omega_b()
    Omega_c = D.Omega_c()
    ...

Drop the actual UM math into the function bodies as the derivations
land. Tests in ``tests/test_limb_derivations.py`` (to be written)
should pin every returned value against the published UM result so a
regression in the algebra is caught immediately.
"""
from __future__ import annotations
