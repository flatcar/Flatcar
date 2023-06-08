# Flatcar Security 
<todo - describe a security Schedule of tracking security issues of Flatcar>
- Describe the process of tracking security issues for Flatcar, especially tracking issues from upstream projects like Gentoo Linux.

## Daily security runbook for Security team primaries and secondaries

The runbook below discusses steps for identifying new potential security issues and for making the issues known to the Flatcar project's maintainers and / or the other members of the Security team.
Embargoed issues are recorded in a private issue tracker only accessible by the Security team, while public issues are openly tracked in the [Flatcar project](https://github.com/Flatcar/Flatcar/issues).

Primaries are expected to execute the runbook at least once per day, optionally assisted or off-loaded by Secondaries.

Every day look into upstream security trackers like below:
- Gentoo security vulnerabilities. It might be useful to use gorss + RSS feed for this.
- oss-security mailing list
- Golang announce mailing list
- Rust security announcements
- (optional) issue trackers of other distros
- Whenever we discover any new CVE, we add it to an internal database, and use automation tools to create a new issue about the CVE in [Flatcar GitHub issues](https://github.com/Flatcar/Flatcar/issues) with labels `security` and `advisory`.
- If an issue of updating the specific package affected by the new CVE is already open in [Flatcar GitHub issues](https://github.com/Flatcar/Flatcar/issues), then unfortunately we need to manually edit the existing issue to add the new CVE.
