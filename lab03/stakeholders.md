# CampusPulse stakeholder analysis

Name or team: Zayed Alahbabi

Date: 7 September 2026

Read the stakeholder notes in the lab handout before completing this file.
Use the stakeholder types and power-interest quadrants from Week 2, Lecture 2.

Stakeholder types: end user, operations, business, regulator, negative stakeholder

Power-interest quadrants: key player, keep satisfied, keep informed, minimal effort

## S1

- Stakeholder: Student attendee
- Stakeholder type: End user
- Power-interest quadrant: Keep informed - students have high interest in a useful, private and accessible service, but individually have limited decision power.
- Main goal: Find followed groups' events and announcements in one mobile-friendly browser service and RSVP without unwanted exposure.
- Main concern: An RSVP could reveal the student's identity by default, or the service could be unusable on a phone or with a screen reader.
- How you would involve or monitor this stakeholder: Recruit a diverse student panel, including screen-reader and mobile users, for prototype walkthroughs and acceptance testing; monitor opt-in public-RSVP rates and accessibility feedback during the pilot.

## S2

- Stakeholder: Group officer
- Stakeholder type: End user
- Power-interest quadrant: Key player - officers create most content and their adoption determines whether students receive useful information.
- Main goal: Collaboratively prepare announcements and events, control their audience, and notify attendees when details change.
- Main concern: An unapproved person could publish for the group, or a correction might not reach people who RSVP'd.
- How you would involve or monitor this stakeholder: Run workflow workshops with approved officers, test draft-to-publish permissions and audience controls, and review failed-publish and correction-notification reports during the pilot.

## S3

- Stakeholder: Campus moderator
- Stakeholder type: Operations
- Power-interest quadrant: Key player - moderators operate the safety process and can remove harmful content immediately.
- Main goal: Review reports, hide harmful events quickly, preserve appeal evidence, and maintain an accountable decision record.
- Main concern: Immediate hiding could destroy evidence, or moderation decisions could lack the report reason, actor, and audit history needed for an appeal.
- How you would involve or monitor this stakeholder: Co-design the report, hide, audit and appeal workflows; conduct scenario-based tests for phishing and compromised accounts; review moderation turnaround and audit completeness.

## S4

- Stakeholder: Student Affairs
- Stakeholder type: Business
- Power-interest quadrant: Key player - it sponsors the pilot, defines official verification, scale and deadline, and can stop the release.
- Main goal: Launch a trustworthy pilot for 5,000 students and 200 verified groups before Orientation Week.
- Main concern: A false official badge, insufficient capacity, or a late release would undermine trust and the pilot.
- How you would involve or monitor this stakeholder: Hold fortnightly scope and risk reviews, obtain sign-off on the verification policy, demonstrate capacity-test evidence, and report readiness against the Orientation Week deadline.

## S5

- Stakeholder: Data Protection Officer
- Stakeholder type: Regulator
- Power-interest quadrant: Keep satisfied - the officer may block non-compliant processing even though they do not use CampusPulse day to day.
- Main goal: Minimise personal-data collection, make RSVP visibility private by default, and remove cancelled-event attendance data on time.
- Main concern: The service may expose or retain personal data without necessity or informed choice.
- How you would involve or monitor this stakeholder: Complete a privacy review before launch, obtain approval for the data inventory and retention schedule, and provide monthly deletion-job and access-control audit evidence.

## S6

- Stakeholder: Abusive actor using an imitated or compromised group account
- Stakeholder type: Negative stakeholder
- Power-interest quadrant: Minimal effort - the actor is not consulted, but abuse patterns must be monitored because their actions can damage trust.
- Main goal: Impersonate a verified group, publish phishing content, or repeatedly post the same announcement.
- Main concern: Verification controls, publishing permissions, duplicate detection, reporting and moderation will prevent or quickly contain the abuse.
- How you would involve or monitor this stakeholder: Do not involve the actor directly; threat-model the two stated abuse cases, monitor repeated-post and impersonation signals, and test containment and evidence preservation through security exercises.

## Conflicts to resolve

Describe at least two real tensions. For each one, name both stakeholder IDs
and either propose a decision or write a specific question that should go back
to the stakeholders.

### Conflict 1

- Stakeholders: S1 (student attendee) and S2 (group officer)
- What conflicts: Officers may value a visible attendee list for planning and community building, while students do not want their names made public unless they choose it.
- Proposed decision or follow-up question: Make each RSVP identity private by default and allow the student to opt in to public display; officers may see only the minimum attendee data authorised for event administration.

### Conflict 2

- Stakeholders: S3 (campus moderator) and S5 (Data Protection Officer)
- What conflicts: Moderators need preserved report and event evidence for appeals, while the DPO requires data minimisation and deletion of cancelled-event attendance data within 30 days.
- Proposed decision or follow-up question: Separate moderation evidence from attendance data. Delete attendance data within 30 days of cancellation, while retaining only the report, challenged content snapshot and decision audit record under an appeal-specific retention period. Ask S3 and S5: "What is the minimum appeal-evidence retention period, and which exact fields may it contain?"

### Conflict 3

- Stakeholders: S2 (group officer) and S6 (abuse case)
- What conflicts: Multiple officers need to collaborate efficiently, but a compromised officer account could publish repeated phishing announcements.
- Proposed decision or follow-up question: Permit approved officers to edit shared drafts, require the publishing officer to be approved at publication time, label only verified groups as official, and rate-limit duplicate publication while still allowing an authorised correction.
