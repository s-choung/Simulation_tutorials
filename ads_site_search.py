"""Backward-compatible wrapper for the extracted surface-site helper."""

from pathlib import Path
import sys

SRC_DIR = Path(__file__).resolve().parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


def get_surface_sites(*args, **kwargs):
    from simulation_tutorials.surface_sites import get_surface_sites as _get_surface_sites

    return _get_surface_sites(*args, **kwargs)


__all__ = ["get_surface_sites"]
