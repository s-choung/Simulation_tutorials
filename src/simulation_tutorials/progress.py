"""Simple text progress helpers for notebook loops."""

from __future__ import annotations


def status_bar(
    proceed: float,
    *,
    segments: int = 20,
    increment: float = 5,
    filled: str = "#",
    empty: str = ".",
) -> str:
    """Return a fixed-width progress bar string."""

    completed = max(0, min(segments, int(proceed / increment)))
    return f"{filled * completed}{empty * (segments - completed)}"
