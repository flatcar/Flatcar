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
- If we see any new CVE, then add it to the CVE spreadsheets (still private), and click the link (above left) to generate new issues. Then we should be able to see a new issue created in Kinvolk security Github issues. (still private)
- If the package of the new CVE is already open in Kinvolk security Github issues, then unfortunately we need to manually edit the existing issue to add the new CVE.
