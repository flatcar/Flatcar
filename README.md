# Flatcar Container Linux

## Mission statement

_Flatcar Container Linux is a fully open source, minimal-footprint, secure by default and always up-to-date Linux distribution for running containers at scale._

## Code of Conduct

Please refer to the Flatcar [Code of Conduct](CODE_OF_CONDUCT.md).

## Releases

See the [project website](https://flatcar-linux.org) for information about [current releases](https://flatcar-linux.org/releases).

## Install and operate Flatcar

Flatcar Container Linux has a dedicated [documentation site](https://docs.flatcar-linux.org). Some helpful links:

* [Getting started](http://docs.flatcar-linux.org/installing)
* [Working with clusters](http://docs.flatcar-linux.org/#creating-clusters)

**Does Flatcar run in my environment?** Consult the [interop-matrix](interop-matrix.md).

## Report bugs and request features

Please file a respective [issue](issues) right here in the top-level github project.
For instance, please use the "New Package Request" issue type to [file your request](https://github.com/kinvolk/Flatcar/issues/new/choose). Please see [adding new packages to the Flatcar Linux OS image](adding-new-packages.md) for general guidelines.

## Participate and contribute

If you are thinking of making a contribution, then please engage with the project as early as possible -- by commenting on an existing issue, or creating a new issue, on GitHub. Consider the project’s mission, and how your contribution furthers it.
Making your intent visible early on can be a major factor for getting your work accepted.

For an introduction to the Flatcar SDK and a walk-through of common developer cases like customising the OS image (e.g. adding or upgrading packages), have a look at our [developer guides](https://docs.flatcar-linux.org/reference/developer-guides/); particularly the [customise images howto](https://docs.flatcar-linux.org/reference/developer-guides/sdk-modifying-flatcar/).
The guides aim to provide a solid base for working with the SDK to help you filing successful PRs to the Flatcar project.

For the general guidelines on making PRs/commits easier to review, please check out the project's [contribution guidelines on git](contributions-git.md).

While short-term concerns are logged in our [issue tracker](https://github.com/flatcar-linux/Flatcar/issues), long-term items are reflected on our [roadmap board](https://github.com/orgs/kinvolk/projects/16).

### Monthly Community meeting and release planning

We maintain a [Google Calendar](https://calendar.google.com/calendar/u/0/embed?src=c_ii991mqrpta9en8o7ofd4v19g4@group.calendar.google.com) ([iCal](https://calendar.google.com/calendar/ical/c_ii991mqrpta9en8o7ofd4v19g4%40group.calendar.google.com/public/basic.ics)) with both our community calls and release planning meeting series which interested folks can comfortably import into the calendar app of their choice.

Join us in our monthly [community meetings](community-meetings) to engage with the Flatcar community interactively, to learn about the project's directions, and to discuss contributions.
Meeting agendas are published in advance - watch out for [open PRs on the communit-meetings/](https://github.com/flatcar-linux/Flatcar/pulls) folder. If you have a pressing issue of common interest you'd like discussed, please let us know on Matrix, or simply bring it to the next meeting's Q&A.

For more sizeable agenda items please consider speaking up on the PR of the agenda of the next meeting, or file a new PR if the upcoming meeting's agenda was already merged.

**Community calls are on the second Tuesday of every month at 9pm IST / 5:30pm CEST / 3:30pm GMT / 11:30am EDT / 8:30am PST**
* Zoom link: [https://us06web.zoom.us/j/84336116610](https://us06web.zoom.us/j/84336116610)
  * Meeting ID: 843 3611 6610
  * Passcode: 444888
* A youtube live stream (which also serves as the meeting's recording) will be published on the respective agenda when a meeting starts.

While release planning is a recurring part of each community call we also conduct separate release plannings - the Flatcar Alpha channel roughly has a 2-week release cadence, therefore one planning per month does not suffice.

**Additional stand-alone release planning meetings commence every 4th Tuesday of a month at 9pm IST / 5:30pm CEST / 3:30pm GMT / 11:30am EDT / 8:30am PST**
* Zoom link: [https://us06web.zoom.us/j/82054240491](https://us06web.zoom.us/j/82054240491)
  * Meeting ID: 820 5424 0491
  * Passcode: 444888
* A youtube live stream (which also serves as the meeting's recording) will be published on the respective agenda when a meeting starts.


### Chat

For quick questions or for just hanging out with the community please use
* Our matrix chat (via element.io): [https://app.element.io/#/room/#flatcar:matrix.org](https://app.element.io/#/room/#flatcar:matrix.org)
* A bridged IRC channel (Libera.chat): #[flatcar](ircs://irc.libera.chat:6697/#flatcar) channel is also available.

### Discussions

For more far-reaching topics please have a look at our [discussions](https://github.com/flatcar-linux/Flatcar/discussions). Feel to open a new discussion if you don't find an existing one covering your topic.

### Mailing lists

Though the use of Github Discussions is encouraged (see above), we also maintain groups / mailing lists for a more old-fashioned way of having a discussion. Please note that we might consider to discontinue these mailing lists at some point in the future.
* Flatcar Users: https://groups.google.com/g/flatcar-linux-user
* Flatcar Devs: https://groups.google.com/g/flatcar-linux-dev

## Release process

Flatcar Container Linux follows an Alpha-Beta-Stable release process. New features and major version upgrades will enter the Alpha channel for initial testing, then transition to Beta, before landing in Stable.

Note that unlike features, bug fixes for any release channel will be released to that respective channel directly, i.e. Alpha bug fixes will be included in the next Alpha, Beta fixes will directly go to Beta, and Stable fixes will be released with the next Stable.

We plan our releases in a 14-day cadence. The maintainer team holds fortnightly release meetings - both as recurring part of our monthly [community calls](tree/main/community-meetings/) as well as a separate meeting in-between the monthly community call cadence. Up-to-date planning status is reflected in our [release planning board](https://github.com/orgs/kinvolk/projects/15).

### LTS

Some users prefer to avoid the operational impact of frequent version upgrades.
For such users, the Flatcar project provides an "LTS channel".
The LTS channel / branch is based on a "golden Stable" and is maintained for 18 months.
A new LTS is branched from Stable every 12 months, leaving a 6 months window for LTS users to upgrade.

## Project governance

Flatcar is a community-driven project, with community members participating through the following forums:

* Contributors.
* Flatcar Team.
* Core Working Group.

### Contributors

Every participant of the open source project - bug reporter, feature requester, code contributor - is considered a contributor.

### The Flatcar Team

The Flatcar Team comprises contributors with a proven track record of helping the project.
They are members of the Flatcar project on github and are typically responsible for a specific domain within the project, for example:
* Interoperability with a particular environment
* Prioritization and handling of issues
* A specific package or set of packages
* The build / continuous integration process
* Releases
* Community engagement.

### The Core Working Group

The Core Working Group comprises long term core contributors who have demonstrable impact on the project as a whole.
The Working Group are project administrators/maintainers and ultimately responsible for the project's long-term direction as well as stewarding day-to-day project work.

## Repositories

The repositories are currently part of the Kinvolk org for historical reasons. Flatcar will move to its own github org soon.

Meanwhile, github repositories that comprise Flatcar Container Linux can be found via the [Flatcar topic](https://github.com/search?q=org%3Akinvolk+topic%3Aflatcar).
