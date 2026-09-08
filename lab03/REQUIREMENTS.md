# CampusPulse requirements

Name or team: Zayed Alahbabi

Date: 7 September 2026

Status: validated baseline for first release

Use the source IDs `S1` to `S6` from the lab handout. Keep every requirement
short enough to test and trace.

## 1. Release scope

### In scope

- Browser-based access through university sign-in for a pilot of 5,000 students and 200 groups.
- Verified-group profiles with official badges and approved-officer publishing permissions.
- Shared drafts and publication of announcements and events for university-wide or members-only audiences.
- Following groups, viewing a combined feed, RSVP with private-by-default visibility, and change or cancellation notifications.
- Corrections, reporting, immediate moderation hiding, audit records, preserved appeal evidence, and appeals.
- Controls for group impersonation and repeated announcements from compromised accounts.

### Out of scope

- Native mobile applications and access by external users.
- Direct messages and payments.
- Video hosting and AI recommendations.

## 2. User requirements

- UR-1 [Must] Students need one mobile-friendly, accessible feed for events and announcements from groups they follow. [Source: S1]
- UR-2 [Must] Students need their RSVP identity to remain private unless they explicitly choose public visibility. [Source: S1, S5]
- UR-3 [Must] Approved group officers need to share drafts and publish announcements and events to university-wide or members-only audiences. [Source: S2]
- UR-4 [Must] Students who RSVP need to be informed when an event's place or time changes or when the event is cancelled. [Source: S2]
- UR-5 [Must] Campus moderators need reports containing the reported content and reason, with the ability to hide content while preserving evidence and decision accountability for appeals. [Source: S3]
- UR-6 [Must] Students need an official badge to identify groups checked by Student Affairs. [Source: S4, S6]
- UR-7 [Must] Student Affairs needs the browser service to support a pilot of 5,000 students and 200 groups before Orientation Week. [Source: S4]
- UR-8 [Must] The Data Protection Officer needs only necessary personal data collected and cancelled-event attendance data deleted within 30 days. [Source: S5]

## 3. Functional requirements

Write at least six observable system behaviours. Start each one with "The
system shall" and trace it to one or more user requirements.

Format: `FR-1 [Must] The system shall ... [Source: UR-1]`

- FR-1 [Must] The system shall
- FR-2 [Must] The system shall
- FR-3 [Must] The system shall
- FR-4 [Must] The system shall
- FR-5 [Must] The system shall
- FR-6 [Must] The system shall

## 4. Non-functional requirements

Write at least four measurable quality requirements. State what is measured,
the target, and the condition under which the target applies. If you introduce
a number that is not in the handout, record it as an assumption or open
question in Section 8.

Format: `NFR-1 [Must] The system shall ... [Measure: target and condition] [Source: UR-1]`

- NFR-1 [Must] The system shall
- NFR-2 [Must] The system shall
- NFR-3 [Should] The system shall
- NFR-4 [Must] The system shall

## 5. User stories and acceptance criteria

Write at least three stories from different stakeholder viewpoints. Each story
needs at least two acceptance criteria. Across the set, include a failure,
permission boundary, privacy rule, or other non-happy path.

### US-1 [Source: S?, UR-?]

As a <role>,

I want <capability>,

so that <benefit>.

Acceptance criteria:

-
-

### US-2 [Source: S?, UR-?]

As a <role>,

I want <capability>,

so that <benefit>.

Acceptance criteria:

-
-

### US-3 [Source: S?, UR-?]

As a <role>,

I want <capability>,

so that <benefit>.

Acceptance criteria:

-
-

## 6. MoSCoW summary

List requirement or story IDs in every category. The Won't category must state
what is excluded from this release.

- Must:
- Should:
- Could:
- Won't this release:

## 7. Traceability

Add at least four complete paths. Every row should connect evidence to a user
requirement, a system requirement, and a user story.

| Stakeholder need | User requirement | System requirement | User story |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## 8. Assumptions and open questions

Separate decisions your team has assumed from questions that still need an
answer.

### Assumptions

- A1:

### Open questions

- Q1:
