from __future__ import annotations

from datetime import datetime
from typing import Literal

from .base import BaseSchema


class GitHubActivityEntry(BaseSchema):
    """One row in the Frogge Tech Solutions site's "what I'm building right now" widget. `detail`
    is deliberately generic (no commit message or branch name) for anything from a private repo -
    see api.routers.public for why."""

    id: str
    kind: Literal["push", "create", "delete"]
    repo: str
    detail: str
    timestamp: datetime
