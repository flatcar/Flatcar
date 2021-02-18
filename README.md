# Flatcar Container Linux

## Mission statement

_Flatcar Container Linux is a fully open source, minimal-footprint, secure by default and always up-to-date Linux distribution for running containers at scale._

## Releases

See the [project website](https://kinvolk.io/flatcar-container-linux/) for information about [current releases](https://kinvolk.io/flatcar-container-linux/releases/). 

## Repositories

Github repositories that comprise Flatcar Container Linux are on the [Kinvolk org and using the Flatcar topic](https://github.com/search?q=org%3Akinvolk+topic%3Aflatcar).

## User Documentation

Flatcar Container Linux has a dedicated [documentation site](https://kinvolk.io/docs/flatcar-container-linux/latest/). Some helpful links:

* [Getting started](https://kinvolk.io/docs/flatcar-container-linux/latest/installing/)
* [Working with clusters](https://kinvolk.io/docs/flatcar-container-linux/latest/#creating-clusters)
* [Migrating from CoreOS Container Linux](https://kinvolk.io/docs/flatcar-container-linux/latest/migrating-from-coreos/)
  * [Updating directly from CoreOS Container Linux](https://kinvolk.io/docs/flatcar-container-linux/latest/migrating-from-coreos/update-from-container-linux/)

## Release process

Flatcar Container Linux follows an Alpha-Beta-Stable release process. New features and major version upgrades will enter the Alpha channel for initial testing, then transition to Beta, before landing in Stable.

Note that contrary to features, bug fixes for any release channel will be released to that respective channel directly, i.e. Alpha bug fixes will be included in the next Alpha, Beta fixes will directly go to Beta, and Stable fixes will be released with the next Stable.

### Edge

There’s a fourth channel which is roughly based on Alpha, but otherwise unrelated to the other three - the Edge channel. Edge is meant for testing cutting-edge features, e.g. new BPF functionality in the Linux kernel, or new container runtimes. Edge features are for experimenting, there is no guarantee that Alpha will pick those up.

## General discussions on the project and its direction

For general discussions around Flatcar Container Linux please join our forums (Google groups) for [users](https://groups.google.com/forum/#!forum/flatcar-linux-user) and for [developers](https://groups.google.com/forum/#!forum/flatcar-linux-dev). Please do not use the GitHub project for general discussions. For a quick chat with other users and developers try the `#flatcar` IRC channel on irc.freenode.net.

## Code of Conduct

Please refer to the Kinvolk [Code of Conduct](https://github.com/kinvolk/contribution/blob/master/CODE_OF_CONDUCT.md).

## Contributing to Flatcar Container Linux

We encourage community contributions to the Flatcar project! In order to make the contribution process as smooth as possible, please follow the guidelines below.

First, please engage with the development team as early as possible. Let us know (by commenting on an existing issue, or creating a new issue, on GitHub) if you are thinking of making a contribution, so we can align on the best implementation approach and maximize the chances of it being successfully merged. Consider the project’s mission, and how your contribution furthers and is compatible with it.

### Commit guidelines

For the general guidelines on making PRs/commits easier to review, please checkout Kinvolk's [contribution guidelines on git](https://github.com/kinvolk/contribution/tree/master/topics/git.md).

### Minor Contributions

Short-term concerns and minor features are covered in the [issue tracker](https://github.com/kinvolk/Flatcar/issues/). When approaching the project please ensure you have searched through / reviewed existing issues and pull requests.

If an issue or PR you’d like to contribute to is already assigned to someone, please reach out to them to coordinate your work.

If you would like to start contributing to an issue or PR, please assign it to yourself. It is also often helpful to state your intent in a comment on the issue, as well as to announce a rough ETA of your contribution - this helps others to manage their expectations regarding traction and progress.

### Major Contributions

Major new features are tracked on our [roadmap](https://github.com/orgs/kinvolk/projects/12).

### Requesting new packages

Please see [adding new packages to the Flatcar Linux OS image](adding-new-packages.md) for general guidelines, and please use the "New Package Request" issue type to [file your request](https://github.com/kinvolk/Flatcar/issues/new/choose).
