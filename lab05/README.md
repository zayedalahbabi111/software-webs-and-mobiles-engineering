# Lab 5 - C4 Design Challenge

90 minutes. Work individually in `lab05/` inside your existing private `ai1220` repository.

Read the two-page student sheet. Produce four C4 views and one dynamic diagram for the Campus Workshop Board. No application code or long report is required.

1. Copy this folder's contents into `ai1220/lab05/` without creating a nested repository.
2. Use any diagramming tool. Save editable files in `diagrams/source/` and readable PDF/SVG/PNG exports in `diagrams/exports/`.
3. Follow the five questions in the sheet. Use `DESIGN.md` only for the brief notes and component list; the diagrams carry the explanation.
4. Check consistency and readability. Commit and push before the session ends, then verify files and instructor access on GitHub.

Weights: context 15%, containers 20%, components 25%, code 15%, dynamic 25%. Partial work earns proportional credit.

AI assistance is allowed; check and understand its output. No paid service, real credentials or application setup is needed. If tooling or submission fails, save locally and ask the instructor for help before the session ends.

References: [C4 views](https://c4model.com/diagrams), [dynamic diagrams](https://c4model.com/diagrams/dynamic), [notation](https://c4model.com/diagrams/notation).

## Completed submission

Open [DESIGN.md](DESIGN.md) for the required brief notes, component list, operation reference, and Ari's before/after state. The submission contains five editable diagrams.net sources and five matching SVG exports; no application implementation is needed.

| Exercise | Readable export | Editable source |
|---|---|---|
| 1 - Context (15%) | [01-context.svg](diagrams/exports/01-context.svg) | [01-context.drawio](diagrams/source/01-context.drawio) |
| 2 - Containers (20%) | [02-containers.svg](diagrams/exports/02-containers.svg) | [02-containers.drawio](diagrams/source/02-containers.drawio) |
| 3 - Components (25%) | [03-components.svg](diagrams/exports/03-components.svg) | [03-components.drawio](diagrams/source/03-components.drawio) |
| 4 - Code (15%) | [04-code.svg](diagrams/exports/04-code.svg) | [04-code.drawio](diagrams/source/04-code.drawio) |
| 5 - Dynamic (25%) | [05-dynamic.svg](diagrams/exports/05-dynamic.svg) | [05-dynamic.drawio](diagrams/source/05-dynamic.drawio) |

SVGs are vector diagrams: open the file at full size and zoom for the detailed component and runtime views. Sources have editable text, shapes and connectors. Each view has one page; the dynamic view wraps one numbered sequence into panels A-D on that page.

Design basis: the supplied two-page Lab 5 student sheet, the [C4 notation guidance](https://c4model.com/diagrams/notation), and the [C4 dynamic-diagram guidance](https://c4model.com/diagrams/dynamic). The locking argument uses PostgreSQL [row locks](https://www.postgresql.org/docs/current/explicit-locking.html#LOCKING-ROWS) with later statements at [READ COMMITTED](https://www.postgresql.org/docs/current/transaction-iso.html#XACT-READ-COMMITTED). The external HTTPS/JSON interfaces are proposed contracts; the brief does not prescribe vendor APIs.

Submission details still requiring the student: supply official name/student ID in DESIGN.md, and confirm the instructor accepts this course repository's name and public visibility rather than the sheet's private `ai1220` repository. Instructor collaborator access has not been verified.
