# AI1220 — Lab 08: Collaborative Playlist

A collaborative playlist created for **Software, Web & Mobile Engineering**. The FastAPI backend and vanilla-JavaScript frontend communicate through the shared API contract in `CONTRACT.md`.

## Required setup

This folder belongs at `lab08_playlist/` in each partner's AI1220 GitHub repository.

```bash
cd lab08_playlist
uv sync --frozen
uv run python backend.py
```

Visit:

- Web app: http://127.0.0.1:8000/
- Interactive FastAPI documentation: http://127.0.0.1:8000/docs

Use the **backend URL**, not Live Server and not a local `file://` URL. Saving `backend.py` restarts the server with the three starter songs. Songs are stored in memory, not in a database.

## Features

1. On page load, GET `/songs` renders one card per song, in the server's original order.
2. Add Song sends `POST /songs` with `title` and `artist`, clears both inputs on success, and reloads the live list.
3. Vote sends `POST /songs/{id}/vote` and reloads the live vote totals.
4. The server rejects empty/missing song fields (400) and nonexistent votes (404) with the common `{ "error": "..." }` structure. The page displays the server's exact message.
5. All song text is HTML-escaped using the starter template's `esc()` helper.

## File responsibility

| File | Description |
| --- | --- |
| `CONTRACT.md` | Jointly agreed API paths, bodies and status codes (marked: 30%) |
| `backend.py` | Backend role, the 3 FastAPI endpoints and root web page (marked: 35%) |
| `index.html` | Frontend role, Fetch API and live playlist cards (marked: 35%) |
| `TEAM.md` | Names, GitHub usernames and roles; partner details must be completed |
| `pyproject.toml`, `uv.lock` | Provided locked dependencies for Python 3.13 |
| `test_backend.py` | Extra regression checks for the contract and edge cases |

## Run automated checks

```bash
uv run python -m unittest -v test_backend.py
```

Manual integration check: start the app, confirm the three starting songs; add a fourth song (including via `/docs`) and refresh the page; vote on it; submit an empty artist and verify the exact backend error message appears. The frontend never hardcodes the playlist.

## Submission

Commit and push `lab08_playlist/` on your own repository's `main` branch. The two partners must agree on `CONTRACT.md` and end with matching app files. The professor requires a separate commit of the file you personally owned during Step 2; follow that requirement when collaborating.
