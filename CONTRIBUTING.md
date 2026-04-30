# Contributing Guide

Welcome! We're so glad you're here and interested in contributing to Flatcar! 💖

## Table of Contents

- [Contributing Guide](#contributing-guide)
  - [Table of Contents](#table-of-contents)
  - [Ways to Contribute](#ways-to-contribute)
  - [Getting Started](#getting-started)
    - [Finding Issues](#finding-issues)
    - [Proposing New Features](#proposing-new-features)
  - [Repository Overview](#repository-overview)
    - [OS Image Build System](#os-image-build-system)
    - [Update and Reboot Infrastructure](#update-and-reboot-infrastructure)
    - [Node Configuration and Provisioning](#node-configuration-and-provisioning)
    - [System Extensions](#system-extensions)
    - [Testing and Tooling](#testing-and-tooling)
    - [Deployment and Cloud](#deployment-and-cloud)
    - [Cluster API Integration](#cluster-api-integration)
    - [Flatcar Apps](#flatcar-apps)
    - [Project and Community](#project-and-community)
  - [Communication Channels](#communication-channels)
  - [Development](#development)
    - [Development Environment Setup](#development-environment-setup)
    - [Pull Request Lifecycle](#pull-request-lifecycle)
    - [Authoring PRs](#authoring-prs)
      - [Commit Best Practices](#commit-best-practices)
      - [PR Description](#pr-description)
    - [Commit Guidelines](#commit-guidelines)
      - [The Rules](#the-rules)
      - [Examples](#examples)

---

As a newcomer, you're actually in the best position to help us improve! We'd really love your feedback on:

- Confusing steps when setting up your developer environment
- Missing information in our guides or documentation
- Bugs or rough edges in our automation scripts

If something doesn't make sense or doesn't work, please let us know by opening a bug report — we genuinely appreciate it and every bit of feedback helps make Flatcar better!

---

## Ways to Contribute

There are so many ways to get involved! We welcome all kinds of contributions:

| Category          | Examples                                                                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Code**          | New features, bug fixes, builds, CI/CD                                                                                                                                                                              |
| **Documentation** | Guides, tutorials, API docs                                                                                                                                                                                         |
| **Community**     | Issue triage, answering questions on Discord/Matrix/Slack                                                                                                                                                           |
| **Flatcar Apps**  | Create reference implementations for running services on Flatcar (e.g., [Minecraft](https://github.com/flatcar/flatcar-app-minecraft), [Jitsi](https://github.com/flatcar/flatcar-app-jitsi)) — great for learning! |
| **Outreach**      | Blog posts, talks, presentations, workshops                                                                                                                                                                         |
| **Coordination**  | Release management, upstream project coordination (e.g., Flatcar CAPI, sysext initiative)                                                                                                                           |
| **Events**        | Bug fixing days, doc writing days, devrooms, meetups, conferences                                                                                                                                                   |
| **Design**        | Web design, maintaining the Flatcar website                                                                                                                                                                         |

Not everything happens through a GitHub pull request. Please come to our [meetings or contact us](https://github.com/flatcar/Flatcar/blob/main/README.md#community-meetings) to discuss how we can work together — we'd love to meet you!

---

## Getting Started

Thinking of contributing? Awesome! The best way to start is to engage with the project early — drop a comment on an existing issue or open a new one. Let us know what you're interested in working on. This helps us help you, and it's often the key to getting your contribution accepted smoothly.

To report bugs or request features, just file an [issue](https://github.com/flatcar/Flatcar/issues) — we're always happy to help point you in the right direction!

### Finding Issues

Not sure where to start? No worries — we've got you covered!

| Label                                                                                                                 | Description                                             |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| [`good first issue`](https://github.com/flatcar/Flatcar/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) | Extra guidance to help you make your first contribution |
| [`help wanted`](https://github.com/flatcar/Flatcar/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)           | Issues suitable for non-core maintainers                |

> 💡 **Tip:** Don't see any issues with these labels? No problem! There's always something exciting to work on. Hop on [Discord](https://discord.gg/PMYjFUsJyq) or join one of our Office Hours — we'll find something that fits your interests and skill level.

> 🌟 **Great for newcomers:** Consider contributing a [Flatcar App](https://github.com/flatcar/Flatcar/issues/2029)! A Flatcar App is a reference implementation showing how to run a specific service on Flatcar (e.g., [Minecraft Server](https://github.com/flatcar/flatcar-app-minecraft), [Jitsi](https://github.com/flatcar/flatcar-app-jitsi)). It's a fantastic way to learn Flatcar hands-on while creating something awesome that helps other newcomers learn too!

Found something you'd like to work on? Excellent! Just leave a comment like "I'd like to work on this" — that's all it takes to claim it.

### Proposing New Features

Got an idea for a new feature or a big architectural change? We'd love to hear it! Don't be shy — the best approach is to open an issue first so we can discuss it together before you invest time in implementation.

For package requests, use the "New Package Request" issue type and check out [Adding New Packages](https://github.com/flatcar/Flatcar/blob/main/adding-new-packages.md) for guidelines.

---

## Repository Overview

The Flatcar project is spread across multiple repositories in the [`flatcar` GitHub organisation](https://github.com/flatcar). Here is a map of the key repos, grouped by function, to help you find where to contribute.

### OS Image Build System

These repos are the beating heart of the OS image build system.

| Repository | Description |
| ---------- | ----------- |
| [scripts](https://github.com/flatcar/scripts) | Image build, SDK, and package management — the main entry point for OS development |
| [init](https://github.com/flatcar/init) | systemd boot files and early OS initialisation |
| [bootengine](https://github.com/flatcar/bootengine) | Early-boot initrd (dracut) modules |
| [baselayout](https://github.com/flatcar/baselayout) | Base filesystem layout |
| [flatcar-build-scripts](https://github.com/flatcar/flatcar-build-scripts) | Extra build helper scripts independent of the main `scripts` repo |

### Update and Reboot Infrastructure

Flatcar ships atomic, automatic updates. These repos implement the full update and reboot-coordination stack.

| Repository | Description |
| ---------- | ----------- |
| [update_engine](https://github.com/flatcar/update_engine) | Update daemon — the Omaha protocol client running on each node |
| [nebraska](https://github.com/flatcar/nebraska) | Web-based Omaha update server, dashboard, and release manager |
| [ue-rs](https://github.com/flatcar/ue-rs) | Experimental Rust implementation of the Omaha update client |
| [locksmith](https://github.com/flatcar/locksmith) | Reboot coordinator using etcd locks to prevent cluster-wide simultaneous reboots |
| [flatcar-linux-update-operator](https://github.com/flatcar/flatcar-linux-update-operator) | Kubernetes operator that integrates the update engine with the Kubernetes node lifecycle |
| [fleetlock](https://github.com/flatcar/fleetlock) | Go client for the FleetLock reboot-coordination protocol |

### Node Configuration and Provisioning

Tools for bootstrapping and configuring nodes at first boot.

| Repository | Description |
| ---------- | ----------- |
| [ignition](https://github.com/flatcar/ignition) | Flatcar's fork of Ignition — used for CAPI builds and development |
| [coreos-cloudinit](https://github.com/flatcar/coreos-cloudinit) | Legacy cloud-init configuration tool for Flatcar |
| [container-linux-config-transpiler](https://github.com/flatcar/container-linux-config-transpiler) | Converts human-friendly Container Linux Config YAML into Ignition JSON |

### System Extensions

Flatcar is minimal by design; system extensions let you layer software on top without modifying the read-only OS image.

| Repository | Description |
| ---------- | ----------- |
| [sysext-bakery](https://github.com/flatcar/sysext-bakery) | Recipes for building systemd-sysext images (Docker, containerd, Kubernetes, and more) |

### Testing and Tooling

| Repository | Description |
| ---------- | ----------- |
| [mantle](https://github.com/flatcar/mantle) | Test framework (kola), image upload tools, and general glue utilities |
| [toolbox](https://github.com/flatcar/toolbox) | Interactive debugging container that provides a mutable shell on a Flatcar node |
| [update-ssh-keys](https://github.com/flatcar/update-ssh-keys) | Manages authorized SSH keys from multiple sources |
| [mayday](https://github.com/flatcar/mayday) | Gathers diagnostic support information from a running node |
| [seismograph](https://github.com/flatcar/seismograph) | Disk partition management tools |
| [nss-altfiles](https://github.com/flatcar/nss-altfiles) | NSS module that allows relocating `/etc/passwd` and related files |

### Deployment and Cloud

Templates, examples, and tooling for getting Flatcar running on cloud and on-prem infrastructure.

| Repository | Description |
| ---------- | ----------- |
| [flatcar-terraform](https://github.com/flatcar/flatcar-terraform) | Terraform examples for AWS, Azure, GCP, Equinix Metal, and more |
| [flatcar-packer-qemu](https://github.com/flatcar/flatcar-packer-qemu) | Packer templates for building QEMU and Vagrant images |
| [flatcar-cloud-image-uploader](https://github.com/flatcar/flatcar-cloud-image-uploader) | Tooling for uploading Flatcar images to cloud providers |

### Cluster API Integration

| Repository | Description |
| ---------- | ----------- |
| [cluster-api-bootstrap-provider-kubeadm-ignition](https://github.com/flatcar/cluster-api-bootstrap-provider-kubeadm-ignition) | CAPI bootstrap provider that provisions Flatcar nodes using Ignition configs generated by kubeadm |

### Flatcar Apps

Reference implementations showing how to run real-world services on Flatcar — great for learning and as starting points for your own deployments.

| Repository | Description |
| ---------- | ----------- |
| [flatcar-app-minecraft](https://github.com/flatcar/flatcar-app-minecraft) | Containerised PaperMC Minecraft server deployable on Azure and other clouds |
| [flatcar-app-jitsi](https://github.com/flatcar/flatcar-app-jitsi) | Jitsi video-conferencing server automation |
| [flatcar-mastodon](https://github.com/flatcar/flatcar-mastodon) | Automation for deploying a Mastodon node on Flatcar |

### Project and Community

| Repository | Description |
| ---------- | ----------- |
| [Flatcar](https://github.com/flatcar/Flatcar) | Central issue tracker, project documentation, governance, and release planning |
| [flatcar-website](https://github.com/flatcar/flatcar-website) | Source for [flatcar.org](https://www.flatcar.org/) |
| [flatcar-demos](https://github.com/flatcar/flatcar-demos) | Demo scripts and artefacts from conferences and meetups |
| [flatcar-tutorial](https://github.com/flatcar/flatcar-tutorial) | Hands-on tutorial material for newcomers |

> 💡 **Starting out?** `scripts` is where most OS-level contributions happen. `sysext-bakery` is a great low-barrier entry point for adding or updating software extensions.

---

## Communication Channels

For all communication channels, community meetings, and social media links, see the [Communication Channels](https://github.com/flatcar/Flatcar/blob/main/README.md#communication-channels) section in the README. Come hang out with us on [Discord](https://discord.gg/PMYjFUsJyq)!

---

## Development

### Development Environment Setup

Ready to dive into the code? Let's go! Our [Developer Guides](https://www.flatcar.org/docs/latest/reference/developer-guides/) will walk you through the Flatcar SDK and common tasks like adding or upgrading packages. Start here:

- [Building Custom Images from Source](https://www.flatcar.org/docs/latest/reference/developer-guides/sdk-modifying-flatcar/)

These guides will give you a solid foundation for working with the SDK and help you submit PRs that sail through review!

### Pull Request Lifecycle

Pull requests can be issued from repository branches (maintainers only) or from forks. The project treats all PRs equally for review and merge, regardless of origin.

**Requirements:**
- Successful CI
- At least one LGTM from a maintainer who is not the PR author
- Approvers may be co-authors (allowing reviewers to suggest changes)

**Stages:**

| Stage                   | Description                                                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **1. Filed**            | PR is created. Draft PRs only undergo build+test when explicitly requested.                                      |
| **2. Ready for Review** | Maintainers can begin reviewing and approve CI runs. Authors may file directly in this stage if the PR is ready. |
| **3. Under Review**     | Maintainers add comments, request changes, and vet against Flatcar's mission and core principles.                |
| **4. Merged or Closed** | PR is merged upon approval or closed without merge.                                                              |

> 💡 **Tip:** PR feeling stuck? Don't be shy — reach out on [Discord](https://discord.gg/PMYjFUsJyq) or bring it up in a community meeting. We're here to help and we want to see your contribution succeed!

### Authoring PRs

Here are some tips to make your PRs shine and get merged quickly:

#### Commit Best Practices

- **Atomic commits:** Each commit should be self-contained and address a single logical change. See the Linux Kernel guide on [separating changes][linux-sep-changes].

- **Meaningful messages:** Commit messages should explain _why_ something is done, not just _what_. See [describing changes][linux-desc-changes].

- **Clean history:** Use `git rebase` to squash and order commits logically. Don't retain messy development history.

- **No throwaway commits:** Don't add code you'll change in a later commit. Squash related changes together.

- **Self-review:** Give your own code a critical look before submitting — you'll often spot things you missed, and reviewers will thank you!

#### PR Description

Think of your PR description as a cover letter. Help reviewers understand:
- Explain _why_ you're proposing the change
- Provide an overview of the changes
- List any unresolved questions or TODO items
- Give reviewers the context they need

### Commit Guidelines

Great commit messages make everyone's life easier (and make you look like a pro!). Here's the format we use:

```
<area>: <description of changes>

Detailed information about the commit message goes here.
```

#### The Rules

| Rule                  | Details                                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Line length**       | Title ≤ 72 characters; body wrapped at 72 characters                                                                 |
| **Blank line**        | Separate title and body with one empty line                                                                          |
| **Title mood**        | Use [imperative mood](https://chris.beams.io/posts/git-commit/#imperative) (e.g., "Add feature" not "Added feature") |
| **Title punctuation** | No period at the end                                                                                                 |
| **Body punctuation**  | End sentences with periods                                                                                           |

#### Examples

✅ **Good:**
```
app-shells/bash: update ebuild to 5.3

Gentoo upstream has unmasked bash 5.3 and declared it stable.
This change updates the component to use the latest upstream ebuild.
```

❌ **Bad:**
```
Update bash

Updated bash to the latest one.
```

---

Thanks for reading, and thank you so much for contributing! 🙏 We're thrilled to have you as part of the Flatcar community. If you have any questions at all, don't hesitate to reach out — we're always happy to help and can't wait to see what you build! 🎉

[linux-sep-changes]: https://www.kernel.org/doc/html/latest/process/submitting-patches.html#separate-your-changes
[linux-desc-changes]: https://www.kernel.org/doc/html/latest/process/submitting-patches.html#describe-your-changes