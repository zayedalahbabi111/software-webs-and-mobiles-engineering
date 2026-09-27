# Campus Workshop Board - Design notes

Name: Zayed Alahbabi
Student ID: Not supplied

## Diagram files

Each source is one editable diagrams.net page; each export is the matching vector SVG.

| View | Editable source | Export |
|---|---|---|
| 01-context | [01-context.drawio](diagrams/source/01-context.drawio) | [01-context.svg](diagrams/exports/01-context.svg) |
| 02-containers | [02-containers.drawio](diagrams/source/02-containers.drawio) | [02-containers.svg](diagrams/exports/02-containers.svg) |
| 03-components | [03-components.drawio](diagrams/source/03-components.drawio) | [03-components.svg](diagrams/exports/03-components.svg) |
| 04-code | [04-code.drawio](diagrams/source/04-code.drawio) | [04-code.svg](diagrams/exports/04-code.svg) |
| 05-dynamic | [05-dynamic.drawio](diagrams/source/05-dynamic.drawio) | [05-dynamic.svg](diagrams/exports/05-dynamic.svg) |

## One structural choice (Exercise 2)

One server-rendered web application with a PostgreSQL database keeps deployment and maintenance small for 200 students while database transactions enforce durable, concurrency-safe reservations.

## Your components (Exercise 3)

All seven components are TypeScript modules inside **Board Web App**, not separate services.

| Name | Job | Customer rule(s) served |
|---|---|---|
| Web Routes | Handle HTTPS forms, require authentication on board routes, call use cases and render HTML with precise outcomes. | R1-R6 |
| Identity Gate | Verify credentials using Campus Identity; issue and validate signed, expiring session cookies; supply trusted student ID, name and email. | R1, R4 |
| Workshop Rules | Validate creation, generate unique IDs, set creator as owner, and permit only that owner to publish without reserving a seat. | R2, R5 |
| Board Queries | Read published workshop summaries and the caller's reservation; check stored ownership before returning attendee names/emails. | R3, R5 |
| Reservation Rules | Reject unverified calls, serialize decisions per workshop, return existing seats unchanged, enforce publication/capacity, and request email only for newly committed seats. | R1, R4-R6 |
| Workshop Store | Persist workshops and reservations, provide transactions and row locks, and return stored state for refresh. | R2-R5 |
| Confirmation | Request University Mail once after commit; return Requested or Unavailable without changing reservations. | R6 |

## Reservation operation (Exercise 4)

See **04-code**, including the typed `ReservationService.reserve` contract, result variants, ordered algorithm and overlap proof. The invariant is `0 <= reservationCount(w) <= capacity(w)` and at most one stored reservation per `(workshopId, studentId)`. Every writer locks the same workshop row until commit; existing-reservation lookup and count run as later statements at READ COMMITTED, so a waiting caller sees the preceding commit. A unique database constraint also enforces the pair. Email occurs after commit, never on the Existing path.

## Ari's incident (Exercise 5)

| Observation | Result |
|---|---|
| Stored state before | W17, "Build a tiny game", owner S10, published, capacity 3; reservation student IDs {S21, S22}; 2 seats taken, 1 remaining; S23 has none. |
| Stored state after | W17 and its ownership, title, time, publication and capacity unchanged; reservation student IDs {S21, S22, S23}; new reservation R-W17-S23 stores W17, S23, Ari, ari@example.invalid and its creation time; 3 seats taken, 0 remaining. Existing reservations are unchanged. R-W17-S23 is an illustrative generated ID. |
| Message Ari sees | Your place in "Build a tiny game" is reserved. Confirmation email is unavailable. Your reservation is still saved. |

Refreshing reads the saved S23 reservation and 0 remaining seats. Repeating Reserve returns that same reservation unchanged, with no additional seat or email request.
