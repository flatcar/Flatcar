# Flatcar Project Governance


Flatcar is a community based project, anyone who wants to participate is welcomed.
We adopted the [CNCF code of Conduct](./CODE_OF_CONDUCT.md) as we pledge to be an opening and welcoming community for anyone who want to participate in it.

The project is governed by a flat hierarchy - a group of people sharing a common vision of Flatcar in accordance to its mission statement.

This goverance explains how the project is run.

- [Values](#values)
- [Maintainers](#maintainers)
- [Becoming a Maintainer](#becoming-a-maintainer)
- [Meetings](#meetings)
- [CNCF Resources](#cncf-resources)
- [Code of Conduct Enforcement](#code-of-conduct)
- [Security Response Team](#security-response-team)
- [Voting](#voting)
- [Modifications](#modifying-this-charter)

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

Maintainer candidates should have demonstrated they:
- Collaborate well.
- Have a deep and comprehensive understanding of the Flatcar code base, technical goals, and directions.
- Actively engage with major Flatcar feature proposals and implementations.

The Flatcar project welcomes both development as well as community-focuses contributions.
To gain maintainership, the following is expected:
  * commitment to the project's continued success:
    * participate in discussions, contributions, code and documentation reviews for 6 months or more,
    * actively evangelise Flatcar in at least 20 talks/presentations at 10 different conferences or meetups
    * organise and chair at least 15 maintainer events, e.g. bug fixing or doc writing days, with at least 5 maintainers participating each event
  * Contribute to the project's development
    * perform reviews for 30 non-trivial pull requests,
    * contribute 10 non-trivial pull requests and have them merged,
  * ability to write quality code and/or documentation,
  * ability to collaborate with the team,
  * demonstrated understanding of how the team works (policies, processes for testing and code review, etc),
  * understanding of the project's code base and coding and / or documentation style.

Periodically, the existing maintainers curate a list of contributors that have shown regular activity on the project over the prior months.
The nominating maintainer will create a PR to update the Maintainers List.
It is recommended to describe the reasons for the nomination and the contribution of the nominee in the PR.
Upon consensus of incumbent maintainers, the PR will be approved and the new maintainer becomes active.

Maintainers who are selected will be granted the necessary GitHub rights.


### Removing a Maintainer

Life priorities, interests, and passions can change.
If you're a maintainer but feel you must remove yourself from the list, inform other maintainers that you intend to step down, and if possible, help find someone to pick up your work. 
At the very least, ensure your work can be continued where you left off.
After you've informed other maintainers, create a pull request to remove yourself from the MAINTAINERS file.

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

Time zones permitting, Maintainers are expected to participate in the Flatcar Developer Syncs meeting, which occurs every 4th Tuesday of a month at 9pm IST / 5:30pm CEST / 3:30pm GMT / 11:30am EDT / 8:30am PST

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
holes and breaches according to the [security policy](TODO:Link to security.md).

## Voting

While most business in Flatcar is conducted by "[lazy consensus](https://community.apache.org/committers/lazyConsensus.html)", 
periodically the Maintainers may need to vote on specific actions or changes.
A vote can be taken on 
[the private Maintainer mailing list](maintainers-noreply@flatcar-linux.org) for security or conduct matters.  
Votes may also be taken at [Flatcar Developer Syncs meetings](https://meet.flatcar.org/OfficeHours).  Any Maintainer may
demand a vote be taken.

Most votes require a simple majority of all Maintainers to succeed, except where
otherwise noted.  Two-thirds majority votes mean at least two-thirds of all 
existing maintainers.

## Modifying this Charter

Changes to this Governance and its supporting documents may be approved by 
a 2/3 vote of the Maintainers.
