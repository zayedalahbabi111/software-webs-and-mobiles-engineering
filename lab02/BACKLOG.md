# Backlog — LabLoans

## Items

- [F] The lab technician can record each equipment loan against an identified borrower and a due date.
- [F] Borrowers can see the equipment they currently hold and when each item is due.
- [F] The lab technician can record an item's return and its condition.
- [F] Borrowers receive a reminder before an item becomes overdue.
- [NF] Loan records are visible only to authorised lab staff and the borrower concerned.
- [NF] A loan or return can be recorded within 30 seconds during normal lab operation.
- [F] The lab technician can see all overdue items and the borrowers responsible.
- [F] The lab technician can record that a loan requires supervisor approval when its value exceeds £500.
- [F] The lab technician can mark equipment as unavailable when it is damaged or under maintenance.
- [NF] The service preserves confirmed loan records if a user's session or network connection fails.
- [F] The lab technician can export a monthly summary of loans, late returns, and missing items. (assistant)
- [F] Borrowers can report a fault against equipment they currently hold. (assistant)

## The change

The client added: "Any loan worth more than £500 must be approved by a supervisor." I placed that requirement eighth: it is an important loss-control measure, but the core ability to issue, return, remind, and trace overdue loans must come first. It did not enter Sprint 1, so it displaced nothing; Sprint 1 remains fixed at three selected items.

## From the assistant

Kept:

- [F] The lab technician can export a monthly summary of loans, late returns, and missing items. (assistant) — kept because it gives the client checkable evidence of whether losses are decreasing.
- [F] Borrowers can report a fault against equipment they currently hold. (assistant) — kept because early fault reporting helps distinguish damaged equipment from missing equipment.

Rejected:

- [F] Borrowers can reserve equipment in advance. — rejected because reservations do not directly address lost equipment and would broaden the first release.
- [F] Borrowers can rate equipment after returning it. — rejected because ratings do not support accountability or asset recovery.
- [F] The system can recommend equipment based on previous loans. — rejected because recommendations are outside the client's loss-prevention goal.
