"""Utilities shared across the SNU computational materials tutorials."""

from importlib import import_module

__all__ = [
    "get_surface_sites",
    "png_frames_to_gif",
    "relax_structure",
    "render_structure",
    "repeat_and_render",
    "save_structure_frame",
    "status_bar",
    "trajectory_to_gif",
]

_EXPORT_MAP = {
    "get_surface_sites": ("simulation_tutorials.surface_sites", "get_surface_sites"),
    "png_frames_to_gif": ("simulation_tutorials.visualization", "png_frames_to_gif"),
    "relax_structure": ("simulation_tutorials.optimization", "relax_structure"),
    "render_structure": ("simulation_tutorials.visualization", "render_structure"),
    "repeat_and_render": ("simulation_tutorials.visualization", "repeat_and_render"),
    "save_structure_frame": ("simulation_tutorials.visualization", "save_structure_frame"),
    "status_bar": ("simulation_tutorials.progress", "status_bar"),
    "trajectory_to_gif": ("simulation_tutorials.visualization", "trajectory_to_gif"),
}


def __getattr__(name):
    if name not in _EXPORT_MAP:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    module_name, attr_name = _EXPORT_MAP[name]
    value = getattr(import_module(module_name), attr_name)
    globals()[name] = value
    return value
