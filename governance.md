# Flatcar Project Governance


Flatcar is a community based project, anyone who wants to participate is welcomed.
We adopted the [CNCF code of Conduct](./CODE_OF_CONDUCT.md) as we pledge to be an opening and welcoming community for anyone who want to participate in it.

The project is governed by a flat hierarchy - a group of people sharing a common vision of Flatcar in accordance to its mission statement.

This goverance explains how the project is run.

- [Flatcar Project Governance](#flatcar-project-governance)
  - [Values](#values)
  - [Maintainers](#maintainers)
    - [Becoming a Maintainer](#becoming-a-maintainer)
    - [Removing a Maintainer](#removing-a-maintainer)
  - [Meetings](#meetings)
  - [CNCF Resources](#cncf-resources)
  - [Code of Conduct](#code-of-conduct)
  - [Security Response Team](#security-response-team)
  - [Voting](#voting)
  - [Roadmap Changes](#roadmap-changes)
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
Maintainership is not limited to engineering / development merits; all contributions - e.g. working with issues, providing guidance and feedback to users, reviewing PRs, contributing to docs, evangelising Flatcar - count.
Becoming a maintainer is about building trust with the current maintainers of the project and being a person that they can depend on to make decisions in the best interest of the project in a consistent manner.

People interested in becoming maintainers are encouraged to reach out to the existing maintainers well before they expect to be nominated.
Likewise, existing maintainers may approach contributors who have shown that they are ready to grow into the role.
Early conversations are encouraged so that we can help contributors understand the project, find impactful ways to contribute, and build toward maintainership deliberately.

There is no single checklist for becoming a maintainer.
Instead, maintainer candidates are expected to demonstrate continuous engagement with both the project and the community over time.
This includes contributing regularly in ways that help Flatcar succeed, collaborating well with others, and building trust with the existing maintainers.

The Flatcar project welcomes both development- and community-focused contributions.
Relevant contributions include, but are not limited to:

- Code, bug fixes, builds, and CI/CD improvements.
- Documentation such as guides, tutorials, and API docs.
- Community work such as issue triage and answering questions on Discord, Slack, or GitHub.
- Flatcar Apps and other reference implementations that help users learn and adopt Flatcar.
- Outreach such as blog posts, talks, presentations, and workshops.
- Coordination work such as release management and upstream project collaboration.
- Events such as bug fixing days, doc writing days, devrooms, meetups, and conferences.
- Design work such as improving the website and other project-facing materials.

Maintainer candidates should have demonstrated that they:
- Contribute continuously and in meaningful ways.
- Do work that has clear impact on the project or community.
- Collaborate well and treat others with respect, in line with the Code of Conduct.
- Develop a solid understanding of the Flatcar code base, technical goals, processes, and direction.
- Actively engage with important project discussions, reviews, and proposals.

Maintainer nominations are based on the judgment of the existing maintainers.
Periodically, the existing maintainers curate a list of contributors that have shown regular activity on the project over the prior months.
The nominating maintainer will create a PR to update the Maintainers List.
It is recommended to describe the reasons for the nomination and the contribution of the nominee in the PR.
Upon consensus of incumbent maintainers, the PR will be approved and the new maintainer becomes active.

Maintainers who are selected will be granted the necessary GitHub rights. The [CONTRIBUTING.md](./CONTRIBUTING.md) process should be used when onboarding a new maintainer.


### Removing a Maintainer

Life priorities, interests, and passions can change.
If you're a maintainer but feel you must remove yourself from the list, inform other maintainers that you intend to step down, and if possible, help find someone to pick up your work. 
At the very least, ensure your work can be continued where you left off.
After you've informed other maintainers, create a pull request to remove yourself from the [MAINTAINERS](MAINTAINERS.md) file.
If applicable, include a change to [EMERITUS_MAINTAINERS](EMERITUS_MAINTAINERS.md) to add yourself to the list of emeritus maintainers.
This will ease your return to active maintainership in the future.

Maintainers may also be removed after being inactive, failure to fulfill their 
Maintainer responsibilities, violating the Code of Conduct, or other reasons.
Inactivity is defined as a period of very low or no activity in the project 
for a year or more, with no definite schedule to return to full Maintainer 
activity.

A Maintainer may be removed at any time by a 2/3 vote of the remaining maintainers.

Depending on the reason for removal, a Maintainer may be converted to Emeritus
status.  Emeritus Maintainers will still be consulted on some project matters,
and can be rapidly returned to Maintainer status if their availability changes.


## Meetings

Time zones permitting, Maintainers are expected to participate in the Flatcar Developer Syncs meeting every 4th Wednesday of a month.
The meeting time observes the Universal Coordinated time. It occurs at 2:30pm UTC.
Depending on your local timezone, the slot might be subject to summer time changes.
* During daylight saving time, the meeting occurs at 8pm IST (IST does not observe daylight saving time) / 4:30pm CEST / 10:30am EDT / 7:30am PST.
* Outside of daylight saving time, the meeting occurs at 8pm IST  / 3:30pm CET / 9:30am EST / 6:30am PST.

A calendar is available to ease planning. The calendar contains Developer syncs, project office hours, and one-off events like bug fixing or doc writing days.
* Google calendar link: https://calendar.google.com/calendar/u/0/embed?src=c_ii991mqrpta9en8o7ofd4v19g4@group.calendar.google.com
* iCal link (for importing): https://calendar.google.com/calendar/ical/c_ii991mqrpta9en8o7ofd4v19g4%40group.calendar.google.com/public/basic.ics

Members of the community are welcome to join these meetings and are strongly encouraged to do so.
Developer Syncs are not limited to Maintainers; they are an important place for contributors and community members to follow project direction, participate in discussions, voice their opinions, and get involved in ongoing work.
Community participation in these meetings is valuable and actively encouraged, especially when contributors want to raise concerns, share feedback, or help shape the direction of the project.

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
on the [private Maintainer mailing list](maintainers@flatcar-linux.org).  If a Maintainer is directly involved
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
[the private Maintainer mailing list](maintainers@flatcar-linux.org) for security or conduct matters.  
Votes may also be taken at [Flatcar Developer Syncs meetings](https://meet.flatcar.org/OfficeHours).  Any Maintainer may
demand a vote be taken.

Most votes require a simple majority of all Maintainers to succeed, except where
otherwise noted.  Two-thirds majority votes mean at least two-thirds of all 
existing maintainers.

## Roadmap Changes

Changes to the project roadmap should be discussed openly and with enough context for contributors and Maintainers to understand the reasoning behind the proposed change.
Roadmap changes may be proposed through a GitHub issue, by a vote, or during a meeting of the Maintainers.
Using an issue is encouraged where practical, as it creates a clear public record of the proposal, the discussion around it, and the decision that follows.
In practice, roadmap changes will usually be discussed during the Flatcar Developer Syncs.
These meetings are listed on the public project calendar, and their recordings are publicly available through the meeting agendas.
When a roadmap change is made during a meeting, at least two-thirds of the Maintainers must be present for that decision.

## Modifying this Charter

Changes to this Governance and its supporting documents may be approved by 
a 2/3 vote of the Maintainers.
