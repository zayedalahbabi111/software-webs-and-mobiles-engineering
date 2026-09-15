# Lab 04 report

Student name: zayedalahbabi111 (GitHub username; replace with your official course name if required)

Date: 2026-09-15

Repository: zayedalahbabi111/software-webs-and-mobiles-engineering

Status: Lab 04 implementation completed and pushed to GitHub. Direct API and code-level verification passed. Browser-only visual checks are listed separately because the execution environment blocks localhost pages in Chromium.

## Exercise 1 - Explore and make a commit

- Working folder: `lab04`
- Git repository root: `software-webs-and-mobiles-engineering`
- Initial report commit hash (`Start lab04 report`): `80aa94af174cd0414891ee67205e5bafc1f55405`
- Files included in that commit: `lab04/REPORT.md` only
- What was saved in that commit: the Lab 04 report starter, repository details, and the frontend/backend explanation before the implementation commit.
- Which file owns the playlist, and why: `backend.py` owns the in-memory `songs` list, validates additions, and assigns the server-side IDs.
- Which file displays the playlist, and why: `index.html` provides the page, form, and JavaScript that fetches the server data and creates the visible list items.
- How the initial song gets from the server to the page: on page load, `loadSongs()` calls `GET /songs`; the backend returns the seed song as JSON; the frontend creates a list item from that response.
- Codex access issues and instructor-supported alternatives, if any: none recorded for GitHub access. The automated Chromium environment blocked localhost navigation, so browser-only checks must be confirmed once on a normal local browser.

## Exercise 2 - Backend

- Explain your completed `create_song(payload)` function: it first verifies that both required fields exist and are strings, trims surrounding whitespace, checks that each trimmed value is between 1 and 80 characters, then creates a song using the current `next_id`, appends it to `songs`, increments `next_id`, and returns the stored song.
- Explain how both fields are validated and stored: `title` and `artist` are handled using the same presence/type checks and the same 1-80 character rule after `.strip()`. Only the trimmed values are stored. Extra input fields are ignored.
- Explain how rejected input leaves the playlist and next ID unchanged: every validation step happens before the song is appended or `next_id` is incremented. A `ValueError` exits the function before either global value is changed.
- Accepted direct request checked before Exercise 3, and observation: `POST /songs` with `{"title":"  Quiet Road  ","artist":"Sample Artist"}` returned `201 Created` and `{"id":2,"title":"Quiet Road","artist":"Sample Artist"}`.
- Rejected direct request checked before Exercise 3, and observation: a whitespace-only title returned `400 Bad Request` with a helpful error, and the next accepted item still received the next unused ID.

## Exercise 3 - Frontend

- Visible heading after your edit: `My playlist`
- Explain your completed `sendSong(title, artist)` function: it calls the supplied `requestJSON()` helper for `/songs`, specifies `POST`, sends `Content-Type: application/json`, serializes the exact form values with `JSON.stringify({ title, artist })`, and returns the helper result.
- Explain how the request method, path, headers, and body match the contract: method is `POST`, path is `/songs`, the JSON content type is declared, and the body contains exactly `title` and `artist`. Trimming and validation stay in Python as required.
- Observed behavior after an accepted form submission: the supplied form handler resets the form only after `sendSong()` resolves, then calls `loadSongs()` and displays `Song added.`. The `sendSong()` request shape was executed in a JavaScript test and passed. A normal-browser visual confirmation is still required because localhost navigation is blocked in this environment.
- Observed behavior after a rejected form submission: the supplied catch path shows `error.message`, re-enables the button, and returns before `form.reset()` or `loadSongs()`, so the inputs/list are retained by design. Direct API rejection was verified; visual browser confirmation remains to be done locally.
- How you checked that the display matches what the server stores: `loadSongs()` always rebuilds the list from `GET /songs`, so after a successful POST the page reads the server's list rather than constructing a separate client-side copy.

## Exercise 4 - Actual verification observations

| Check from page 3 | Actual observation | Pass/fail |
| --- | --- | --- |
| Fresh start: GET shows only First Light / Demo Band, ID 1 | After restarting the server, `GET /songs` returned only `[{"id":1,"title":"First Light","artist":"Demo Band"}]`. | Pass |
| Form: Blue Sky / Test Duo appears once; fields clear | Frontend request/reset code reviewed; localhost browser execution is blocked in this environment. | Local browser check required |
| Refresh: both songs remain | Server stores accepted songs in memory and `loadSongs()` reads `GET /songs`; visual refresh check requires local browser. | Local browser check required |
| Form: another invented song with different values works | `sendSong()` was executed with JavaScript stubs and produced the required POST body. | Code path pass; local visual check required |
| Direct addition: 201, trimmed values, next unused ID | Quiet Road request returned 201, trimmed values, ID 2. | Pass |
| Whitespace-only title: 400; no new song | Returned 400 with `Title must contain between 1 and 80 characters after trimming.` | Pass |
| Missing artist: 400 | Returned 400 with `Missing required field: artist.` | Pass |
| Numeric title: 400 | Returned 400 with `Title must be a string.` | Pass |
| 81-character title: 400 | Returned 400 with the 1-80 character error. | Pass |
| 80-character title: accepted | Returned 201 and was stored. | Pass |
| Rejected additions do not consume an ID | After four rejected requests following ID 2, the valid 80-character title was assigned ID 3. | Pass |
| Form rejection: visible error, retained inputs, unchanged list | Supplied handler logic reviewed; browser visual confirmation requires local browser. | Local browser check required |
| Corrected form submission succeeds | Backend accepts corrected valid input and frontend success path is complete. | Code path pass; local visual check required |
| Keyboard: Tab and Enter work | Native labels, inputs, and submit button are present; direct keyboard execution is blocked with localhost browser access here. | Local browser check required |
| Network: POST payload, 201 status, JSON response, following GET | POST/GET were verified directly with HTTP requests; DevTools visual inspection requires local browser. | API pass; DevTools check required |
| Restart and refresh: only the seed song remains | Restarted the server and `GET /songs` again returned only the seed song. | Pass |

### One successful request and response

Request method and path: `POST /songs`

Request headers: `Content-Type: application/json`

Actual request body:

```json
{"title":"  Quiet Road  ","artist":"Sample Artist"}
```

Actual response status and headers: `201 Created`, `Content-Type: application/json`, `Cache-Control: no-store`

Actual response body:

```json
{"id":2,"title":"Quiet Road","artist":"Sample Artist"}
```

What the following GET and page showed: the following direct `GET /songs` contained the seed song and the new trimmed `Quiet Road` entry. The page code reads this same endpoint; visual page confirmation should be done locally.

### One failed request and response

Request method and path: `POST /songs`

Request headers: `Content-Type: application/json`

Actual request body:

```json
{"title":"   ","artist":"Sample Artist"}
```

Actual response status and headers: `400 Bad Request`, `Content-Type: application/json`, `Cache-Control: no-store`

Actual response body:

```json
{"error":"Title must contain between 1 and 80 characters after trimming."}
```

Evidence that the playlist and next ID were unchanged: after the valid ID 2 addition, whitespace-only, missing-artist, numeric-title, and 81-character-title requests were rejected; the next accepted request received ID 3. Therefore no rejected request consumed an ID.

### One code change I reviewed

File and change: `backend.py` - implemented `create_song(payload)`.

My explanation of the change: validation is completed before mutation. Only after both trimmed fields pass the contract does the function build the new song, append it, and increment `next_id`.

Observed result and why it agrees with the contract: direct HTTP checks showed trimmed stored values, sequential IDs for accepted requests, 400 errors for invalid requests, and no ID gaps caused by rejected requests. That matches the supplied API contract.

## Submission

- Final implementation commit (`Complete lab04 playlist`): recorded by GitHub after the final commit is created.
- Files included and review notes: `lab04/backend.py`, `lab04/index.html`, `lab04/REPORT.md`, `lab04/README.md`, and `lab04/.gitignore`.
- Push and GitHub verification: files are written directly to the repository `main` branch through the connected GitHub account; final verification is performed after the commit.
- Optional stretch, if attempted: not attempted.
