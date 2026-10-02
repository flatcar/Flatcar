> **📋 PROPOSAL: this document is a governance proposal and has not been adopted.**

# Flatcar Technical Committee Charter

**Status:** DRAFT / PROPOSAL. This document is not yet adopted. Adopting it requires a
vote of the Maintainers as described in `governance.md`.

This document describes what the Flatcar Technical Committee is for, what it does, and
how it is run.

## Mission

The Technical Committee is responsible for the technical health, architecture, and
overall engineering direction of Flatcar.

It provides technical leadership, helps resolve disputes that span multiple repositories
or subgroups, and maintains technical standards across the project.

The maintainer subgroups continue to own and run their own areas day to day. The
Technical Committee exists to coordinate across those areas and decide matters that no
single subgroup should own alone.

## Scope

The Technical Committee handles technical matters that affect the project as a whole
rather than a single repository or subgroup.

## Escalations

Escalations are used to resolve technical misalignments. Any involved party may
escalate a technical matter to the Technical Committee for mediation once they judge
it is blocked and cannot be resolved between the parties or within a single subgroup
directly. Escalation does not require every party to agree that a problem exists, so a
party who is itself the source of the block cannot stop the matter being raised.

## Responsibilities

The Technical Committee is responsible for:

- Setting and defending the technical direction and architecture of the project.
- Owning and maintaining the process for technical proposals, design reviews,
  architectural decisions, or similar project-wide technical processes.
- Defining project-wide technical standards and conventions.
- Resolving technical disputes or escalations that cannot be resolved within a single
  subgroup (see [Escalations](#escalations) above).
- Coordinating technical direction across repositories, subgroups, and cross-cutting
  initiatives.
- Advising the Steering Committee on technical implications of non-technical decisions.

### Founding mandate

In addition to the responsibilities above, the founding-term Technical Committee is
specifically tasked with defining, before its term ends, the rules that will govern
the Committee and its member selection from the second term onward (these rules are
not fixed forever and may themselves be revised later (see "Changes to this
charter" below). This includes at least:

- The number of seats.
- Candidate and voter eligibility.
- The selection model (election, appointment, nomination plus vote, or otherwise).
- Term length, staggering, and term limits.
- Company representation limits, if any.
- Vacancy, removal, and Emeritus rules.
- Meeting quorum and meeting model.

To avoid this work landing in a rush at the very end of the term, the founding Committee
should publish a first full draft of these rules by roughly month 9 of the 12-month term
and open a public comment period on it. The rules should then be published as an update
to this charter, and adopted by the Maintainers per the amendment process described in
"Changes to this charter" below, before the founding term ends.

## What the Technical Committee does not do

The Technical Committee sets technical direction. It should not sit in the path of
routine engineering work.

In particular, the following should remain with the normal maintainer and subgroup
process, with no Technical Committee approval required:

- Ordinary review and merge decisions in a single area.
- Creating, renaming, archiving, or transferring repositories.
- Setting up CI, bots, tooling, and normal engineering automation.
- Routine package additions, bug fixes, refactors, and other ordinary technical work
  that already has an established owner or process.

The Technical Committee should only step in when a matter is cross-cutting,
project-wide, architectural, or explicitly escalated.

## Relationship to other bodies

### Maintainer Council

The Technical Committee operates within the authority delegated by the Maintainer
Council and the project's governance.

### Maintainer subgroups

Maintainer subgroups continue to own their own areas. The Technical Committee
coordinates across them and resolves cross-area technical questions.

### Steering Committee

The Steering Committee handles non-technical governance. The Technical Committee
handles technical governance. When a matter has both technical and non-technical
aspects, the two committees should work together.

## Membership

### Founding term

The first Technical Committee term (the "founding term") uses fixed starting
parameters so the project can bootstrap the Committee before full selection rules
exist:

- **Size:** 5 seats.
- **Length:** 1 year.
- **Candidate eligibility:** any Maintainer or recognised Contributor is automatically
  eligible to stand. Known and active community members or users are also eligible, but
  only after a vetting review run by the Maintainers (this applies to community members
  and users only, not to Maintainers or Contributors). Vetting confirms the person has
  made multiple meaningful contributions to Flatcar, technical or non-technical, in the
  previous 12 months, following the model of Istio's project-member definition. The
  review looks at the substance and recency of those contributions, not employer or
  title.
- **Concurrent membership:** a person cannot serve on the Technical Committee and the
  Steering Committee at the same time. Serving on one committee and later standing
  for, or serving on, the other (at a different time) is allowed.
- **Voter eligibility:** all Maintainers and Contributors are eligible to vote.
  Active, recognised community members or users may also vote if they request voting
  rights. For the founding election these requests are approved by the Maintainer
  Council, since the Steering Committee does not yet exist. From the second term onward,
  approval moves to the Steering Committee itself, matching how Istio and Kubernetes
  route voting exceptions through the elected body.
- **Selection model:** Condorcet voting.

One of the founding term Committee's primary responsibilities is to define the
selection rules for the Technical Committee from the second term onward (see
"Founding mandate" above). Until it does, the sections below describe only the
founding term; all values for subsequent terms are marked X pending that work.

### Size

- **Founding term:** 5 seats (see "Founding term" above).
- **Subsequent terms:** The Technical Committee has X seats, to be determined by the
  founding Technical Committee as part of the founding mandate.

### Eligibility

- **Founding term:** see "Founding term" above.
- **Subsequent terms:**

  Eligibility to stand for the Technical Committee is X.

  Eligibility to vote in Technical Committee elections or selections is X.

  Concurrent membership: as in the founding term, a person cannot serve on the
  Technical Committee and the Steering Committee at the same time. This rule is
  fixed and is not part of the founding mandate.

### Selection model

- **Founding term:** Condorcet voting (see "Founding term" above).
- **Subsequent terms:** Technical Committee members are chosen by X.

  Possible models could include election, appointment, nomination plus vote, or some
  other mechanism. The chosen model is X.

Whenever the Technical Committee is selected by election, that election is run by an
Elections Organizing Group (EOG), following the same rules as for Steering Committee
elections: see the "Elections Organizing Group" section of
`steering-committee/elections.md`. The founding EOG (Maintainer volunteers, subject to
a one-week veto window) organizes the founding Technical Committee election; before its
term ends, the sitting Technical Committee selects the people who will organize its own
next election, which may or may not be the same people the Steering Committee selects
for its election.

### Terms

- **Founding term:** 1 year.
- **Subsequent terms:** 2 years.

A member may serve for at most X consecutive terms / X consecutive years.

After reaching that limit, a member must step off the Committee for X before serving
again.

Terms may be staggered so that X seats are up each cycle, or all seats may be selected
together. The exact approach is X *(term limits and staggering for terms after the
founding term are part of the founding mandate; see "Founding mandate" above)*.

### Company representation

The project may choose to limit the number of seats held by people from the same
company.

The Technical Committee uses a deliberately loose limit: no single company may hold more
than 4 of the 5 seats. This keeps at least one independent voice on technical governance
without forcing an unrealistic spread while the contributor base is still concentrated. A
tighter limit for later terms is part of the founding mandate.

### Vacancies

If a member leaves or is removed before the end of their term, the vacancy is filled by
the next-highest-ranked, still-eligible candidate from that seat's original election,
i.e. the runner-up who did not win a seat moves in to serve out the remainder of the
term. If no such candidate is available, the vacancy-filling process is X.

### Removal

A Technical Committee member may be removed for sustained inactivity or for a serious
breach of the Code of Conduct. Removal requires a 4 of 5 supermajority vote of the other
seated members; the member in question does not vote on their own removal.

Removal is initiated by any seated member raising it with the Committee, followed by that
vote. The reason and outcome are recorded in the project's governance records, and the
vacated seat is filled through the Vacancies process above.

### Emeritus

The project may choose to recognise former Technical Committee members as Emeritus.

The meaning and privileges of Emeritus status are X.

## Decision-making

For the founding term, the Technical Committee decides by vote rather than full
consensus, so a single member cannot block progress on the founding mandate. A normal
technical decision passes by simple majority of the seats (3 of 5). A major architectural
or breaking decision, and any charter change, passes by supermajority (4 of 5). If a seat
is vacant or a member abstains, the thresholds apply to the seats actually filled and
voting.

Once the founding Committee defines a different seat count or structure for
subsequent terms (see "Founding mandate" above), it may revisit whether these
thresholds remain practical at that size. Until then:

- A normal technical decision passes by simple majority of the Committee.
- A major architectural or breaking decision passes by a 4 of 5 supermajority.
- Other special thresholds are X.

The exact voting process, including where votes happen and how long they stay open, is
X.

## Meetings

The Technical Committee meets on an as-needed basis, but must meet at least once every
2 months to sync even if there is no pressing business.

The meeting model (open, closed, or a mix) and the quorum for holding a meeting and for
taking a vote are part of the founding mandate and will be set by the founding Committee.
Until those are defined, the Committee meets and decides using the thresholds in the
Decision-making section above.

The Steering Committee and Technical Committee may hold regular joint sessions. If so,
the frequency and expectations for those sessions are X.

## Changes to this charter

The initial charter is approved by the Maintainers as a whole, since they currently hold
governance authority and are delegating some of it to the new Technical Committee. After
that, ongoing charter amendments move to the Technical Committee itself, using the
charter-change voting threshold (see the Decision-making section above) rather than
requiring a full Maintainer vote each time.

The exact process for proposing, discussing, voting on, and merging charter changes is:
a pull request against the governance document itself (so the exact change is visible,
not just described), followed by a public discussion period before any vote. Once the
Technical Committee holds this authority, the vote uses the charter-change threshold,
followed by a short waiting period before the change takes effect so anyone who missed
the discussion still sees the outcome before it goes live.
