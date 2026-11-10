# Flatcar Steering Committee Charter

**Status:** Adopted October 16, 2026 by a vote of the Maintainers.

* Last updated: November 2026 (https://github.com/flatcar/Flatcar/pull/2483)

This document describes what the Flatcar Steering Committee is for, what it does, and
how it is run.

## Mission

The Steering Committee is responsible for the non-technical side of the Flatcar project.
It handles governance, community structure, project resources, and long-term direction.

The Steering Committee exists to serve the project and the community. It sets the
project's non-technical direction, while the Maintainer Council runs the project day to
day.

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
fixed forever and may themselves be revised later; see [Changes to this
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
this charter and to [`elections.md`](../elections.md), and adopted by the Maintainers per the
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
so the project can bootstrap the Committee before full election rules exist. During the
founding term, the Committee is called the Bootstrap Steering Committee.

- **Size:** open, with no distinction between seat types. Every eligible person who
  volunteers and is not vetoed joins, within the company representation limit below.
- **Length:** 1 year.
- **Candidate eligibility:** any Maintainer or recognised Contributor is automatically
  eligible. Known and active community members or users are also eligible if they have
  made multiple meaningful contributions to Flatcar, technical or non-technical, in the
  previous 12 months, following the model of Istio's project-member definition. The
  Maintainers check this during the veto period below, looking at the substance and
  recency of those contributions, not employer or title. Anyone who works for, or
  represents, an organisation listed in [ADOPTERS.md](../../ADOPTERS.md) is also
  eligible without the contributions check, so that users have a voice in the
  project. The Maintainers confirm the listing during the veto period.
- **Concurrent membership:** a person cannot serve on the Steering Committee and the
  Technical Committee at the same time. Serving on one committee and later standing
  for, or serving on, the other (at a different time) is allowed.
- **Selection:** there is no election in the founding term. Eligible people volunteer
  during a two-week period by commenting on a public issue in the flatcar/Flatcar
  repository; anyone who is not a Maintainer or recognised Contributor links examples of
  their contributions, or names the listed adopter they work for or represent. The list
  of volunteers is then posted, and any Maintainer may veto a volunteer within one week,
  sharing the reason with the other Maintainers. Volunteers who are not vetoed join the
  Committee when that week ends.
- **Voter eligibility:** there is no vote in the founding term. From the second term
  onward, requests for voting rights from active, recognised community members or users
  are approved by the Steering Committee itself, matching how Istio and Kubernetes route
  voting exceptions through the elected body.

One of the founding term Committee's primary responsibilities is to define the
rules for seat count, seat types, eligibility, terms, staggering, company
representation, and the voting method to be used from the second term onward (see
"Founding mandate" below). Until the founding Committee publishes
those rules, the sections below describe only the founding term; all values for
subsequent terms are marked X pending that work.

### Size

- **Founding term:** open (see "Founding term" above).
- **Subsequent terms:** The Steering Committee has X seats, to be determined by the
  founding Steering Committee as part of the founding mandate.

### Seat types

- **Founding term:** No seat types; all seats are the same.
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
company. For these limits, a company includes its subsidiaries and affiliates.

No single company may have more than 2 members on the Bootstrap Steering Committee.
From the second term onward, no single company may hold more than 1 seat. The more relaxed
founding-term limit reflects the current maintainer mix; the tighter ongoing limit keeps
the Committee genuinely multi-company once the contributor base can support it.

In the founding term, if more people from one company volunteer than the limit allows,
that company decides which of them join. From the second term onward, if an election
result would put a company over its limit, the lowest-ranked candidate(s)
from the over-represented company are dropped one at a time, and the freed seat(s) go to
the next-highest-ranked eligible candidate(s) from other companies. If a member changes
employer mid-term in a way that breaks the limit, they are treated as having resigned the
seat, which is then filled through the Vacancies process below.

### Vacancies

In the founding term there is no election ranking, so if a member leaves or is removed,
the seat may simply close, or the Committee may invite an eligible person to join,
subject to the same one-week Maintainer veto.

From the second term onward, if a member leaves or is removed before the end of their
term, the vacancy is filled by the next-highest-ranked, still-eligible candidate from
that seat's original election,
i.e. the runner-up who did not win a seat moves in to serve out the remainder of the
term. If no such candidate is available, the vacancy-filling process is X.

### Removal

A Steering Committee member may be removed for sustained inactivity or for a serious
breach of the Code of Conduct. Removal requires a two-thirds supermajority vote of the
other seated members; the member in question does not vote on their own removal.

Removal is initiated by any seated member raising it with the Committee, followed by that
vote. The reason and outcome are recorded in the project's governance records, and the
vacated seat is filled through the Vacancies process above.

### Emeritus

The project may choose to recognise former Steering Committee members as Emeritus.

The meaning and privileges of Emeritus status are X.

## Voting

For the founding term, the Steering Committee decides by vote rather than full
consensus, so a single member cannot block progress on the founding mandate. A normal
decision passes by simple majority of seated members. A charter change, and adoption of
the second-term rules produced under the founding mandate, passes by a two-thirds
supermajority of seated members. If a member abstains, the thresholds apply to the
members actually voting.

Every decision also needs yes votes from members of at least two different companies,
so no single company can decide on its own, whatever the Committee's size or who
attends.

Once the founding Committee defines a different seat count or structure for
subsequent terms (see [Founding mandate](#founding-mandate) above), it may revisit
whether these thresholds remain practical at that size. Until then:

- A normal decision passes by simple majority of the Committee.
- A charter change or founding-mandate adoption passes by a two-thirds supermajority.
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
