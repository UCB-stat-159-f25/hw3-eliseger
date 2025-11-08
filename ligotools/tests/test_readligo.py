import os
from pathlib import Path
import numpy as np
from ligotools import readligo as rl


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"

H1_FILE = DATA_DIR / "H-H1_LOSC_4_V2-1126259446-32.hdf5"
L1_FILE = DATA_DIR / "L-L1_LOSC_4_V2-1126259446-32.hdf5"

def _flex_loaddata(fn, det):
    """
    Normalize rl.loaddata output across variants:
      - (strain, time, dt, utc)
      - (strain, time, dt)
      - (strain, time, meta_dict)
    Returns: (strain, time, dt, utc_or_None)
    """
    out = rl.loaddata(fn, det)
    if not isinstance(out, (tuple, list)):
        raise AssertionError("loaddata should return a tuple/list")

    if len(out) == 4:
        strain, time, dt, utc = out
    elif len(out) == 3:
        strain, time, third = out
        utc = None
        if np.isscalar(third):
            dt = float(third)
        elif isinstance(third, dict):
            dt = third.get("dt", None)
            if dt is None:
                dt = float(np.median(np.diff(time)))
        else:
            dt = float(np.median(np.diff(time)))
    else:
        raise AssertionError(f"Unexpected loaddata() return length: {len(out)}")

    dt = float(dt)
    return strain, time, dt, utc

def test_loaddata_basic_structure():
    """loaddata returns 1-D arrays with positive dt and consistent time grid."""
    strain, time, dt, _ = _flex_loaddata(H1_FILE, "H1")
    n = len(strain)
    assert n > 0 and len(time) == n
    assert dt > 0.0
    est_dt = float(np.median(np.diff(time)))
    assert np.isfinite(est_dt) and abs(est_dt - dt) < 1e-6

def test_sample_rate_consistency_between_detectors():
    """H1 and L1 for the same event should have identical dt."""
    _, _, dt_H1, _ = _flex_loaddata(H1_FILE, "H1")
    _, _, dt_L1, _ = _flex_loaddata(L1_FILE, "L1")
    assert abs(dt_H1 - dt_L1) < 1e-10