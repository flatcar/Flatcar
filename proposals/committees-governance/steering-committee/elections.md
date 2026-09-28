> **📋 PROPOSAL: this document is a governance proposal and has not been adopted.**

# Flatcar Steering Committee Elections

**Status:** DRAFT / PROPOSAL. This document is not yet adopted. Adopting it requires a
vote of the Maintainers as described in `governance.md`.

This document describes how Steering Committee elections work.

## Purpose

The election process should produce a Steering Committee that is trusted by the project,
reflects the community, and is able to carry out the responsibilities described in the
Steering Committee charter.

## Open design questions

> **Founding term note:** For the founding term only, seats (5, no seat types),
> terms (1 year), candidate/voter eligibility, and voting method (Condorcet) are
> already fixed; see the "Founding term" section of `steering-committee.md`. The
> founding Steering Committee's founding mandate is to answer the open questions below
> for the second term onward.

The project still needs to decide the following:

- How many total seats there should be: X
- Whether there should be different seat types: X
- If there are different seat types, how many seats of each type: X
- Who can stand for election: X
- Who can vote: X
- How long terms should be: X *(the founding term is fixed at 1 year; this question
  applies to terms from the second term onward, expected to be 2 years)*
- Whether terms should be staggered: X
- Whether there should be term limits: X
- Whether there should be company representation limits: X
- What voting system should be used: X
- How vacancies should be filled: X

## Candidate eligibility

Candidate eligibility is X.

If the project wants different eligibility rules for different seat types, those rules
are X.

## Voter eligibility

Voter eligibility is X.

If the project wants to recognise non-code contributions, the process for doing so is X.

## Seat allocation

The Steering Committee seat allocation model is X.

Possible models include:

- All seats elected the same way.
- Some seats allocated by contribution and others elected by the community.
- Some seats reserved for specific groups or perspectives.
- Some other model.

The chosen model is X.

## Election method

The election method is Condorcet voting, matching both Kubernetes and Istio. It
handles multi-seat elections more fairly than a plain most-votes-wins approach, since
it accounts for full voter preference rather than just first choices, and there is
real precedent for running it well within CNCF projects.

Possible methods include Condorcet, approval voting, ranked choice, simple majority, or
another system.

The chosen method is Condorcet.

## Company representation

If the project adopts limits on same-company representation, the exact rules are: the
lowest-ranked candidate(s) from an over-represented company are dropped one at a time
until the cap is satisfied, with the freed seat(s) going to the next-highest-ranked
candidate(s) from other companies (following Kubernetes' approach).

Where seat categories exist, the same-company limit applies to a company's total across
all categories: a company's combined seats may not exceed the cap set in the Company
representation section, regardless of how those seats are split between categories.

## Election operations

The election is run by 1–2 dedicated election officers: eligible voters who are not
themselves candidates in that election. Given Flatcar's smaller size, this is expected
to be enough, rather than having the sitting Committee run its own election or
bringing in a fully external group.

The nomination period is measured in weeks rather than months, to fit Flatcar's
smaller scale (closer to Istio's timeline than Kubernetes'). It runs for three weeks, set
longer than a typical long holiday so nobody who wants to stand is shut out by being
away.

The voting period is likewise measured in weeks rather than months. It runs for four
weeks after nominations close, which also gives candidates time to publish a short
statement of their priorities and goals before people vote.

The method for publishing results is to publish full ranked results and vote totals,
not just the winners, consistent with the project's value of being as open as
possible.

Recusal, campaigning, and election-officer rules: campaigning must stay brand-free:
candidates and their employers should not use company branding to campaign or drum up
votes. Sitting Steering Committee members and election officers must step back from
publicly campaigning, nominating, or endorsing during an election; privately
encouraging someone to run, or simply voting, is fine. There is no formal complaints
process; the election officers (see above) handle any issues that arise directly.

## Vacancies and replacements

If an elected member cannot serve or leaves early, the replacement process is X.
