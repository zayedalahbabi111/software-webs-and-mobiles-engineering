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
- FR-8 [Must] The system shall promptly notify every current RSVP holder when an event's place or time changes or when the event is cancelled. [Source: UR-4]
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

### US-1 [Source: S1, S5, UR-1, UR-2]

As a student attendee,

I want to follow groups and RSVP privately from my phone,

so that I can find relevant events without exposing my attendance.

Acceptance criteria:

- Given a signed-in student who follows two groups, when both groups publish content, then both items appear in the student's chronological feed and meet the NFR-1 accessibility checks.
- Given a student submits an RSVP without changing visibility, when another student views the event, then the RSVP holder's name is absent from the public attendee list.

### US-2 [Source: S2, UR-3, UR-4]

As an approved group officer,

I want officers to collaborate on audience-controlled content and correct event details,

so that the right community receives accurate information.

Acceptance criteria:

- Given officer A saves a draft, when approved officer B opens and publishes it to members only, then group members can view it and non-members receive no content.
- Given an unapproved account attempts to publish the draft, when it submits the action, then publication is rejected and the draft remains unpublished.
- Given an officer saves a changed event time, when the change is processed, then every current RSVP holder is promptly sent a notification identifying the event and changed time.

### US-3 [Source: S3, UR-5]

As a campus moderator,

I want to hide a reported phishing event while retaining evidence and an audit trail,

so that I can protect students and support a fair appeal.

Acceptance criteria:

- Given a report with a reason and content snapshot, when an authorised moderator hides the event, then students can no longer view it but the report and snapshot remain available to authorised moderators.
- Given a moderator decides an appeal, when the decision is saved, then the audit record contains the moderator identity, outcome, reason and timestamp.

### US-4 [Source: S4, S6, UR-6]

As a Student Affairs administrator,

I want the official badge limited to checked groups,

so that students can distinguish verified groups from impersonators.

Acceptance criteria:

- Given Student Affairs approves a group's verification, when a student views the group or its event, then the official badge is displayed.
- Given an unverified group copies a verified group's name or imagery, when its page is displayed, then no official badge is shown.

### US-5 [Source: S5, UR-8]

As the Data Protection Officer,

I want cancelled-event attendance records deleted on schedule,

so that CampusPulse does not retain personal data longer than necessary.

Acceptance criteria:

- Given an event was cancelled exactly 30 days ago, when the daily deletion job finishes, then no attendance record linked to that event remains.
- Given an event was cancelled fewer than 30 days ago, when the deletion job runs, then its attendance records are not deleted by the cancellation-retention rule.

## 6. MoSCoW summary

- Must: UR-1 to UR-8; FR-1 to FR-13; NFR-1 to NFR-6; US-1 to US-5.
- Should: Rate-limit substantially identical announcements from the same group while allowing authorised corrections (candidate derived from S6; threshold is Q4).
- Could: Provide officers with aggregate, non-identifying RSVP counts and provide moderators with an abuse-trend dashboard.
- Won't this release: Native mobile applications, external users, direct messages, payments, video hosting, and AI recommendations.

## 7. Traceability

| Stakeholder need | User requirement | System requirement | User story |
|---|---|---|---|
| S1: accessible followed-group feed | UR-1 | FR-2, NFR-1, NFR-2 | US-1 |
| S1/S5: private-by-default RSVP identity | UR-2 | FR-3 | US-1 |
| S2: shared drafts and approved publishing | UR-3 | FR-4, FR-5, NFR-5 | US-2 |
| S2: members-only audience control | UR-3 | FR-6 | US-2 |
| S2: tell RSVP holders about changes | UR-4 | FR-7, FR-8 | US-2 |
| S3: accountable moderation with appeal evidence | UR-5 | FR-9, FR-10, FR-11 | US-3 |
| S4/S6: trustworthy official badge | UR-6 | FR-12, NFR-5 | US-4 |
| S5: delete cancelled-event attendance data | UR-8 | FR-13, NFR-6 | US-5 |

## 8. Assumptions and open questions

### Assumptions

- A1: Until Orientation Week peak traffic is measured, performance testing will use 100 concurrent signed-in users, a 15-minute representative workload, a 2-second feed-response target, and a 95th-percentile pass threshold.
- A2: A daily retention job may finish within 24 hours after an attendance record reaches its 30-day cancellation deadline.
- A3: University sign-in supplies a stable university identifier and group membership data needed for access control without CampusPulse collecting separate credentials.

### Open questions

- Q1: What peak concurrent-user and request-rate figures should replace A1 for Orientation Week?
- Q2: What exact fields may approved officers view for a private RSVP, beyond the aggregate count needed to plan the event?
- Q3: How long must moderation evidence and appeal audit records be retained, and which fields are necessary?
- Q4: What similarity threshold and time window should trigger the repeated-announcement control without blocking legitimate corrections?
