# Maintainer Offboarding Checklist

This document is a **template** for offboarding Flatcar maintainers who are stepping down, moving to emeritus status, or being removed.

> **How to use this template:**
> Copy the raw Markdown contents of this file and paste them into a new GitHub issue (e.g. titled _"Offboarding: \<maintainer's name\>"_). Track progress and tick off checklist items in that issue — do **not** edit the checkboxes in this file. This document remains the canonical template for all future offboardings.
>
> **Improving this template:**
> If you find that this document does not reflect the realities of offboarding (missing steps, outdated information, etc.), please open a pull request to update it.
>
> **One-time access audit (follow-up required):**
> When this checklist is first adopted, an audit should be performed to verify that all currently listed access grants match the current maintainer roster. This requires administrative access to the relevant systems and must be carried out by an existing maintainer or project coordinator — it cannot be automated or performed without elevated privileges.

The checklist is split into two parts:

- **[For the offboarding coordinator](#for-the-offboarding-coordinator)** — actions that an existing maintainer or project coordinator must perform to revoke the departing maintainer's access.
- **[For the departing maintainer](#for-the-departing-maintainer)** — actions the departing maintainer should complete themselves, if able.

---

## Exit Cases

This checklist applies to all three exit scenarios:

- **Voluntary step-down** — the maintainer chooses to leave the active roster.
- **Move to emeritus** — the maintainer is moved to emeritus status due to inactivity or by choice.
- **Removal** — the maintainer is removed by a 2/3 vote of the remaining maintainers.

In every case, the [Bookkeeping](./governance.md#bookkeeping) steps described in the governance document must also be completed.

---

## For the Offboarding Coordinator

These steps require elevated access and must be completed by an existing maintainer or project coordinator.

### GitHub Access

- [ ] Remove the departing maintainer from the [flatcar-maintainers](https://github.com/orgs/flatcar/teams/flatcar-maintainers) GitHub team.
- [ ] Remove the departing maintainer from all repository-specific review teams they were a member of, for example:
  - `flatcar-ci`
  - `nebraska-maintainers`
  - `flatcar-integrations`
  - `flatcar-communication`
  - `flatcar-infra`
  - Other repository-specific teams as applicable.
- [ ] If the departing maintainer had Nebraska read-only (`ro`) or read-write (`rw`) group access, remove them from those groups.
- [ ] Review `CODEOWNERS` files in repositories where the departing maintainer was explicitly listed, and update as needed.

### CNCF Registration

- [ ] Remove the departing maintainer from the [CNCF project maintainers list](https://github.com/cncf/foundation/blob/main/project-maintainers.csv) by opening a pull request against the [cncf/foundation](https://github.com/cncf/foundation/) repository.
- [ ] Revoke any CNCF account access or services the departing maintainer had (e.g. CNCF service desk, CNCF Slack roles).

### Mailing Lists

Remove the departing maintainer from the following mailing lists:

**Private lists** (maintainer-only):
- [ ] `maintainers@flatcar-linux.org` — maintainer coordination and voting
- [ ] Infra mailing list — infrastructure and operational discussions
- [ ] Security mailing list — undisclosed security issue handling

**Public lists** (optional — the departing maintainer may choose to remain):
- [ ] [Flatcar Users](https://groups.google.com/g/flatcar-linux-user) — confirm with the departing maintainer whether they wish to remain subscribed.

### Infrastructure Access

Revoke the departing maintainer's access to the following infrastructure systems:

- [ ] Jenkins (CI)

### Communication and Collaboration Tools

- [ ] Revoke access to the shared Flatcar events Google Calendar (or downgrade to viewer if appropriate).
- [ ] Revoke access to the Flatcar YouTube channel (or downgrade to viewer if appropriate).
- [ ] Revoke access to the [HackMD](https://hackmd.io) workspace used for collaborative documents.

### Linux Foundation

- [ ] Remove the departing maintainer's access to the Linux Foundation Jira project.
- [ ] Note: The departing maintainer's Linux Foundation account itself is their own — it does not need to be removed, only project-specific access.

### Governance Records

- [ ] Update [MAINTAINERS.md](./MAINTAINERS.md) to remove the departing maintainer.
- [ ] Update [EMERITUS_MAINTAINERS.md](./EMERITUS_MAINTAINERS.md) to add the departing maintainer (for voluntary step-down and emeritus transitions; not applicable for removal due to Code of Conduct violations, at the discretion of the remaining maintainers).

---

## For the Departing Maintainer

If possible, please complete these steps yourself before or during the transition.

### Knowledge Transfer

- [ ] Identify any areas of the project where you are the primary or sole point of contact and flag them to the maintainer team.
- [ ] Document or hand off any in-progress work, including open PRs, issues you are shepherding, and ongoing initiatives.
- [ ] If you hold any role-specific knowledge (e.g. release process details, infrastructure access specifics), ensure it is documented or shared with another maintainer.

### Access and Accounts

- [ ] Confirm that your access to the following has been revoked (or request revocation if it has not been):
  - [flatcar-maintainers](https://github.com/orgs/flatcar/teams/flatcar-maintainers) GitHub team
  - Repository-specific review teams
  - Private mailing lists (maintainers, infra, security)
  - Jenkins
  - Shared Google Calendar
  - YouTube channel
  - HackMD workspace
  - Linux Foundation Jira project access
  - CNCF project maintainers list

### Community Channels

- [ ] Note: Membership in community channels (Discord, Kubernetes Slack #flatcar) is **not** revoked — departing maintainers are welcome to continue participating as community members.

---

## Questions and Support

If you have any questions during offboarding, please reach out to the maintainer team via:

- Discord: [discord.gg/PMYjFUsJyq](https://discord.gg/PMYjFUsJyq)
- Slack: [#flatcar](https://kubernetes.slack.com/archives/C03GQ8B5XNJ) in the Kubernetes Slack org
- Private maintainer mailing list: `maintainers@flatcar-linux.org`
