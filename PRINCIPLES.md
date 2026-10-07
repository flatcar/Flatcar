# Flatcar Container Linux — Principles & Design Philosophy

This document answers a common question: *"Does Flatcar have a principle document? How does it work, and how is it different from other similar projects?"*

## Design Principles

Flatcar Container Linux is built around a small set of core ideas:

- **No package manager.** There is no `apt`, `yum`, or similar tool. This eliminates configuration drift between machines — every node running the same Flatcar version is identical.
- **Immutable, read-only root filesystem.** The OS filesystem cannot be modified at runtime, which shrinks the attack surface and makes systems predictable and reproducible.
- **Declarative provisioning via Ignition.** Instead of manually configuring a machine after boot, you describe the desired state in an Ignition config, and Flatcar applies it atomically on first boot.
- **Atomic, automatic updates.** Updates are downloaded and applied in the background to a passive partition, then activated on the next reboot. If an update fails, the system can roll back to the last known-good version.
- **Minimal footprint.** Flatcar ships only what is needed to run containers — nothing more. Additional software is expected to run inside containers or system extensions (sysext), not on the base OS.

## How It Works

1. You provision a machine with an **Ignition** config describing users, files, systemd units, disks, etc.
2. Flatcar boots and applies that configuration exactly once, atomically.
3. The system then runs your container workloads (Docker, Kubernetes, etc.) with the OS itself staying out of the way.
4. In the background, `update_engine` checks for new releases and applies them to the alternate (B) partition. On the next reboot, the system switches to the updated partition.

## How Flatcar Differs from Similar Projects

| Aspect | Flatcar Container Linux | Talos Linux |
|---|---|---|
| **Management model** | Traditional Linux: SSH access, systemd, standard tooling | API-driven only: no SSH, no shell — managed entirely through a gRPC API |
| **Origin** | Fork/successor of CoreOS Container Linux (after CoreOS was acquired by Red Hat/IBM and Container Linux was discontinued) | Purpose-built from scratch specifically as a minimal OS for Kubernetes |
| **Scope** | General-purpose container host — can run any container workload | Kubernetes-only; not intended as a general container host |
| **Debuggability** | Familiar Linux debugging tools available (journalctl, standard filesystem layout, SSH) | Debugging happens through the Talos API and its own tooling, since there's no traditional shell access |
| **Flexibility** | Closer to a "normal" immutable Linux distro, easier to adapt to non-Kubernetes use cases | More opinionated and locked-down, trading flexibility for a smaller attack surface |

In short: **Flatcar keeps the familiar feel of a Linux server while making it immutable and self-updating**, whereas **Talos removes the traditional OS interface entirely** in favor of a fully API-managed appliance model.

## Where These Principles Live Today

There is no single canonical "principles" document beyond this one — the philosophy is currently expressed across several places:

- [`README.md`](./README.md) — project overview and quick orientation
- [`governance.md`](./governance.md) — how the project is governed and how decisions are made
- [flatcar.org/docs](https://www.flatcar.org/docs/latest/) — the full technical documentation site, including the [Getting Started](https://www.flatcar.org/docs/latest/installing/) guide

This document is intended to consolidate the "why" in one place, complementing the existing "how" documentation.
