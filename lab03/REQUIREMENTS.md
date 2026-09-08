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

- FR-1 [Must] The system shall authenticate students and officers using university sign-in before granting access. [Source: UR-1, UR-3]
- FR-2 [Must] The system shall display a chronological feed of events and announcements published by groups the signed-in student follows. [Source: UR-1]
- FR-3 [Must] The system shall set each new RSVP identity to private and shall display it publicly only after the student explicitly opts in. [Source: UR-2]
- FR-4 [Must] The system shall allow approved officers of the same group to create and edit a shared draft. [Source: UR-3]
- FR-5 [Must] The system shall permit publication only when the acting account is an approved officer of that group at publication time. [Source: UR-3]
- FR-6 [Must] The system shall restrict members-only content to authenticated members of the publishing group. [Source: UR-3]
- FR-7 [Must] The system shall record each event place, time or cancellation change and identify the officer who made it. [Source: UR-4]
- FR-8 [Must] The system shall notify every current RSVP holder of an event place, time or cancellation change within 5 minutes of the saved change. [Source: UR-4]
- FR-9 [Must] The system shall create a report containing the reporter, reported content snapshot, reason and submission time. [Source: UR-5]
- FR-10 [Must] The system shall allow an authorised moderator to hide reported content immediately without deleting the report or evidence snapshot. [Source: UR-5]
- FR-11 [Must] The system shall record the moderator identity, decision, reason and timestamp for every hide, restore and appeal decision. [Source: UR-5]
- FR-12 [Must] The system shall display an official badge only for a group whose verification status is approved by Student Affairs. [Source: UR-6]
- FR-13 [Must] The system shall permanently delete attendance records linked to a cancelled event no later than 30 days after cancellation. [Source: UR-8]

## 4. Non-functional requirements

- NFR-1 [Must] The system shall expose labels, names, roles and states that meet WCAG 2.2 Level AA success criteria on every student and officer journey. [Measure: zero Level A or AA failures in automated checks plus keyboard and screen-reader review of each release candidate] [Source: UR-1]
- NFR-2 [Must] The responsive browser interface shall render without horizontal page scrolling at viewport widths from 320 to 1440 CSS pixels at 200% zoom, except for content that intrinsically requires two-dimensional layout. [Measure: pass at every tested width on the supported-browser matrix] [Source: UR-1]
- NFR-3 [Must] The system shall support 5,000 registered student accounts and 200 registered group accounts without data loss. [Measure: successful load test using a dataset of at least 5,000 students and 200 groups] [Source: UR-7]
- NFR-4 [Must] The system shall complete at least 95% of feed requests within 2 seconds under 100 concurrent signed-in users. [Measure: server response time measured over a 15-minute representative load test; target and concurrency are assumption A1 pending Orientation Week traffic evidence] [Source: UR-1, UR-7]
- NFR-5 [Must] The system shall prevent an unauthorised account from publishing, viewing members-only content, or changing verification status in 100% of the permission test suite. [Measure: all positive and negative authorisation cases pass before release] [Source: UR-3, UR-6]
- NFR-6 [Must] The system shall complete the scheduled deletion of due cancelled-event attendance records within 24 hours after their 30-day deadline. [Measure: zero overdue attendance records in a daily retention audit; scheduling tolerance is assumption A2] [Source: UR-8]

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
