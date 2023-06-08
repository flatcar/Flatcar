# Flatcar Security 
<todo - describe a security Schedule of tracking security issues of Flatcar>
- Describe the process of tracking security issues for Flatcar, especially tracking issues from upstream projects like Gentoo Linux.

## Primary person should do so:

Every day look into upstream security trackers like below:
- Gentoo security vulnerabilities. It might be useful to use gorss + RSS feed for this.
- oss-security mailing list
- Golang announce mailing list
- Rust security announcements
- (optional) RedHat vulnerabilities
- Whenever we discover any new CVE, we add it to an internal database, and use automation tools to create a new issue about the CVE in [Flatcar GitHub issues](https://github.com/Flatcar/Flatcar/issues) with labels `security` and `advisory`.
- If the package of the new CVE is already open in Kinvolk security Github issues, then unfortunately we need to manually edit the existing issue to add the new CVE.
