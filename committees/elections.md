# Flatcar Committee Elections

**Status:** Adopted October 16, 2026 by a vote of the Maintainers.

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

> **Founding term note:** For the founding term only, the seats, terms, candidate and
> voter eligibility, and voting method for both committees are already fixed; see the
> "Founding term" section of each committee's charter. The founding mandate of each
> committee is to answer the open questions below for its own second term onward, with
> a first full draft published around month 9 of the 12-month term and a public comment
> period before adoption.

For each committee, the project still needs to decide the following for the second term
onward:

- How many total seats there should be: X
- Who can stand for election: X
- Who can vote: X
- Whether terms should be staggered: X
- Whether there should be term limits: X
- How vacancies should be filled when no runner-up is available: X

The following questions apply only to the Steering Committee:

- Whether there should be different seat types: X
- If there are different seat types, how many seats of each type: X
- What voting system should be used: X

The following questions apply only to the Technical Committee:

- The selection model (election, appointment, nomination plus vote, or another
  mechanism): X
- The company representation limit: X

The charters already set the following for the second term onward. Apart from
concurrent membership, the founding committees may revisit these as part of their
founding mandates:

- Term length is 2 years for both committees.
- The Steering Committee company limit is no more than 1 seat per company.
- Concurrent membership on both committees is not allowed. This rule is fixed and is
  not part of the founding mandate.

## Candidate eligibility

**Founding term (both committees):**

- Any Maintainer or recognised Contributor is automatically eligible to stand.
- Known and active community members or users are also eligible, but only after a
  vetting review run by the Maintainers. This review applies to community members and
  users only, not to Maintainers or Contributors.
- Vetting confirms the person has made multiple meaningful contributions to Flatcar,
  technical or non-technical, in the previous 12 months, following the model of Istio's
  project-member definition. The review looks at the substance and recency of those
  contributions, not employer or title.
- A person cannot serve on the Steering Committee and the Technical Committee at the
  same time. Serving on one committee and later standing for, or serving on, the other
  (at a different time) is allowed.

**Subsequent terms:** Candidate eligibility for each committee is X.

If the project wants different eligibility rules for different Steering Committee seat
types, those rules are X.

## Voter eligibility

**Founding term (both committees):**

- All Maintainers and Contributors are eligible to vote.
- Active, recognised community members or users may also vote if they request voting
  rights. For the founding election, these requests are approved by the Maintainer
  Council, since the Steering Committee does not yet exist.

**Subsequent terms:** For both committees, approval of voting-rights requests moves to
the Steering Committee, matching how Istio and Kubernetes route voting exceptions
through the elected body. Voter eligibility for each committee is otherwise X.

If the project wants to recognise non-code contributions, the process for doing so is X.

## Seat allocation

**Founding term:** Each committee has 5 seats. The Steering Committee has no seat
types; all 5 seats are the same.

**Subsequent terms:** The seat allocation model for each committee is X.

Possible models include:

- All seats elected the same way.
- Some seats allocated by contribution and others elected by the community.
- Some seats reserved for specific groups or perspectives.
- Some other model.

The chosen model for each committee is X.

## Election method

The election method for the founding term of both committees is Condorcet voting,
matching both Kubernetes and Istio. It handles multi-seat elections more fairly than a
plain most-votes-wins approach, since it accounts for full voter preference rather than
just first choices, and there is real precedent for running it well within CNCF
projects.

For subsequent terms, the Steering Committee's voting method is part of its founding
mandate. Possible methods include Condorcet, approval voting, ranked choice, simple
majority, or another system. For the Technical Committee, the founding mandate decides
the selection model, which may or may not be an election.

The chosen method for subsequent terms is X.

## Company representation

Company representation limits are applied separately to each committee:

- **Steering Committee:** no single company may hold more than 2 of the 5 seats in the
  founding term, and no more than 1 seat from the second term onward.
- **Technical Committee:** no single company may hold more than 4 of the 5 seats in the
  founding term. A tighter limit for later terms is part of the Technical Committee's
  founding mandate and is X.

If an election result would put a company over its limit, the lowest-ranked
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

- **Founding elections:** the founding EOG is formed from Maintainers who volunteer to
  serve on it. Once a Maintainer volunteers, any other Maintainer may veto their
  inclusion within one week of the volunteer being proposed. If no veto is raised
  within that week, the volunteer joins the group. There is no minimum or maximum
  group size beyond needing enough volunteers to run the elections.
- **Subsequent elections:** before its term ends, each sitting Committee selects the
  people who will organize its own next election. The Steering Committee and Technical
  Committee may select the same people, forming a single shared EOG, or select
  different people for each; either is acceptable.
- In all cases, EOG members must be eligible voters who are not themselves candidates
  in the election they are organizing.

## Election operations

Each election is run by the Elections Organizing Group (see "Elections Organizing
Group" above). Given Flatcar's smaller size, this is expected to be enough rather than
bringing in a fully external group.

The nomination period is measured in weeks rather than months, to fit Flatcar's
smaller scale (closer to Istio's timeline than Kubernetes'). It runs for three weeks,
set longer than a typical long holiday so nobody who wants to stand is shut out by
being away.

The voting period is likewise measured in weeks rather than months. It runs for four
weeks after nominations close, which also gives candidates time to publish a short
statement of their priorities and goals before people vote.

The method for publishing results is to publish full ranked results and vote totals,
not just the winners, consistent with the project's value of being as open as
possible. The full ranking is also used to fill vacancies (see below).

Recusal, campaigning, and EOG-member rules: campaigning must stay brand-free.
Candidates and their employers should not use company branding to campaign or drum up
votes. Sitting Steering Committee members and EOG members must step back from publicly
campaigning, nominating, or endorsing during an election; privately encouraging someone
to run, or simply voting, is fine. There is no formal complaints process; the EOG (see
"Elections Organizing Group" above) handles any issues that arise directly.

## Vacancies and replacements

If a Steering Committee or Technical Committee member leaves or is removed before the
end of their term, the vacancy is filled by the next-highest-ranked, still-eligible
candidate from that seat's original election. That runner-up serves out the remainder
of the term. If no such candidate is available, the vacancy-filling process is X.

A member of either committee may be removed for sustained inactivity or for a serious
breach of the Code of Conduct. Removal requires a 4 of 5 supermajority vote of the other
seated members, and the member in question does not vote on their own removal. The
vacated seat is filled through the vacancy process above. See each committee's charter
for the full removal process.
