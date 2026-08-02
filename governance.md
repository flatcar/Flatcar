# Flatcar Project Governance


Flatcar is a community based project, anyone who wants to participate is welcomed.
We adopted the [CNCF code of Conduct](./CODE_OF_CONDUCT.md) as we pledge to be an opening and welcoming community for anyone who want to participate in it.

The project is governed by a flat hierarchy - a group of people sharing a common vision of Flatcar in accordance to its mission statement.

This governance explains how the project is run.

- [Flatcar Project Governance](#flatcar-project-governance)
  - [Values](#values)
  - [Maintainers](#maintainers)
    - [Becoming a Maintainer](#becoming-a-maintainer)
      - [Eligibility](#eligibility)
      - [What Is Not Required](#what-is-not-required)
      - [Routes to Maintainership](#routes-to-maintainership)
      - [Nomination and Evidence](#nomination-and-evidence)
      - [Approval](#approval)
    - [Removing a Maintainer](#removing-a-maintainer)
      - [Voluntary Step-Down](#voluntary-step-down)
      - [Inactivity](#inactivity)
      - [Removal for Cause](#removal-for-cause)
    - [Emeritus Maintainers](#emeritus-maintainers)
    - [Bookkeeping](#bookkeeping)
  - [Meetings](#meetings)
  - [CNCF Resources](#cncf-resources)
  - [Code of Conduct](#code-of-conduct)
  - [Security Response Team](#security-response-team)
  - [Voting](#voting)
  - [Modifying this Charter](#modifying-this-charter)

## Values

The Flatcar project, its leadership, and its maintainers embrace the following values:

* Openness: Communication and decision-making happens in the open and is discoverable for future
  reference. As much as possible, all discussions and work take place in public
  forums and open repositories.

* Fairness: All stakeholders have the opportunity to provide feedback and submit
  contributions, which will be considered on their merits.

* Community over Product or Company: Sustaining and growing our community takes
  priority over shipping code or sponsors' organizational goals.  Each
  contributor participates in the project as an individual.

* Inclusivity: We innovate through different perspectives and skill sets, which
  can only be accomplished in a welcoming and respectful environment.

* Participation: Responsibilities within the project are earned through
  participation, and there is a clear path up the contributor ladder into leadership
  positions.

## Maintainers

Flatcar Maintainers have full access to most of the repositories in the [Flatcar project](https://github.com/orgs/flatcar/), except for very few repositories that contain sensitive information, e.g. for with undisclosed security issues (see [SECURITY.md](./SECURITY.md) for more information).
Maintainers can merge PRs, approve PR builds+tests, and create and publish releases.
Maintainers collectively manage the project's resources, interact with contributors, elect new maintainers, and remove inactive ones.
The current list of maintainers can be found in [MAINTAINERS.md](./MAINTAINERS.md). Most maintainer access privileges are granted via membership of the Flatcar Github organisation's [Flatcar Maintainers team](https://github.com/orgs/flatcar/teams/flatcar-maintainers).

This privilege is granted with some expectation of responsibility: maintainers
are people who care about the Flatcar project and want to help it grow and
improve. A maintainer is not just someone who can make changes, but someone who
has demonstrated their ability to collaborate with the team, get the most
knowledgeable people to review code and docs, contribute high-quality code, and
follow through to fix issues (in code or tests).

A maintainer is a contributor to the project's success and a citizen helping
the project succeed.

The collective team of all Maintainers is known as the Maintainer Council, which
is the governing body for the project.

### Becoming a Maintainer

Maintainers are active community members who are responsible for the overall quality and stewardship of the project, and are expected to remain actively involved in the project and participate in voting and discussing of proposed project level changes.

Anyone with an established track record of contributions to the project can become a maintainer.
The contributions are expected to be substantial, and must demonstrate a commitment to the long-term success of the project.
Maintainership is not limited to engineering or development merits; all contributions — working with issues, providing guidance and feedback to users, reviewing PRs, contributing to docs, evangelising Flatcar — count.
Becoming a maintainer is about building trust with the current maintainers of the project and being a person that they can depend on to make decisions in the best interest of the project in a consistent manner.

People interested in becoming maintainers are encouraged to reach out to the existing maintainers well before they expect to be nominated.
Likewise, existing maintainers may approach contributors who have shown that they are ready to grow into the role.
Early conversations are encouraged so that we can help contributors understand the project, find impactful ways to contribute, and build toward maintainership deliberately.

#### Eligibility

There is no single checklist for becoming a maintainer.
Instead, a candidate must satisfy three tests, each assessed by the existing maintainers:

1. **Sustained responsibility in an area of the project.** The candidate has taken meaningful, ongoing ownership of a recognisable part of the project — whether that is a subsystem, a workflow, documentation, community support, or any other area — over a period long enough to demonstrate commitment beyond a one-off contribution.

2. **Command of the area and demonstrated judgement.** The candidate understands their area well enough to make sound decisions, knows when to seek input from others, and has shown good technical or organisational judgement across the work they have done.

3. **Trust of the current maintainers.** The existing maintainers are confident that the candidate will act in the best interest of the project, collaborate respectfully, and uphold the [Code of Conduct](./CODE_OF_CONDUCT.md).

The Flatcar project welcomes both development-focused and community-focused contributions.
Relevant contributions include, but are not limited to:

- Code, bug fixes, builds, and CI/CD improvements.
- Documentation such as guides, tutorials, and API docs.
- Community work such as issue triage and answering questions on Discord, Slack, or GitHub.
- Flatcar Apps and other reference implementations that help users learn and adopt Flatcar.
- Outreach such as blog posts, presentations, and workshops.
- Coordination work such as release management and upstream project collaboration.
- Design work such as improving the website and other project-facing materials.

#### What Is Not Required

The following are explicitly **not** requirements for maintainership:

- A minimum number of talks, conference appearances, or event participations.
- Employment or sponsorship by any particular company or organisation.
- Residence in a specific timezone or geographic region.
- Elevated access (e.g. CI admin, infrastructure credentials) prior to nomination.
- Passing through every rung of a formal contributor ladder — a contributor who meets the three tests above may be nominated directly.

#### Routes to Maintainership

There are two routes into the role, both subject to the same three eligibility tests:

- **Progression.** A contributor grows through increasing responsibility — for example moving from Contributor to Triager or Reviewer and then to Maintainer. This is the most common path and gives both the contributor and the existing maintainers time to build mutual confidence.

- **Direct nomination.** In exceptional cases, a contributor who already meets the three tests — for example an experienced upstream developer or a long-standing community leader — may be nominated directly without having held an intermediate role.

#### Nomination and Evidence

Any existing maintainer may nominate a candidate by opening a pull request against [MAINTAINERS.md](./MAINTAINERS.md) that adds the candidate to the maintainer table (including the candidate's name, GitHub handle, and organisational affiliation at the time of nomination).

The PR description must include a prose explanation of why the nominee meets the three eligibility tests, with links to relevant contributions, reviews, discussions, or other evidence.
A simple tally of merged PRs or event appearances is not sufficient; the narrative should make the case that the candidate has demonstrated sustained responsibility, sound judgement, and the trust of the maintainer team.

Self-nomination is permitted.
A self-nomination PR must be co-signed (via a GitHub review approval) by at least one existing maintainer who can attest to the candidate's eligibility.

#### Approval

A nomination PR must remain open for a minimum of **two weeks** (14 calendar days) to give all maintainers adequate time to review, ask questions, and raise concerns.

Approval is by [lazy consensus](https://community.apache.org/committers/lazyConsensus.html): the nomination is accepted if no unresolved objections remain at the end of the review period.
Any maintainer may call for a formal vote under the [Voting](#voting) rules at any point during the review period.

Objections that are person-related or otherwise sensitive must be raised on the [private maintainer mailing list](mailto:maintainers@flatcar-linux.org) rather than on the public PR.
The outcome of the nomination — whether approved or declined — is always recorded publicly on the PR.

Once approved, the new maintainer is onboarded following the [Onboarding checklist](./ONBOARDING.md) and granted the necessary access.

### Removing a Maintainer

A maintainer may leave the active roster through any of the following paths.
In every case, the [Offboarding checklist](./OFFBOARDING.md) must be completed and the [Bookkeeping](#bookkeeping) steps must be followed.

#### Voluntary Step-Down

Life priorities, interests, and passions can change.
If you are a maintainer but feel you must step down, inform the other maintainers of your intent and, if possible, help find someone to pick up your work.
At the very least, ensure your work can be continued where you left off.
After you have informed the other maintainers, create a pull request to move yourself from [MAINTAINERS.md](./MAINTAINERS.md) to [EMERITUS_MAINTAINERS.md](./EMERITUS_MAINTAINERS.md).

#### Inactivity

Inactivity is defined as a period of very low or no activity in the project for **one year or more**, with no communicated plan to return to full maintainer activity.

"Activity" is measured against the same kinds of contributions described in the [Eligibility](#eligibility) section: code contributions, reviews, issue triage, documentation, community support, release work, event organisation, and similar efforts that help the project succeed.
Simply holding the title without exercising the responsibilities it entails does not count as activity.

The Maintainer Council reviews the activity of all maintainers **once per year**, at the same time as the annual review of the [Security Response Team](#security-response-team) membership.
Before any status change is proposed, the maintainer in question must be contacted directly (via email and, if possible, a second channel) and given a reasonable opportunity to respond — at minimum **four weeks**.

If a maintainer is confirmed to be inactive and does not wish to resume activity, they are moved to emeritus status.

#### Removal for Cause

Maintainers may also be removed for failure to fulfil their maintainer responsibilities, violating the [Code of Conduct](./CODE_OF_CONDUCT.md), or other serious reasons.
A maintainer may be removed at any time by a 2/3 vote of the remaining maintainers under the [Voting](#voting) rules.

### Emeritus Maintainers

A maintainer who has stepped down or been moved to emeritus retains their name in [EMERITUS_MAINTAINERS.md](./EMERITUS_MAINTAINERS.md) as recognition of their past contributions. For removals under Removal for Cause, whether the maintainer's name is retained in EMERITUS_MAINTAINERS.md is at the discretion of the remaining maintainers involved in the removal vote.
All active access — GitHub team memberships, mailing lists, infrastructure credentials, and any other privileges described in the [Onboarding checklist](./ONBOARDING.md) — is removed when a maintainer moves to emeritus status.
The [Offboarding checklist](./OFFBOARDING.md) must be completed for every transition to emeritus.

An emeritus maintainer who wishes to return to active status may do so by resuming meaningful, sustained contributions.
They do not need to go through the full nomination process from scratch; instead, an existing maintainer opens a PR to move them back to [MAINTAINERS.md](./MAINTAINERS.md).
This PR follows the same two-week lazy-consensus approval process described in [Approval](#approval).
The returning maintainer is then re-onboarded following the [Onboarding checklist](./ONBOARDING.md).

### Bookkeeping

Every change in maintainer status — addition, move to emeritus, return from emeritus, or removal — must be reflected in all of the following:

- [MAINTAINERS.md](./MAINTAINERS.md) (including the affiliation column).
- [EMERITUS_MAINTAINERS.md](./EMERITUS_MAINTAINERS.md), where applicable.
- The [CNCF project maintainers list](https://github.com/cncf/foundation/blob/main/project-maintainers.csv).


## Meetings

Time zones permitting, Maintainers are expected to participate in the Flatcar Developer Syncs meeting every 4th Wednesday of a month.
The meeting time observes the Universal Coordinated time. It occurs at 2:30pm UTC.
Depending on your local timezone, the slot might be subject to summer time changes.
* During daylight saving time, the meeting occurs at 8pm IST (IST does not observe daylight saving time) / 4:30pm CEST / 10:30am EDT / 7:30am PST.
* Outside of daylight saving time, the meeting occurs at 8pm IST  / 3:30pm CET / 9:30am EST / 6:30am PST.

A calendar is available to ease planning. The calendar contains Developer syncs, project office hours, and one-off events like bug fixing or doc writing days.
* Google calendar link: https://calendar.google.com/calendar/u/0/embed?src=c_ii991mqrpta9en8o7ofd4v19g4@group.calendar.google.com
* iCal link (for importing): https://calendar.google.com/calendar/ical/c_ii991mqrpta9en8o7ofd4v19g4%40group.calendar.google.com/public/basic.ics

Maintainers will also have closed meetings in order to discuss security reports
or Code of Conduct violations.  Such meetings should be scheduled by any
Maintainer on receipt of a security issue or CoC report.  All current Maintainers
must be invited to such closed meetings, except for any Maintainer who is
accused of a CoC violation.

## CNCF Resources

Any Maintainer may suggest a request for CNCF resources during a
meeting.  A simple majority of Maintainers approves the request.  The Maintainers
may also choose to delegate working with the CNCF to non-Maintainer community
members, who will then be added to the [CNCF's Maintainer List](https://github.com/cncf/foundation/blob/main/project-maintainers.csv)
for that purpose.

## Code of Conduct

[Code of Conduct](./code-of-conduct.md)
violations by community members will be discussed and resolved
on the [private Maintainer mailing list](mailto:maintainers@flatcar-linux.org).  If a Maintainer is directly involved
in the report, the Maintainers will instead designate two Maintainers to work
with the CNCF Code of Conduct Committee in resolving it.

## Security Response Team

The Maintainers will appoint a Security Response Team to handle security reports.
This committee is a sub-set of the Maintainer Council with full access to undisclosed security issues tracked by the project.
Members of the Security Response team as well as respective access permissions to sensitive data are administrated via membership in the [Flatcar Github organisation's Security team](https://github.com/orgs/flatcar/teams/flatcar-security-team).
The Maintainers will review who is assigned to this at least once a year.

The Security Response Team is responsible for handling all reports of security
issues and breaches according to the [security policy](./SECURITY.md).

## Voting

While most business in Flatcar is conducted by "[lazy consensus](https://community.apache.org/committers/lazyConsensus.html)", 
periodically the Maintainers may need to vote on specific actions or changes.
A vote can be taken on 
[the private Maintainer mailing list](mailto:maintainers@flatcar-linux.org) for security or conduct matters.  
Votes may also be taken at [Flatcar Developer Syncs meetings](https://meet.flatcar.org/OfficeHours).  Any Maintainer may
demand a vote be taken.

Most votes require a simple majority of all Maintainers to succeed, except where
otherwise noted.  Two-thirds majority votes mean at least two-thirds of all 
existing maintainers.

## Modifying this Charter

Changes to this Governance and its supporting documents may be approved by 
a 2/3 vote of the Maintainers.
