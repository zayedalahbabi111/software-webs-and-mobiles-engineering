# CampusPulse requirements review

Name or team: Zayed Alahbabi

Reviewer: Zayed Alahbabi (self-review against S1-S6)

Date: 7 September 2026

Review the completed `stakeholders.md` and `REQUIREMENTS.md`. Refer to specific
IDs and evidence in every answer. A yes or no by itself is not enough.

## Validity

Response: The specification represents each supplied source rather than treating meeting notes as ready-made requirements. S1 maps to the followed-group feed and accessibility in UR-1, FR-2 and NFR-1/NFR-2, and to RSVP privacy in UR-2 and FR-3. S2 maps to shared drafts, approved publication, audience control and change notification in UR-3/UR-4 and FR-4 to FR-8. S3's report, immediate hide, evidence and accountable decision needs map to UR-5 and FR-9 to FR-11. S4's verified badge and stated pilot scale map to UR-6/UR-7, FR-12 and NFR-3. S5 maps to private defaults and deletion in UR-2/UR-8, FR-3/FR-13 and NFR-6. S6's impersonation case is addressed by FR-12 and US-4; repeated posts remain a prioritised Should item with its unknown threshold recorded as Q4 rather than invented as stakeholder evidence.

## Consistency

Response: The scope and MoSCoW Won't list both exclude the same six capabilities: native mobile apps, external users, direct messages, payments, video hosting and AI recommendations. Browser responsiveness in NFR-2 therefore does not imply a native app. FR-3's private RSVP default agrees with UR-2 and the S1/S5 conflict decision. FR-10 hides content without deleting evidence, while FR-13 deletes attendance data after cancellation; these do not conflict because the S3/S5 decision separates appeal evidence from attendance records. Every FR and NFR cites an existing UR, and all cited IDs appear in Section 2.

## Completeness

Response: The normal flows cover sign-in, following/feed display, private RSVP, shared drafting, publication, audiences, changes, reporting, moderation, official verification and retention. Permission and failure boundaries are explicit in FR-5, FR-6, FR-10, FR-12, NFR-5, US-2 and US-4. Privacy is addressed by FR-3 and FR-13. The product boundary is explicit in Sections 1 and 6. Two deliberate gaps remain visible instead of being hidden: the brief supplies no Orientation Week peak traffic figure (Q1), and S6 supplies no defensible duplicate threshold (Q4). External users are not a missing actor because they are explicitly out of scope.

## Realism

Response: A browser-only first release for 5,000 students and 200 groups is more realistic than adding the six excluded capabilities. NFR-3 uses S4's supplied scale exactly. The 100-user concurrency, 2-second response target and 15-minute load-test condition in NFR-4 are explicitly labelled assumption A1 because the brief provides no peak traffic. NFR-6's 24-hour job tolerance is likewise labelled A2. The official-badge workflow depends on Student Affairs approval (FR-12), while university identity and membership data availability is recorded as A3. Q1-Q4 identify evidence still needed before these assumptions become agreed baselines.

## Verifiability

Response: Each FR describes observable behaviour, and each NFR identifies a target, measure and condition. A tester can verify FR-3 by checking that a default RSVP name is absent publicly, FR-5/FR-6 through negative permission tests, FR-8 using a five-minute timer, FR-10 by confirming hidden public content and retained evidence, and FR-13/NFR-6 by inspecting due retention records. The acceptance criteria use Given/When/Then-style conditions with visible pass/fail outcomes. During review, the earlier wording of FR-8 used "promptly," which was not objectively testable; it was replaced with the five-minute assumed target documented below and in A4.

## One requirement you revised

- Requirement ID: FR-8
- Before: FR-8 [Must] The system shall promptly notify every current RSVP holder when an event's place or time changes or when the event is cancelled. [Source: UR-4]
- What was wrong or missing: "Promptly" had no measurable deadline, so different developers and testers could interpret it differently and no acceptance test had an objective pass/fail boundary.
- After: FR-8 [Must] The system shall notify every current RSVP holder of an event place, time or cancellation change within 5 minutes of the saved change. [Source: UR-4]
- Evidence or stakeholder to confirm the change: S2 confirms who must be notified and which changes matter; the five-minute target is an explicit team assumption pending confirmation from group officers. The revised FR-8 appears in REQUIREMENTS.md, the S2/UR-4 traceability row, and US-2's third acceptance criterion.

## Final check

- [x] Stakeholder conflicts have a decision or a follow-up question.
- [x] Scope exclusions agree with the Won't list.
- [x] Every FR and NFR traces to a user requirement.
- [x] Every NFR contains a measurable target and condition.
- [x] Traceability rows use IDs that exist in the document.
- [x] The revised requirement has also been updated in the traceability table.
