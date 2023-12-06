# Flatcar Container Linux

## Mission statement

_Flatcar Container Linux is a fully open source, minimal-footprint, secure by default and always up-to-date Linux distribution for running containers at scale._

## Code of Conduct

We follow the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/main/code-of-conduct.md).

Please contact [private Maintainer mailing list](maintainers@flatcar-linux.org) or the Linux Foundation mediator, Mishi Choudhary mishi@linux.com
to report an issue.

## Releases

See the [project website](https://www.flatcar.org/) for information about [current releases](https://www.flatcar.org/releases).

## Install and operate Flatcar

Flatcar Container Linux has a dedicated [documentation site](https://www.flatcar.org/docs/latest/).

The getting started guide has further links to the topics Ignition, local testing with QEMU, controlling automatic updates, and usage with cloud providers:

* [Getting started](https://www.flatcar.org/docs/latest/installing/)

**Does Flatcar run in my environment?** Consult the [interop-matrix](interop-matrix.md).

**Does Flatcar have CIS Benchmarks?** Consult the [CIS reports](CIS/README.md).

## Report bugs and request features

Please file a respective [issue](https://github.com/flatcar/Flatcar/issues) right here in this github project.
For instance, please use the "New Package Request" issue type to [file your request](https://github.com/flatcar/Flatcar/issues/new/choose).
Please see [adding new packages to the Flatcar Linux OS image](adding-new-packages.md) for general guidelines.

## Participate and contribute

If you are thinking of making a contribution, then please engage with the project as early as possible -- by commenting on an existing issue, or creating a new issue, on GitHub. Consider the project’s mission, and how your contribution furthers it.
Making your intent visible early on can be a major factor for getting your work accepted.

For the general guidelines on making PRs/commits easier to review, please check out the project's [contribution guidelines](CONTRIBUTING.md).

For an introduction to the Flatcar SDK and a walk-through of common developer cases like customising the OS image (e.g. adding or upgrading packages), have a look at our [developer guides](https://www.flatcar.org/docs/latest/reference/developer-guides/); particularly the [howto on building custom images from source](https://www.flatcar.org/docs/latest/reference/developer-guides/sdk-modifying-flatcar/).
The guides aim to provide a solid base for working with the SDK to help you filing successful PRs to the Flatcar project.

### Becoming a maintainer

The Flatcar maintainer path is laid out in our [governance document](governance.md).

## Project status and roadmap - What's everybody working on, right now and in the future?

1. short-term concerns (bugs and minor enhancements) enter the project via our [issue tracker](https://github.com/flatcar/Flatcar/issues)
2. our [tactical board](https://github.com/orgs/flatcar/projects/7/views/1) reflects the issues and PRs the maintainers and the contributors are currently engaged with
3. items which are done will be assigned to an upcoming release on the [release board](https://github.com/orgs/flatcar/projects/7/views/8)
   in our release planning calls

Lastly, epics like major features and long-term items are reflected in our [roadmap board](https://github.com/orgs/flatcar/projects/7/views/9).

Check out our Matrix and Slack channels (see below) for getting into contact with maintainers, and consider joining our Flatcar Developer Sync (next section below) where contributors and maintainers coordinate our work.

### Monthly Office hours and Developer Syncs

We maintain a [Google Calendar](https://calendar.google.com/calendar/u/0/embed?src=c_ii991mqrpta9en8o7ofd4v19g4@group.calendar.google.com) ([iCal](https://calendar.google.com/calendar/ical/c_ii991mqrpta9en8o7ofd4v19g4%40group.calendar.google.com/public/basic.ics)) with both our Office Hours and Developer Sync meeting series which interested folks can comfortably import into the calendar app of their choice.

Join us in our monthly [office hours meetings](../../discussions/categories/flatcar-office-hours) to engage with the Flatcar User community interactively, to learn about the project's directions, and to discuss contributions. We also conduct the occasional user-focused demo of technologies related to image-based Linux.
Lastly, the call includes a brief Release Planning with an update on the changes in the next immediate releases.

If you'd like to share something or if you have a pressing issue you'd like discussed, please let us know.
Either comment on the respective meeting discussion, reach out to us on Matrix (see below), or simply join the meeting and speak up in the meeting's Q&A.

**Flatcar Office Hours are on the second Tuesday of every month at 9pm IST / 5:30pm CEST / 3:30pm GMT / 11:30am EDT / 8:30am PST**

* Meeting agendas are published in advance - check our [discussions section](../../discussions/categories/flatcar-office-hours) for examples.
* Call link: [https://meet.flatcar.org/OfficeHours](https://meet.flatcar.org/OfficeHours)
* A Youtube live stream (which also serves as the meeting's recording) will be published on the respective agenda when a meeting starts.


**Flatcar Developer Syncs commence every 4th Tuesday of a month at 9pm IST / 5:30pm CEST / 3:30pm GMT / 11:30am EDT / 8:30am PST**

While release planning is a recurring part of each community call we also conduct separate Developer Syncs for backlog grooming and task planning. We discuss Roadmap items, special projects, and day-to-day issues in these calls. If you want to participate and discuss or pick up work, that call is for you!
Just like the Office Hours the call includes a brief Release Planning with an update on the changes in the next immediate releases.

* Meeting agendas are published in advance - check our [discussions section](../../discussions/categories/flatcar-developer-sync) for examples.
* Call link: [https://meet.flatcar.org/OfficeHours](https://meet.flatcar.org/OfficeHours)
* A youtube live stream (which also serves as the meeting's recording) will be published on the respective agenda when a meeting starts.

### Social Media/Fediverse

You can follow the [Flatcar Mastodon account](https://hachyderm.io/@flatcar).

### Chat

For quick questions or for just hanging out with the community please use
* Our matrix chat (via element.io): [https://app.element.io/#/room/#flatcar:matrix.org](https://app.element.io/#/room/#flatcar:matrix.org)
* Our Slack channel in the Kubernetes Slack org: https://kubernetes.slack.com/archives/C03GQ8B5XNJ
* A bridged IRC channel (Libera.chat): #[flatcar](ircs://irc.libera.chat:6697/#flatcar) channel is also available.

### Discussions

For more far-reaching topics please have a look at our [discussions](https://github.com/flatcar/Flatcar/discussions). Feel free to open a new discussion if you don't find an existing one covering your topic.

### Mailing lists

Though the use of Github Discussions is encouraged (see above), we also maintain groups / mailing lists for a more old-fashioned way of having a discussion. Please note that we might consider to discontinue these mailing lists at some point in the future.
* Flatcar Users: https://groups.google.com/g/flatcar-linux-user
* Flatcar Devs: https://groups.google.com/g/flatcar-linux-dev

## Release process

Flatcar Container Linux follows an Alpha-Beta-Stable release process. New features and major version upgrades will enter the Alpha channel for initial testing, then transition to Beta, before landing in Stable.

Note that unlike features, bug fixes for any release channel will be released to that respective channel directly, i.e. Alpha bug fixes will be included in the next Alpha, Beta fixes will directly go to Beta, and Stable fixes will be released with the next Stable.

We plan our releases in a 14-day cadence. The maintainer team holds fortnightly release meetings - both as recurring part of our monthly [community calls](tree/main/community-meetings/) as well as a separate meeting in-between the monthly community call cadence. Up-to-date planning status is reflected in our [release planning board](https://github.com/orgs/flatcar/projects/7).

### LTS

Some users prefer to avoid the operational impact of frequent version upgrades.
For such users, the Flatcar project provides an "LTS channel".
The LTS channel / branch is based on a "golden Stable" and is maintained for 18 months.
A new LTS is branched from Stable every 12 months, leaving a 6 months window for LTS users to upgrade.

## Project governance

Flatcar is a community-driven project, with community members participating through the following forums:

* Contributors.
* Maintainers.

Every participant of the open source project - bug reporter, feature requester, code contributor - is considered a contributor.

Maintainers have commit access to one or more repositories and help govern the project, driving it forward and maintaining its scope and vision.
Please find more details in our [governance doc](governance.md).

## Repositories

The repositories are currently part of the Kinvolk org for historical reasons. Flatcar will move to its own github org soon.

Meanwhile, github repositories that comprise Flatcar Container Linux can be found via the [organization](https://github.com/flatcar) page.
