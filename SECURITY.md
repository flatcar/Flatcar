# Flatcar Security 
To keep Flatcar secure, the maintainers put a strong focus on tracking new and existing security issues.
Dealing with Security concerns is owned by the [Flatcar Security team](https://github.com/orgs/flatcar/teams/flatcar-security-team), a sub-set of the Maintainers team, and elected by the Maintainers (see [governance.md](./governance.md)).

While the team actively researches and tracks new and existing security issues, it may also be notified of issues via [security@flatcar-linux.org](mailto:security@flatcar-linux.org).

The Security team meets in a fortnightly cadence, in a private video call.
The team maintains an internal list of security Primaries and Secondaries, which are rotated on a weekly basis. 
Primary and Secondary are expected to actively engage in security work each day, including executing the Runbook (see below) and working on fixing ongoing security issues.

Undisclosed security issues are tracked in a private repository only accessible by members of the security team.
Public issues are tracked publicly in the project's main issue tracker.

Security issues are addressed by releasing an updated OS image. Releases may be expedited depending on the issues' severity. For each release, release notes contain a concise list of security issues fixed. Also, a separate, detailed report on each of the issues addressed is part of every release.

## Daily security runbook for Security team primaries and secondaries

The runbook below discusses steps for identifying new potential security issues and for making the issues known to the Flatcar project's maintainers and / or the other members of the Security team.

Primaries are expected to execute the runbook at least once per day, optionally assisted or off-loaded by Secondaries.

Every day look into upstream security trackers like below:
- Gentoo security vulnerabilities. It might be useful to use gorss + RSS feed for this.
- oss-security mailing list
- Golang announce mailing list
- Rust security announcements
- (optional) issue trackers of other distros
- Whenever we discover any new CVE, we add it to an internal database, and use automation tools to create a new issue about the CVE in [Flatcar GitHub issues](https://github.com/Flatcar/Flatcar/issues) with labels `security` and `advisory`.
- If an issue of updating the specific package affected by the new CVE is already open in [Flatcar GitHub issues](https://github.com/Flatcar/Flatcar/issues), then unfortunately we need to manually edit the existing issue to add the new CVE.
