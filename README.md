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

For quick questions or for just hanging out with the community please use
* Our matrix chat (via element.io): [https://app.element.io/#/room/#flatcar:matrix.org](https://app.element.io/#/room/#flatcar:matrix.org)

For general discussions please head to our groups / mailing lists:
* Flatcar Users: https://groups.google.com/g/flatcar-linux-user
* Flatcar Devs: https://groups.google.com/g/flatcar-linux-dev

If you are thinking of making a contribution, then please engage with the project as early as possible -- by commenting on an existing issue, or creating a new issue, on GitHub. Consider the project’s mission, and how your contribution furthers it.
Making your intent visible early on can be a major factor for getting your work accepted.

Join us in our monthly [community meetings](community-meetings) to engage with the Flatcar community interactively, to learn about the project's directions, and to discuss contributions.
Meeting agendas are published in advance. If you have a pressing issue of common interest you'd like discussed, please let us know on Matrix, or simply bring it to the next meeting's Q&A.
For more sizeable agenda items please consider filing a PR to the agenda of the next meeting.

For an introduction to the Flatcar SDK and a walk-through of common developer cases like customising the OS image (e.g. adding or upgrading packages), have a look at our [developer guides](https://docs.flatcar-linux.org/reference/developer-guides/); particularly the [customise images howto](https://docs.flatcar-linux.org/reference/developer-guides/sdk-modifying-flatcar/).
The guides aim to provide a solid base for working with the SDK to help you filing successful PRs to the Flatcar project.

For the general guidelines on making PRs/commits easier to review, please check out the project's [contribution guidelines on git](contributions-git.md).

## Release process

Flatcar Container Linux follows an Alpha-Beta-Stable release process. New features and major version upgrades will enter the Alpha channel for initial testing, then transition to Beta, before landing in Stable.

Note that unlike features, bug fixes for any release channel will be released to that respective channel directly, i.e. Alpha bug fixes will be included in the next Alpha, Beta fixes will directly go to Beta, and Stable fixes will be released with the next Stable.

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
