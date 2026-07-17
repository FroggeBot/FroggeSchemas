from __future__ import annotations

from pathlib import Path

__all__ = ["find_repo_root"]


def find_repo_root(start_file: Path, marker: str = ".env") -> Path:
    """Walk upward from start_file looking for the nearest ancestor directory containing `marker`.

    Falls back to start_file's own parent directory if nothing is found (e.g. a
    fresh checkout with no .env yet, or CI where secrets come from real
    environment variables). Works identically whether the caller lives inside a
    monorepo package or at the root of its own standalone repo.
    """
    for candidate in start_file.resolve().parents:
        if (candidate / marker).exists():
            return candidate
    return start_file.resolve().parent
