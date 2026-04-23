# Maintainer Onboarding Checklist

Welcome to the Flatcar maintainer team! 🎉

This document is a **template** for onboarding new Flatcar maintainers.

> **How to use this template:**
> Copy the raw Markdown contents of this file and paste them into a new GitHub issue (e.g. titled _"Onboarding: \<new maintainer's name\>"_). Track progress and tick off checklist items in that issue — do **not** edit the checkboxes in this file. This document remains the canonical template for all future onboardings.
>
> **Improving this template:**
> If you find that this document does not reflect the realities of onboarding (missing steps, outdated information, etc.), please open a pull request to update it.

The checklist is split into two parts:

- **[For the onboarding coordinator](#for-the-onboarding-coordinator)** — actions that an existing maintainer or project coordinator must perform on behalf of the new maintainer.
- **[For the new maintainer](#for-the-new-maintainer)** — actions the new maintainer should complete themselves.

Once onboarding is complete, both parties should confirm each item is ticked off in the tracking issue.

---

## For the Onboarding Coordinator

These steps require elevated access and must be completed by an existing maintainer or project coordinator.

### GitHub Access

- [ ] Add the new maintainer to the [flatcar-maintainers](https://github.com/orgs/flatcar/teams/flatcar-maintainers) GitHub team.
- [ ] Verify the new maintainer has appropriate permissions on all relevant repositories (see [MAINTAINERS.md](./MAINTAINERS.md) for the list of repositories).
- [ ] Assign the new maintainer to the relevant PR review groups based on their area of focus, for example:
  - `flatcar-ci`
  - `nebraska-maintainers`
  - Other repository-specific teams as applicable.
- [ ] If the new maintainer will be involved in release management, add them to the Nebraska read-only (`ro`) or read-write (`rw`) groups in the Nebraska release process as appropriate. See [RELEASES.md](./RELEASES.md) for the full release guide.

### CNCF Registration

- [ ] Add the new maintainer to the [CNCF project maintainers list](https://github.com/cncf/foundation/blob/main/project-maintainers.csv) by opening a pull request against the [cncf/foundation](https://github.com/cncf/foundation/) repository (see [example PR](https://github.com/cncf/foundation/pull/1075)).
- [ ] Ensure the new maintainer has access to CNCF accounts and services used by the project (e.g. CNCF service desk, CNCF Slack).

### Mailing Lists

Add the new maintainer to the following mailing lists:

**Private lists** (maintainer-only):
- [ ] `maintainers@flatcar-linux.org` — maintainer coordination and voting
- [ ] Infra mailing list — infrastructure and operational discussions
- [ ] Security mailing list — undisclosed security issue handling

**Public lists** (community-facing):
- [ ] [Flatcar Users](https://groups.google.com/g/flatcar-linux-user)

### Infrastructure Access

Grant the new maintainer access to the following infrastructure systems (at minimum read/user level; escalate as required by their role):

- [ ] Jenkins (CI)

### Communication and Collaboration Tools

- [ ] Grant access to the shared Flatcar events Google Calendar.
- [ ] Grant access to the Flatcar YouTube channel.
- [ ] Grant access to the [HackMD](https://hackmd.io) workspace used for collaborative documents.

### Linux Foundation

- [ ] Ensure the new maintainer has a Linux Foundation account.
- [ ] Grant access to the Linux Foundation Jira project used for tracking Flatcar work items.

---

## For the New Maintainer

These are steps you should complete yourself after your coordinator has provisioned your access.

### GitHub

- [ ] Accept the invitation to the [flatcar GitHub organisation](https://github.com/flatcar) and the `flatcar-maintainers` team.
- [ ] Review the list of repositories you have been added to and familiarise yourself with their purpose (see [MAINTAINERS.md](./MAINTAINERS.md)).
- [ ] Review the [Governance document](./governance.md) to understand the project's decision-making process, voting, and maintainer responsibilities.

### Calendar and Meetings

- [ ] Add the Flatcar community calendar to your calendar app using the iCal link:
  `https://calendar.google.com/calendar/ical/c_ii991mqrpta9en8o7ofd4v19g4%40group.calendar.google.com/public/basic.ics`
- [ ] Alternatively, subscribe via the [Google Calendar link](https://calendar.google.com/calendar/u/0/embed?src=c_ii991mqrpta9en8o7ofd4v19g4@group.calendar.google.com).
- [ ] Attend your first [Flatcar Developer Sync](https://meet.flatcar.org/OfficeHours) — check the community calendar for the current schedule.
- [ ] Attend your first [Flatcar Office Hours](https://meet.flatcar.org/OfficeHours) — check the community calendar for the current schedule.

### Mailing Lists

- [ ] Confirm you have been added to the private maintainer, infra, and security mailing lists and that you can send and receive messages.
- [ ] Confirm you have been subscribed to the [Flatcar Users](https://groups.google.com/g/flatcar-linux-user) public mailing list.

### Community Channels

- [ ] Join the Flatcar Discord server: [discord.gg/PMYjFUsJyq](https://discord.gg/PMYjFUsJyq)
- [ ] Join the Flatcar Matrix room: [#flatcar:matrix.org](https://app.element.io/#/room/#flatcar:matrix.org)
- [ ] Join the [#flatcar channel](https://kubernetes.slack.com/archives/C03GQ8B5XNJ) in the Kubernetes Slack workspace.

### Infrastructure and Tooling

- [ ] Verify your access to Jenkins
- [ ] Log in to HackMD and confirm access to shared Flatcar documents.
- [ ] Log in to the Linux Foundation Jira and confirm access to the Flatcar project board.
- [ ] Verify CNCF account access.

### Knowledge Sharing

- [ ] Schedule onboarding knowledge-sharing sessions with existing maintainers to cover key areas of the project. Suggested topics include:
  - Overview of the Flatcar build system and SDK
  - CI/CD pipeline and infrastructure
  - Release management process (see [RELEASES.md](./RELEASES.md))
  - Security response process
  - Governance and decision-making
- [ ] Read through the [Flatcar developer guides](https://www.flatcar.org/docs/latest/reference/developer-guides/) and the [SDK how-to](https://www.flatcar.org/docs/latest/reference/developer-guides/sdk-modifying-flatcar/).
- [ ] Review the [CONTRIBUTING.md](./CONTRIBUTING.md) guide.
- [ ] Review the [SECURITY.md](./SECURITY.md) policy.
- [ ] Review the [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

---

## Questions and Support

If you have any questions during onboarding, please reach out to the maintainer team via:

- Discord: [discord.gg/PMYjFUsJyq](https://discord.gg/PMYjFUsJyq)
- Matrix: [#flatcar:matrix.org](https://app.element.io/#/room/#flatcar:matrix.org)
- Slack: [#flatcar](https://kubernetes.slack.com/archives/C03GQ8B5XNJ) in the Kubernetes Slack org
- Private maintainer mailing list: `maintainers@flatcar-linux.org`
