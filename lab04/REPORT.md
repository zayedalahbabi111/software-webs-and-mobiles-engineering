# Lab 04 report

Student name: zayedalahbabi111 (GitHub username; replace with your official name if required)

Date: 2026-09-15

Repository: zayedalahbabi111/software-webs-and-mobiles-engineering

Status: Started - Lab 04 report created before the implementation commit.

## Exercise 1 - Explore and make a commit

- Working folder: lab04
- Git repository root: software-webs-and-mobiles-engineering
- Initial report commit hash (`Start lab04 report`): TODO - recorded after this commit is created
- Files included in that commit: lab04/REPORT.md only
- What was saved in that commit: the Lab 04 report starter and repository details
- Which file owns the playlist, and why: backend.py owns the in-memory `songs` list and assigns IDs on the server.
- Which file displays the playlist, and why: index.html renders the page and uses JavaScript to fetch and display songs.
- How the initial song gets from the server to the page: the page calls GET /songs on load; the server returns the seed song as JSON; JavaScript creates list items from that response.
- Codex access issues and instructor-supported alternatives, if any: none recorded.

## Exercise 2 - Backend

- Explain your completed `create_song(payload)` function: TODO
- Explain how both fields are validated and stored: TODO
- Explain how rejected input leaves the playlist and next ID unchanged: TODO
- Accepted direct request checked before Exercise 3, and observation: TODO
- Rejected direct request checked before Exercise 3, and observation: TODO

## Exercise 3 - Frontend

- Visible heading after your edit: TODO
- Explain your completed `sendSong(title, artist)` function: TODO
- Explain how the request method, path, headers, and body match the contract: TODO
- Observed behavior after an accepted form submission: TODO
- Observed behavior after a rejected form submission: TODO
- How you checked that the display matches what the server stores: TODO

## Exercise 4 - Actual verification observations

Fill in the actual result and pass/fail only after running each check.

| Check from page 3 | Actual observation | Pass/fail |
| --- | --- | --- |
| Fresh start: page and GET show only First Light / Demo Band, ID 1 | TODO | TODO |
| Form: Blue Sky / Test Duo appears once; fields clear | TODO | TODO |
| Refresh: both songs remain | TODO | TODO |
| Form: another invented song with different values works | TODO | TODO |
| Direct addition: 201, trimmed values, next unused ID; visible after refresh | TODO | TODO |
| Whitespace-only title: 400; no new song | TODO | TODO |
| Missing artist: 400 | TODO | TODO |
| Numeric title: 400 | TODO | TODO |
| 81-character title: 400 | TODO | TODO |
| 80-character title: accepted | TODO | TODO |
| Rejected additions do not consume an ID | TODO | TODO |
| Form rejection: visible error, retained inputs, unchanged list | TODO | TODO |
| Corrected form submission succeeds | TODO | TODO |
| Keyboard: Tab and Enter work | TODO | TODO |
| Network: POST payload, 201 status, JSON response, following GET | TODO | TODO |
| Restart and refresh: only the seed song remains | TODO | TODO |

### One successful request and response

Request method and path: TODO

Request headers: TODO

Actual request body:

```text
TODO
```

Actual response status and headers: TODO

Actual response body:

```text
TODO
```

What the following GET and page showed: TODO

### One failed request and response

Request method and path: TODO

Request headers: TODO

Actual request body:

```text
TODO
```

Actual response status and headers: TODO

Actual response body:

```text
TODO
```

Evidence that the playlist and next ID were unchanged: TODO

### One code change I reviewed

File and change: TODO

My explanation of the change: TODO

Observed result and why it agrees with the contract: TODO

## Submission

- Final commit hash (`Complete lab04 playlist`): TODO
- Files included and review notes: TODO
- Push and GitHub verification: TODO
- Optional stretch, if attempted: not attempted
