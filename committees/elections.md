# Flatcar Committee Elections

**Status:** Adopted October 16, 2026 by a vote of the Maintainers.

* Last updated: November 2026 (https://github.com/flatcar/Flatcar/pull/2483)

This document describes how elections for the Flatcar Steering Committee and Technical
Committee work.

## Purpose

The election process should produce Steering and Technical Committees that are trusted
by the project, reflect the community, and are able to carry out the responsibilities
described in their respective charters.

## What is already decided

For an overview of both committees, see [README.md](README.md). The founding-term
rules are set out in the [Steering Committee charter](steering-committee/charter.md)
and the [Technical Committee charter](technical-committee/charter.md). Where this
document and a charter differ, the charter applies.

## Open design questions

> **Founding term note:** There is no election in the founding term. The Bootstrap
> Steering Committee and the Bootstrap Technical Committee are formed from volunteers,
> with a one-week Maintainer veto; see the "Founding term" section of each committee's
> charter. This document applies to elections from the second term onward. The founding
> mandate of each committee is to answer the open questions below for its own second
> term onward, with a first full draft published around month 9 of the 12-month term
> and a public comment period before adoption.

For each committee, the project still needs to decide the following for the second term
onward:

- How many total seats there should be: X
- Who can stand for election: X
- Who can vote: X
- Whether terms should be staggered: X
- Whether there should be term limits: X
- The company representation limit: X
- How vacancies should be filled when no runner-up is available: X

The following questions apply only to the Steering Committee:

- Whether there should be different seat types: X
- If there are different seat types, how many seats of each type: X
- What voting system should be used: X

The following questions apply only to the Technical Committee:

- The selection model (election, appointment, nomination plus vote, or another
  mechanism): X

The charters already set the following for the second term onward. Apart from
concurrent membership, the founding committees may revisit these as part of their
founding mandates:

- Term length is 2 years for both committees.
- Concurrent membership on both committees is not allowed. This rule is fixed and is
  not part of the founding mandate.

## Candidate eligibility

**Founding term (both committees):**

- Any Maintainer or recognised Contributor is automatically eligible.
- Anyone who works for, or represents, an organisation listed in
  [ADOPTERS.md](../ADOPTERS.md) is also eligible, so that users have a voice in the
  project. The Maintainers confirm the listing during the veto period.
- Other community members who contribute regularly can become eligible by first
  becoming a recognised Contributor.
- A person cannot serve on the Steering Committee and the Technical Committee at the
  same time. Serving on one committee and later standing for, or serving on, the other
  (at a different time) is allowed.

**Subsequent terms:** Candidate eligibility for each committee is X.

If the project wants different eligibility rules for different Steering Committee seat
types, those rules are X.

## Voter eligibility

**Founding term (both committees):** there is no vote in the founding term.

**Subsequent terms:** For both committees, approval of voting-rights requests moves to
the Steering Committee, matching how Istio and Kubernetes route voting exceptions
through the elected body. Voter eligibility for each committee is otherwise X.

If the project wants to recognise non-code contributions, the process for doing so is X.

## Seat allocation

**Founding term:** Neither committee has a fixed number of seats. Every eligible
person who volunteers and is not vetoed joins, within the company limits below. The
Steering Committee has no seat types.

**Subsequent terms:** The seat allocation model for each committee is X.

Possible models include:

- All seats elected the same way.
- Some seats allocated by contribution and others elected by the community.
- Some seats reserved for specific groups or perspectives.
- Some other model.

The chosen model for each committee is X.

## Election method

There is no election in the founding term. Condorcet voting, used by both Kubernetes
and Istio, handles multi-seat elections more fairly than a plain most-votes-wins
approach, since it accounts for full voter preference rather than just first choices,
and there is real precedent for running it well within CNCF projects.

For subsequent terms, the Steering Committee's voting method is part of its founding
mandate. Possible methods include Condorcet, approval voting, ranked choice, simple
majority, or another system. For the Technical Committee, the founding mandate decides
the selection model, which may or may not be an election.

The chosen method for subsequent terms is X.

## Company representation

Company representation limits are applied separately to each committee. For these
limits, a company includes its subsidiaries and affiliates.

- **Steering Committee:** no single company may hold more than 40% of the seats in the
  founding term, rounded down, with a minimum of 1 seat. The limit for later terms is
  part of the Steering Committee's founding mandate and is X.
- **Technical Committee:** no single company may have more than 4 members in the
  founding term. The limit for later terms is part of the Technical Committee's
  founding mandate and is X.

In the founding term, if more people from one company volunteer than its limit allows,
that company decides which of them join.

From the second term onward, if an election result would put a company over its limit, the lowest-ranked
candidate(s) from the over-represented company are dropped one at a time until the cap
is satisfied, and the freed seat(s) go to the next-highest-ranked eligible candidate(s)
from other companies (following Kubernetes' approach).

Where seat categories exist, the same-company limit applies to a company's total across
all categories within that committee, regardless of how those seats are split between
categories.

If a Steering Committee member changes employer mid-term in a way that breaks the
limit, they are treated as having resigned the seat, which is then filled through the
vacancies process below.

## Elections Organizing Group

Elections are run by an Elections Organizing Group (EOG) rather than by a sitting
Committee itself or a fully external group, matching Flatcar's smaller scale. The EOG
organizes elections for both the Steering Committee and the Technical Committee; see
the Technical Committee charter's "Selection model" section for how it applies there.

- **Selection:** before its term ends, each sitting Committee selects the people who
  will organize its own next election. The Steering Committee and Technical Committee
  may select the same people, forming a single shared EOG, or select different people
  for each; either is acceptable. There is no minimum or maximum group size beyond
  needing enough people to run the election.
- EOG members must be eligible voters. They may also stand as candidates. Where an EOG
  member is a candidate, an EOG member who is not standing in that race holds the voting
  tool's administrator access and confirms the count, and full results are published as
  described below.

## Election operations

Each election is run by the Elections Organizing Group (see "Elections Organizing
Group" above). Given Flatcar's smaller size, this is expected to be enough rather than
bringing in a fully external group.

The nomination period is measured in weeks rather than months, to fit Flatcar's
smaller scale (closer to Istio's timeline than Kubernetes'). It runs for two weeks,
which covers a typical holiday so nobody who wants to stand is shut out by being away,
and anyone can be nominated by someone else.

The voting period is likewise measured in weeks rather than months. It runs for two
weeks after nominations close. Candidates publish a short statement of their priorities
and goals by the time voting opens.

The method for publishing results is to publish full ranked results and vote totals,
not just the winners, consistent with the project's value of being as open as
possible. The full ranking is also used to fill vacancies (see below).

Recusal, campaigning, and EOG-member rules: campaigning must stay brand-free.
Candidates and their employers should not use company branding to campaign or drum up
votes. Sitting Steering Committee members and EOG members must step back from publicly
campaigning, nominating, or endorsing during an election, except that an EOG member who
is a candidate may campaign for themselves like any other candidate. Official election
messages stay neutral. Privately encouraging someone to run, or simply voting, is fine. There is no formal complaints process; the EOG (see
"Elections Organizing Group" above) handles any issues that arise directly.

## Vacancies and replacements

In the founding term there is no election ranking, so if a member of either committee
leaves or is removed, the seat may simply close, or the committee may invite an eligible
person to join, subject to the same one-week Maintainer veto.

From the second term onward, if a Steering Committee or Technical Committee member
leaves or is removed before the end of their term, the vacancy is filled by the
next-highest-ranked, still-eligible candidate from that seat's original election. That runner-up serves out the remainder
of the term. If no such candidate is available, the vacancy-filling process is X.

A member of either committee may be removed for sustained inactivity or for a serious
breach of the Code of Conduct. Removal requires a two-thirds supermajority vote of the
other seated members, and the member in question does not vote on their own removal. The
vacated seat is filled through the vacancy process above. See each committee's charter
for the full removal process.
