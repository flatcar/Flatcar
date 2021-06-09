# Flatcar inter-operation matrix

This document tracks Flatcar inter-operability across environments.

Ownership of an item implies ensuring test coverage in release tests of official Flatcar releases (L2 and above) as well as handling bugs and feature requests that affect the respective environment specifically.
Please propose ownership by filing a PR for this document.

## Public cloud (machines)

| Environment | Full-Feature (release blocker) | Works | Tested (CI) | Owner | Reference (e.g. GH issue) | Notes |
|-------------|--------------------------------|-------|-------------|-------|---------------------------|-------|
| EC2         |           Partial              |   X   |      X      | @kinvolk/flatcar-maintainers | [#107](https://github.com/kinvolk/Flatcar/issues/107) | EC2 vendor tools not fully supported (e.g. SSM agent for run-command);  IAM 2.0 support missing |
| Azure       |           Partial              |   X   |      X      | @kinvolk/flatcar-maintainers |    | HyperV telemetry support missing; needs tracking issue |
| GCE         |               X                |   X   |      X      | @kinvolk/flatcar-maintainers |    |       |
| Digital Ocean (VMs) |       X                |   X   |      X      | @kinvolk/flatcar-maintainers |    |       |
| Equinix Metal |             X                |   X   |      X      | @kinvolk/flatcar-maintainers |    |       |
| ESXi / vSphere |            X                |   X   |      X      | @kinvolk/flatcar-maintainers |    |       |
| Hetzner Cloud |                              |   X   |             | [no owner] |                      |       |
| Vultr VPS  |                                 |   X   |             | [no owner] |                      |       |
| Cloudscale |                                 |   X   |             | [no owner] |                      |       |
| Oracle Cloud |                               |   X   |             | [no owner] |                      | Bring-your-own-image on OCI VMs; install via Ubuntu on OCI bare metal |
| Tencent |                                    |       |             | [no owner] |                      |       |
| AliCloud |                                   |       |             | [no owner] |                      |       |
| Yandex |                                     |       |             | [no owner] |                      |       |

## Private Cloud (machines)

| Environment | Full-Feature (release blocker) | Works | Tested (CI) | Owner | Reference (e.g. GH issue) | Notes |
|-------------|--------------------------------|-------|-------------|-------|---------------------------|-------|
| Azure Stack |                                | w/ caveat |         | [no owner] |                      | controller node not supported on Flatcar (cloud-init feature missing) |
| Tinkerbell  |                                |   X   |             | [no owner] |                      |       |
| Rancher (VMs) |                              |   X   |             | [no owner] |                      |       |
| QEmu / KVM backed |         X                |   X   |      X      | @kinvolk/flatcar-maintainers |    |       |
| OpenStack |                                  |   X   |             | [no owner] |                      | https://docs.openstack.org/image-guide/obtain-images.html |
| VirtualBox |                                 |   X   |             | [no owner] |                      |       |
| Vagrant |                                    |   X   |             | [no owner] |                      | Isn't this plain qemu/kvm? |

## Managed Kubernetes

| Environment | Full-Feature (release blocker) | Works | Tested (CI) | Owner | Reference (e.g. GH issue) | Notes |
|-------------|--------------------------------|-------|-------------|-------|---------------------------|-------|
| EKS         |                                |   X   |             | [no owner] |                      |       |
| GiantSwarm  |                                |   X   |             | Provider |                        |       |

## Cluster API

| Environment | Full-Feature (release blocker) | Works | Tested (CI) | Owner | Reference (e.g. GH issue) | Notes |
|-------------|--------------------------------|-------|-------------|-------|---------------------------|-------|
| CAPB        |              X                 |   X   |  X (upstream) | Upstream |                      | Covered by CAPB release tests |
| CAPA        |              X                 |   X   |  X (upstream) | Upstream |                      | Covered by CAPA release tests |
| CAPA EKS    |                                |       |             | [no owner] |                      |       |
| CAPZ        |                                |   w/ caveat |       | @kinvolk/flatcar-maintainers |  | WIP Prototype |
| CAPV        |                                | [no owner] |        |                                   |       |
| CAPM3       |                                | [no owner] |        |                                   |       |
| CAPG        |                                | [no owner] |        |                                   |       |

## Kubernetes Distros

| Environment | Full-Feature (release blocker) | Works | Tested (CI) | Owner | Reference (e.g. GH issue) | Notes |
|-------------|--------------------------------|-------|-------------|-------|---------------------------|-------|
| AKS Engine  |                                |   X   |             | [no owner] |                      | https://kinvolk.io/blog/2020/12/supercharging-aks-engine-with-flatcar-container-linux/ |
| Rancher (rke) |                              |   X   |             | [no owner] |                      |       |
| Rancher (rke2) |                             |       |             | [no owner] |                      |       |
| Lokomotive |                X                |   X   |      X      | @kinvolk/lokomotive-developers |  |       |
| Tanzu KG |                                   |   X   |             | [no owner] |                      |       |
| K3s |                                        |   X   |             | [no owner] |                      |       |
| EKS-Distro |                                 |   X   |             | [no owner] |                      |       |
| KOPS |                                       |   X   |             | upstream |                        |       |
| Kubematic |                                  |   X   |             | [no owner] |                      |       |
| Gardener |                                   |   X   |             | [no owner] |                      |       |

## Other

Please add below what does not fit into any of the categories above.

| Environment | Full-Feature (release blocker) | Works | Tested (CI) | Owner | Reference (e.g. GH issue) | Notes |
|-------------|--------------------------------|-------|-------------|-------|---------------------------|-------|
|             |                                |       |             |       |                           |       |
