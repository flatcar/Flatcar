# Flatcar Releases

Flatcar Container Linux uses **automatic, atomic updates** to keep your system secure and up-to-date without manual intervention. Each Flatcar instance receives updates from one of four release channels:

- **Alpha** — the bleeding edge. New features, major version upgrades, and experimental changes land here first. Expect frequent updates and occasional rough edges.
- **Beta** — a stabilization step. Changes that have proven themselves in Alpha are promoted here for broader testing before reaching production.
- **Stable** — the default and recommended channel for production workloads. Only thoroughly tested releases make it here.
- **LTS** — the gold standard for stability. An LTS release is cut from a battle-tested Stable version that has proven itself exceptionally reliable across the community. It receives only critical security and bug fix updates for **18 months**, with a new LTS published every 12 months and a 6-month overlap between consecutive LTS releases so you have plenty of time to upgrade. Ideal for environments where predictability and minimal change are paramount.

Each channel always points to its latest version as the `current` release. Every release has its own version number and dedicated release notes. Bug fixes are shipped directly to the affected channel — an Alpha fix goes to Alpha, a Beta fix to Beta, a Stable fix to Stable, and an LTS fix to LTS.

Within each channel, updates are planned on a **14-day cadence**. Major releases follow a broader rhythm:

| Promotion | Target cadence |
|-----------|----------------|
| New major **Alpha** | Monthly |
| Alpha → **Beta** | Every 2 months |
| Beta → **Stable** | Every 3–4 months |
| New **LTS** | Yearly |

You can learn more about switching between channels and configuring update behavior in the [channel docs](https://www.flatcar.org/docs/latest/setup/releases/switching-channels/).

## Download Images

Browse all available releases at [flatcar.org/releases](https://www.flatcar.org/releases/). Click `amd64` or `arm64` on the channel overview to download images for the `current` release, or navigate to a specific version's release notes to grab that particular build. You'll be able to choose from images for many platforms and cloud providers. The [installation docs](https://www.flatcar.org/docs/latest/installing/) have a quick start guide and information about public images directly available at each cloud provider.

## Track Releases

| Resource | Link |
|----------|------|
| **Releases Tracker** | [Project board](https://github.com/orgs/flatcar/projects/7/views/24) — status of each release across all channels |
| **Release issues** | [kind/release](https://github.com/flatcar/Flatcar/issues?q=is%3Aissue+state%3Aopen+label%3Akind%2Frelease) — upcoming and in-progress releases that populate the tracker |

## Release Process

For the full release process documentation — how releases are built, tested, signed, and published — see the [Release Guide](https://www.flatcar.org/docs/latest/reference/developer-guides/release-guide/) on the Flatcar documentation site.

Have questions about releases or updates? Join one of our [chats or community calls](https://github.com/flatcar/Flatcar/blob/main/README.md#communication-channels) — we're always happy to help!
