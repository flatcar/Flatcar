> **📋 PROPOSAL: this document is a governance proposal and has not been adopted.**

# Flatcar Steering Committee Charter

**Status:** DRAFT / PROPOSAL. This document is not yet adopted. Adopting it requires a
vote of the Maintainers as described in `governance.md`.

This document describes what the Flatcar Steering Committee is for, what it does, and
how it is run.

## Mission

The Steering Committee is responsible for the non-technical side of the Flatcar project.
It handles governance, community structure, project resources, and long-term direction.

The Steering Committee exists to serve the project and the community. It does not
replace the Maintainer Council, which remains the main governing body of the project.

## How it works

- The Committee can adapt its own role and structure as the project's needs change.
- Anything not explicitly delegated to another group stays with the Steering Committee.
- Technical decisions are delegated to the Technical Committee and the relevant
  maintainer subgroups.
- Day-to-day running of the project stays with the Maintainer Council and its subgroups.

## What the Steering Committee does not do

The Steering Committee sets direction and policy. It does not micromanage the project.

In particular, the following should continue to happen through the normal maintainer and
subgroup process, with no Steering Committee approval required:

- Creating, renaming, archiving, or transferring repositories in the `flatcar` GitHub
  organisation.
- Granting or adjusting normal project access for maintainers, contributors, and
  subgroups.
- Running CI, automation, bots, and tooling needed for normal project work.
- Running releases, triaging issues, reviewing pull requests, and other routine
  maintenance work.

The Steering Committee should only step in when a matter is project-wide,
non-technical, or explicitly escalated to it.

### Escalations

Escalations are used to resolve misalignments. Any involved party may escalate a matter
to the Steering Committee for mediation once they judge it is blocked and cannot be
resolved between the parties directly. Escalation does not require every party to agree
that a problem exists, so a party who is itself the source of the block cannot stop the
matter being raised.

## Responsibilities

The Steering Committee is responsible for:

- Setting and defending the non-technical vision, mission, and values of the project.
- Defining and evolving the project's governance structure.
- Creating and approving charters for project-wide groups such as committees, working
  groups, and subgroups.
- Acting as the final escalation point for non-technical disputes in the project (see
  [Escalations](#escalations) above).
- Managing the project's relationship with the CNCF and other outside bodies.
- Advising on trademark, branding, advocacy, and other non-technical project matters.
- Holding and delegating authority over project-wide assets such as GitHub organisation
  ownership, websites, domains, mailing lists, social-media accounts, and similar
  resources.
- Defining what it means for a project group to be in good standing and enforcing those
  expectations.

### Founding mandate

In addition to the responsibilities above, the founding-term Steering Committee is
specifically tasked with defining, before its term ends, the rules that will govern
the Committee and its elections from the second term onward (these rules are not
fixed forever and may themselves be revised later (see [Changes to this
charter](#changes-to-this-charter)). This includes at least:

- The number and type of seats.
- Candidate and voter eligibility.
- Term length, staggering, and term limits.
- Company representation limits, if any.
- The voting method and voting/election process, including thresholds for decisions
  and charter changes.
- Vacancy, removal, and Emeritus rules.
- Meeting quorum and meeting model.

To avoid this work landing in a rush at the very end of the term, the founding Committee
should publish a first full draft of these rules by roughly month 9 of the 12-month term
and open a public comment period on it. The rules should then be published as updates to
this charter and to `steering-elections.md`, and adopted by the Maintainers per the
amendment process described in [Changes to this charter](#changes-to-this-charter),
before the founding term ends.

## Working with the Technical Committee

Technical direction, architecture, and cross-cutting engineering decisions are handled
by the Technical Committee.

The Steering Committee does not overrule technical decisions. When a matter has both
technical and non-technical aspects, the Steering Committee and Technical Committee are
expected to work together, each deciding the parts that fall under their own remit.

## Membership

### Founding term

The first Steering Committee term (the "founding term") uses fixed starting parameters
so the project can bootstrap the Committee before full election rules exist:

- **Size:** 5 seats, with no distinction between seat types.
- **Length:** 1 year.
- **Candidate eligibility:** any Maintainer or recognised Contributor is automatically
  eligible to stand. Known and active community members or users are also eligible, but
  only after a vetting review run by the Maintainers (this applies to community members
  and users only, not to Maintainers or Contributors). Vetting confirms the person has
  made multiple meaningful contributions to Flatcar, technical or non-technical, in the
  previous 12 months, following the model of Istio's project-member definition. The
  review looks at the substance and recency of those contributions, not employer or
  title.
- **Concurrent membership:** a person cannot serve on the Steering Committee and the
  Technical Committee at the same time. Serving on one committee and later standing
  for, or serving on, the other (at a different time) is allowed.
- **Voter eligibility:** all Maintainers and Contributors are eligible to vote.
  Active, recognised community members or users may also vote if they request voting
  rights. For the founding election these requests are approved by the Maintainer
  Council, since the Steering Committee does not yet exist. From the second term onward,
  approval moves to the Steering Committee itself, matching how Istio and Kubernetes
  route voting exceptions through the elected body.
- **Voting method:** Condorcet voting.

One of the founding term Committee's primary responsibilities is to define the
rules for seat count, seat types, eligibility, terms, staggering, company
representation, and the voting method to be used from the second term onward (see
"Founding mandate" below). Until the founding Committee publishes
those rules, the sections below describe only the founding term; all values for
subsequent terms are marked X pending that work.

### Size

- **Founding term:** 5 seats (see "Founding term" above).
- **Subsequent terms:** The Steering Committee has X seats, to be determined by the
  founding Steering Committee as part of the founding mandate.

### Seat types

- **Founding term:** No seat types; all 5 seats are the same.
- **Subsequent terms:** The Steering Committee may include one or more categories of
  seats, such as:

  - **Contributor seats:** held by people selected based on project contribution.
  - **Community seats:** held by people selected to represent the broader community.
  - **Other seat categories** as the project may choose to define.

  The exact number and type of seats is X.

### Eligibility

- **Founding term:** see "Founding term" above.
- **Subsequent terms:**

  Eligibility to stand for the Steering Committee is X.

  Eligibility to vote in Steering Committee elections is X.

  Concurrent membership: as in the founding term, a person cannot serve on the
  Steering Committee and the Technical Committee at the same time. This rule is
  fixed and is not part of the founding mandate.

### Terms

- **Founding term:** 1 year.
- **Subsequent terms:** 2 years.

A member may serve for at most X consecutive terms / X consecutive years.

After reaching that limit, a member must step off the Committee for X before serving
again.

Terms may be staggered so that X seats are up each cycle, or all seats may be elected
together. The exact approach is X *(term limits and staggering for terms after the
founding term are part of the founding mandate; see "Founding mandate"
above)*.

### Company representation

The project may choose to limit the number of seats held by people from the same
company.

No single company may hold more than 2 of the 5 seats on the founding Steering
Committee. From the second term onward, no single company may hold more than 1 seat. The
looser founding-term limit reflects the current maintainer mix; the tighter ongoing
limit keeps the Committee genuinely multi-company once the contributor base can support
it.

If an election result would put a company over its limit, the lowest-ranked candidate(s)
from the over-represented company are dropped one at a time, and the freed seat(s) go to
the next-highest-ranked eligible candidate(s) from other companies. If a member changes
employer mid-term in a way that breaks the limit, they are treated as having resigned the
seat, which is then filled through the Vacancies process below.

### Vacancies

If a member leaves or is removed before the end of their term, the vacancy is filled by
the next-highest-ranked, still-eligible candidate from that seat's original election,
i.e. the runner-up who did not win a seat moves in to serve out the remainder of the
term. If no such candidate is available, the vacancy-filling process is X.

### Removal

A Steering Committee member may be removed for sustained inactivity or for a serious
breach of the Code of Conduct. Removal requires a 4 of 5 supermajority vote of the other
seated members; the member in question does not vote on their own removal.

Removal is initiated by any seated member raising it with the Committee, followed by that
vote. The reason and outcome are recorded in the project's governance records, and the
vacated seat is filled through the Vacancies process above.

### Emeritus

The project may choose to recognise former Steering Committee members as Emeritus.

The meaning and privileges of Emeritus status are X.

## Voting

For the founding term, the Steering Committee decides by vote rather than full
consensus, so a single member cannot block progress on the founding mandate. A normal
decision passes by simple majority of the seats (3 of 5). A charter change, and adoption
of the second-term rules produced under the founding mandate, passes by supermajority
(4 of 5). If a seat is vacant or a member abstains, the thresholds apply to the seats
actually filled and voting.

Once the founding Committee defines a different seat count or structure for
subsequent terms (see [Founding mandate](#founding-mandate) above), it may revisit
whether these thresholds remain practical at that size. Until then:

- A normal decision passes by simple majority of the Committee.
- A charter change or founding-mandate adoption passes by a 4 of 5 supermajority.
- Other special thresholds are X.

The exact voting process, including where votes happen and how long they stay open, is
X.

## Meetings

The Steering Committee meets on an as-needed basis, but must meet at least once every
2 months to sync even if there is no pressing business.

The meeting model (open, closed, or a mix) and the quorum for holding a meeting and for
taking a vote are part of the founding mandate and will be set by the founding Committee.
Until those are defined, the Committee meets and decides using the thresholds in the
Voting section above.

The Steering Committee and Technical Committee may hold regular joint sessions. If so,
the frequency and expectations for those sessions are X.

## Changes to this charter

The initial charter is approved by the Maintainers as a whole, since they currently
hold governance authority and are delegating some of it to the new Steering
Committee. After that, ongoing charter amendments move to the Steering Committee
itself, using the charter-change voting threshold (see [Voting](#voting) above)
rather than requiring a full Maintainer vote each time.

The exact process for proposing, discussing, voting on, and merging charter changes is:
a pull request against the governance document itself (so the exact change is
visible, not just described), followed by a public discussion period before any vote.
Once the Steering Committee holds this authority, the vote uses the charter-change
threshold, followed by a short waiting period before the change takes effect so
anyone who missed the discussion still sees the outcome before it goes live.
