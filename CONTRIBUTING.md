# Contributing Guide

* [New Contributor Guide](#contributing-guide)
  * [Ways to Contribute](#ways-to-contribute)
  * [Participate and contribute](#participate-and-contribute)
  * [Monthly Office hours and Developer Syncs](#Monthly-Office-hours-and-Developer-Syncs)
  * [Report bugs and request features](#Report-bugs-and-request-features)
  * [Pull Request Lifecycle](#pull-request-lifecycle)
  * [Development Environment Setup](#development-environment-setup)
  * [Git and Github](#Git-and-Github)
  * [Start coding](#Start-coding)
  * [Proposing new features](#Proposing-new-features)
  * [Authoring PRs](Authoring-PRs)
  

Welcome! We are glad that you want to contribute to our project! 💖

As you get started, you are in the best position to give us feedback on areas of
our project that we need help with including:

* Problems found during setting up a new developer environment
* Gaps in our Quickstart Guide or documentation
* Bugs in our automation scripts

If anything doesn't make sense, or doesn't work when you run it, please open a
bug report and let us know!

## Ways to Contribute

[Instructions](https://contribute.cncf.io/maintainers/github/templates/required/contributing/#ways-to-contribute)

We welcome many different types of contributions including:

* New features
* Builds, CI/CD
* Bug fixes
* Documentation
* Issue Triage
* Answering questions on Slack/Mailing List/Matrix
* Web design, helping to maintain the Flatcar website
* Communications / Social Media / Blog Posts
* Release management
* Evangelise the project in talks, presentations, and workshops
* Coordinate work between Flatcar maintainers and upstream projects, for instance coordinating work items and planning project roadmaps in special sub-projects like Flatcar CAPI, or our sysext initiative
* Work with contributors and maintainers to organise project-wide events like bug fixing or doc writing days, devrooms at conferences, community days / meetups, or even conferences

Not everything happens through a GitHub pull request. Please come to our
[meetings](### Monthly Office hours and Developer Syncs) or [contact us](maintainers-noreply@flatcar-linux.org) and let's discuss how we can work
together. 

## Participate and contribute

If you are thinking of making a contribution, then please engage with the project as early as possible -- by commenting on an existing issue, or creating a new issue, on GitHub. Consider the project’s mission, and how your contribution furthers it.
Making your intent visible early on can be a major factor for getting your work accepted.

For an introduction to the Flatcar SDK and a walk-through of common developer cases like customising the OS image (e.g. adding or upgrading packages), have a look at our [developer guides](https://www.flatcar.org/docs/latest/reference/developer-guides/); particularly the [howto on building custom images from source](https://www.flatcar.org/docs/latest/reference/developer-guides/sdk-modifying-flatcar/).
The guides aim to provide a solid base for working with the SDK to help you filing successful PRs to the Flatcar project.

For the general guidelines on making PRs/commits easier to review, please check out the project's [contribution guidelines on git](contributions-git.md).


### Monthly Office hours and Developer Syncs

We maintain a [Google Calendar](https://calendar.google.com/calendar/u/0/embed?src=c_ii991mqrpta9en8o7ofd4v19g4@group.calendar.google.com) ([iCal](https://calendar.google.com/calendar/ical/c_ii991mqrpta9en8o7ofd4v19g4%40group.calendar.google.com/public/basic.ics)) with both our Office Hours and Developer Sync meeting series which interested folks can comfortably import into the calendar app of their choice.

Join us in our monthly [office hours meetings](../../discussions/categories/office-hours-agenda) to engage with the Flatcar User community interactively, to learn about the project's directions, and to discuss contributions. We also conduct the occasional user-focused demo of technologies related to image-based Linux.
Lastly, the call includes a brief Release Planning with an update on the changes in the next immediate releases.

If you'd like to share something or if you have a pressing issue you'd like discussed, please let us know.
Either comment on the respective meeting discussion, reach out to us on Matrix (see below), or simply join the meeting and speak up in the meeting's Q&A.

**Flatcar Office Hours are on the second Tuesday of every month at 5:30pm CE[S]T**

The meeting time observes the Central European Time zone and is subject to summer time changes.
It occurs at 5:30pm CE[S]T.
* During summer time (CEST), the meeting occurs at 9pm IST / 5:30pm CEST / 3:30pm GMT / 11:30am EDT / 8:30am PST.
* Outside of summer time (CET), the meeting occurs at 10pm IST / 5:30pm CEST / 4:30pm GMT / 11:30am EST / 8:30am PST.
Special cases occur when CEST is active and EDT/PDT are not - which usually occurs in a narrow, 2-week time window each spring and autumn. Since the meeting always observes CE[S]T, special care needs to be taken by attendees from the Americas.


Meeting agendas are published in advance - check our [discussions section](../../discussions/categories/office-hours-agenda) for examples.
* Video call link: [https://meet.flatcar.org/OfficeHours](https://meet.flatcar.org/OfficeHours)
* A Youtube live stream (which also serves as the meeting's recording) will be published on the respective agenda when a meeting starts.

**Flatcar Developer Syncs commence every 4th Tuesday of a month at 5:30pm CE[S]T **

The meeting time observes the Central European Time zone and is subject to summer time changes.
It occurs at 5:30pm CE[S]T.
Please see above for implications.


While release planning is a recurring part of each community call we also conduct separate Developer Syncs for backlog grooming and task planning. We discuss Roadmap items, special projects, and day-to-day issues in these calls. If you want to participate and discuss or pick up work, that call is for you!
Just like the Office Hours the call includes a brief Release Planning with an update on the changes in the next immediate releases.

* Meeting agendas are published in advance - check our [discussions section](../../discussions/categories/flatcar-developer-sync) for examples.
* Call link: [https://meet.flatcar.org/OfficeHours](https://meet.flatcar.org/OfficeHours)
* A youtube live stream (which also serves as the meeting's recording) will be published on the respective agenda when a meeting starts.

## Report bugs and request features

Please file a respective [issue](issues) right here in the top-level Flatcar github project.
For instance, please use the "New Package Request" issue type to [file your request](https://github.com/flatcar/Flatcar/issues/new/choose). Please see [adding new packages to the Flatcar Linux OS image](adding-new-packages.md) for general guidelines.

We have good first issues for new contributors and help wanted issues suitable for any contributor. [good first issue](https://github.com/flatcar/Flatcar/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) has extra information to help you make your first contribution. [help wanted](TODO) are issues suitable for someone who isn't a core maintainer and is good to move onto after
your first pull request.

Sometimes there won’t be any issues with these labels. That’s ok! There is likely still something for you to work on. If you want to contribute but you don’t know where to start or can't find a suitable issue, you can ⚠️ **explain how people can ask for an issue to work on**.

Once you see an issue that you'd like to work on, please post a comment saying
that you want to work on it. Something like "I want to work on this" is fine.

## Pull Request Lifecycle
<todo>

## Development Environment Setup
For an introduction to the Flatcar SDK and a walk-through of common developer cases like customising the OS image (e.g. adding or upgrading packages), have a look at our [developer guides](https://www.flatcar.org/docs/latest/reference/developer-guides/); particularly the [howto on building custom images from source](https://www.flatcar.org/docs/latest/reference/developer-guides/sdk-modifying-flatcar/).
The guides aim to provide a solid base for working with the SDK to help you filing successful PRs to the Flatcar project.

# Git and Github

This section has the guidelines we use to keep consistency across our different
Git repositories and Github projects.

## Start coding

If you're looking where to start, you can check the issues with the
`good first issue` label. Other labels will be used that may be more related to
the projects themselves, so don't hesitate to get in touch with the developers
if you need more guidance on how to start contributing to our projects.

## Proposing new features

If you want to propose a new feature (e.g adding a package) or do a big change
in the architecture it is highly recommended to open an issue first to discuss
it with the community.

## Authoring PRs

These are general guidelines for making PRs/commits easier to review:

 * Commits should be atomic and self-contained. Divide logically separate changes
   to separate commits. This principle is best explained in the the Linux Kernel
   [submitting patches][linux-sep-changes] guide.

 * Commit messages should explain the intention, _why_ something is done. This,
   too, is best explained in [this section][linux-desc-changes] from the Linux
   Kernel patch submission guide.

 * Commit titles (the first line in a commit) should be meaningful and describe
   _what_ the commit does.

 * Don't add code you will change in a later commit (it makes it pointless to
   review that commit), nor create a commit to add code an earlier commit should
   have added. Consider squashing the relevant commits instead.

 * It's not important to retain your development history when contributing a
   change. Use `git rebase` to squash and order commits in a way that makes them easy to
   review. Keep the final, well-structured commits and not your development history
   that led to the final state.

 * Consider reviewing the changes yourself before opening a PR. It is likely
   you will catch errors when looking at your code critically and thus save the
   reviewers (and yourself) time.

 * Use the PR's description as a "cover letter" and give the context you think
   reviewers might need. Use the PR's description to explain why you are
   proposing the change, give an overview, raise questions about yet-unresolved
   issues in your PR, list TODO items etc.

PRs which follow these rules are easier to review and merge.

[linux-sep-changes]: https://www.kernel.org/doc/html/v4.17/process/submitting-patches.html#separate-your-changes
[linux-desc-changes]: https://www.kernel.org/doc/html/v4.17/process/submitting-patches.html#describe-your-changes

### Commit Format

```
<area>: <description of changes>

Detailed information about the commit message goes here
```

Both the title and the body of the commit message shoud not exceed
72 characters in length. i.e. Please keep the title length under 72
characters, and the wrap the body of the message at 72 characters.

Separate the title and the body by 1 empty line.

Use the [imperative mood](https://chris.beams.io/posts/git-commit/#imperative)
for the title, and don't add a period at the end.

For the commit's message body, a period should come at the end of each
sentence (unless the line is not a regular sentence, e.g. code).

Here is an example of commit messages:

Good:
```
app-shells/bash: update ebuild to 5.3

Gentoo upstream has unmasked bash 5.3 and declared it stable.
This change updates the component to use the latest upstream ebuild.
```

Bad:
```
Update bash

Updated bash to the latest one.
```
