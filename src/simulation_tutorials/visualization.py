"""Reusable ASE visualization helpers for the tutorial notebooks."""

from __future__ import annotations

import contextlib
import shutil
from pathlib import Path
from typing import Iterable

from ase.io import write
from IPython.display import Image as IPythonImage
from IPython.display import display
from PIL import Image

_TEMP_FILES = ("temp.ini", "temp.pov", "temp.png")


def _resize_image(image: Image.Image, max_size: tuple[int, int] | None, stretch_y: float) -> Image.Image:
    if max_size is None:
        return image

    new_size = (max_size[0], int(max_size[1] * stretch_y))
    return image.resize(new_size, Image.LANCZOS)


def _cleanup_temp_files() -> None:
    for temp_name in _TEMP_FILES:
        temp_path = Path(temp_name)
        if temp_path.exists():
            temp_path.unlink()


def render_structure(
    structure,
    *,
    repeat: tuple[int, int, int] = (1, 1, 1),
    rotation: str = "15z,-60x",
    max_size: tuple[int, int] | None = None,
    stretch_y: float = 1.0,
    output_dir: str | Path = "./output",
    png_name: str = "temp.png",
    display_image: bool = True,
) -> Path:
    """Render an ASE structure with POV-Ray and save the rendered assets."""

    atoms = structure.repeat(repeat) if repeat != (1, 1, 1) else structure
    renderer = write("./temp.pov", atoms, rotation=rotation)
    renderer.render()

    with Image.open("./temp.png") as opened:
        image = _resize_image(opened.copy(), max_size=max_size, stretch_y=stretch_y)

    if display_image:
        display(image)

    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)

    for temp_name in _TEMP_FILES:
        source = Path(temp_name)
        if not source.exists():
            continue

        target_name = png_name if temp_name == "temp.png" else source.name
        target = destination / target_name
        if target.exists():
            target.unlink()
        shutil.move(str(source), target)

    return destination / png_name


def repeat_and_render(
    structure,
    *,
    repeats: tuple[int, int, int] = (3, 3, 1),
    rotation: str = "15z,-60x",
    **kwargs,
) -> Path:
    """Expand a slab-like structure before rendering it."""

    expanded = structure.copy()
    expanded = expanded * repeats
    expanded.cell = structure.cell
    return render_structure(expanded, rotation=rotation, **kwargs)


def save_structure_frame(
    structure,
    file_name: str,
    *,
    rotation: str = "15z,-70x",
    max_size: tuple[int, int] | None = None,
    stretch_y: float = 1.0,
    output_dir: str | Path = "./output",
) -> Path:
    """Render a structure and save only the PNG frame."""

    renderer = write("./temp.pov", structure, rotation=rotation)
    renderer.render()

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    with Image.open("./temp.png") as opened:
        image = _resize_image(opened.copy(), max_size=max_size, stretch_y=stretch_y)
        frame_path = output_path / file_name
        image.save(frame_path)

    _cleanup_temp_files()
    return frame_path


def png_frames_to_gif(
    png_dir: str | Path,
    gif_path: str | Path,
    *,
    duration: int = 200,
    pattern: str = "frame*",
    display_gif: bool = True,
) -> Path:
    """Combine rendered PNG frames into an animated GIF."""

    png_dir = Path(png_dir)
    gif_path = Path(gif_path)
    png_files = sorted(png_dir.glob(pattern))

    if not png_files:
        raise ValueError(f"No PNG files found in {png_dir}")

    gif_path.parent.mkdir(parents=True, exist_ok=True)

    with contextlib.ExitStack() as stack:
        images = [stack.enter_context(Image.open(png)) for png in png_files]
        first_image = images[0]
        first_image.save(
            fp=gif_path,
            format="GIF",
            append_images=images[1:],
            save_all=True,
            duration=duration,
            loop=0,
        )

    if display_gif:
        display(IPythonImage(filename=str(gif_path)))

    return gif_path


def trajectory_to_gif(
    trajectory: Iterable,
    *,
    png_dir: str | Path = "./output",
    gif_path: str | Path = "./output/animation.gif",
    duration: int = 200,
    rotation: str = "15z,-70x",
    max_size: tuple[int, int] | None = None,
    stretch_y: float = 1.0,
) -> Path:
    """Render each structure in a trajectory and bundle the frames into a GIF."""

    png_dir = Path(png_dir)
    png_dir.mkdir(parents=True, exist_ok=True)

    for frame_index, atoms in enumerate(trajectory):
        file_name = f"frame_{frame_index:02d}.png"
        save_structure_frame(
            atoms,
            file_name=file_name,
            rotation=rotation,
            max_size=max_size,
            stretch_y=stretch_y,
            output_dir=png_dir,
        )

    return png_frames_to_gif(png_dir=png_dir, gif_path=gif_path, duration=duration)
