from __future__ import annotations

import hashlib
import hmac


def issue_service_token(guild_id: int, *, secret: str) -> str:
    """Issues a service token for the given guild ID using the provided secret."""
    signature = hmac.new(secret.encode(), str(guild_id).encode(), hashlib.sha256).hexdigest()
    return f"{guild_id}.{signature}"

def verify_service_token(token: str, *, secret: str) -> int | None:
    """Verifies the provided service token using the given secret."""
    try:
        guild_id_part, signature = token.split(".", 1)
        guild_id = int(guild_id_part)
    except ValueError:
        return None

    expected = hmac.new(secret.encode(), guild_id_part.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature):
        return None

    return guild_id

_INTERNAL_MARKER = "internal"

def issue_internal_token(*, secret: str) -> str:
    """Issues a service token for cross-guild/internal endpoints, not scoped to any single guild."""
    signature = hmac.new(secret.encode(), _INTERNAL_MARKER.encode(), hashlib.sha256).hexdigest()
    return f"{_INTERNAL_MARKER}.{signature}"

def verify_internal_token(token: str, *, secret: str) -> bool:
    """Verifies the provided internal service token using the given secret."""
    try:
        marker, signature = token.split(".", 1)
    except ValueError:
        return False

    if marker != _INTERNAL_MARKER:
        return False

    expected = hmac.new(secret.encode(), marker.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)
