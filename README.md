# Frogge Schemas

Pydantic models shared by [API](https://github.com/FroggeBot/FroggeAPI),
[Bot](https://github.com/FroggeBot/FroggeBot), and
[Worker](https://github.com/FroggeBot/FroggeWorker) — the wire-format/contract layer for the
Frogge Discord venue-management project. No I/O, no framework dependencies beyond Pydantic.

## What's in here

- `guild.py`, `position.py`, `event.py`, `event_template.py`, `vip.py`, `profiles.py`,
  `verification.py`, `admin_access.py` — one module per domain, matching the API's own
  one-model-file-per-domain layout.
- `plugin_auth.py`, `plugin_event.py`, `plugin_profile.py`, `plugin_vip.py` — the read/write
  contracts for [FroggePlugin](../Plugin/README.md)'s Discord-identity-scoped endpoints, kept
  separate from the guild-admin schemas above.
- `enums.py` — `FroggeEnum`, a `StrEnum` subclass auto-deriving snake_case wire values from
  PascalCase member names plus a `proper_name` display property (overridable via
  `_proper_name_overrides()` for cases like "Miqo'te" that don't survive title-casing).
- `servicetoken.py` — `issue_service_token`/`verify_service_token`, the per-guild HMAC bearer
  scheme every API request is authenticated with.
- `envutil.py` — `find_repo_root`, used by every other package's `Settings` class to locate the
  shared root `.env`.

## Versioning

API/Bot/Worker each pin `schemas` to a public git tag in their own committed `pyproject.toml`
(`tool.uv.sources`), so a change here only reaches them once it's tagged and bumped there. For
local cross-package development, the workspace root's `pyproject.toml` (one level up) overrides
this with a live path dependency — see the root `CLAUDE.md` for the full workspace layout.

## Development

```
uv sync
uv run ruff check . --fix
uv run mypy .
```

No test suite of its own yet — schema behavior (enum wire values, `FroggeEnum` overrides, service
token issue/verify round-trips) is exercised indirectly via API's test suite.
