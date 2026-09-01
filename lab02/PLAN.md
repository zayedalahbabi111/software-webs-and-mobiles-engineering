# Plan — LabLoans

## Process choice

### How stable and binding are the requirements?

The one-sentence brief leaves users, policies, and the meaning of “losing” unresolved, so requirements are not yet stable or contractual. They are likely to change after staff and borrowers see an early workflow.

### How quickly can real feedback arrive?

The lab technician and student borrowers are available on campus, so they can review a usable increment and provide feedback within days.

### What does failure cost?

Failure may cause equipment loss, privacy breaches, or disruption to practical classes, but the first increment can be trialled with a small equipment set and test records to limit harm.

### How many pieces must move together?

Loans, borrower identities, inventory status, and notifications must agree, but the core issue-and-return workflow can deliver value before reminders, reports, and other capabilities are added.

Verdict: Use short increments. The requirements are uncertain, feedback is readily available, a controlled pilot limits failure cost, and the product can be divided into independently useful slices.

## Milestones

| Milestone | When | What is true then |
|---|---|---|
| Core workflow accepted | End of Week 2 | A technician has issued and returned a test item, and the borrower has viewed the active loan; all Sprint 1 acceptance checks pass. |
| Controlled pilot complete | End of Week 4 | At least 20 real loans across one equipment category have been recorded, with every issued item showing a borrower, due date, and current status. |
| Loss-control release ready | End of Week 6 | Reminders, the overdue list, supervisor approval for items over £500, and access-control tests have all passed. |

## Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Staff bypass the service during busy handovers, leaving incomplete records. | Medium | Observe the current handover process, keep the issue/return flow under 30 seconds, and pilot it at one desk before wider rollout. |
| Borrower or inventory data is inaccurate, linking a loan to the wrong person or item. | Medium | Validate borrower and asset identifiers at entry, display a confirmation summary, and reconcile pilot records with the existing inventory each day. |
| Loan information is exposed to unauthorised users. | Low | Apply role-based access, use test accounts for each role, and include cross-user access checks in every release. |
