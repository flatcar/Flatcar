# Flatcar inter-operation matrix

This document tracks Flatcar inter-operability across environments.

Support levels:
* L1: All features supported & covered in release tests
* L2: Supported & covered in release tests
* L3: supported  but no regular tests
* L4: supported with documented caveats

Ownership of an item implies ensuring test coverage in release tests of official Flatcar releases (L2 and above) as well as handling bugs and feature requests that affect the respective environment specifically.
Please propose ownership by filing a PR for this document.

## Public cloud (machines)

| Environment | Support level | Owner | Reference (e.g. GH issue) | Notes |
|-------------|---------------|-------|---------------------------|-------|
| EC2 | L2 | @kinvolk/flatcar-maintainers | #107 | EC2 vendor tools not fully supported (e.g. SSM agent for run-command);  IAM 2.0 support missing |
| Azure | L2 | @kinvolk/flatcar-maintainers |  | HyperV telemetry support missing; needs tracking issue |
| GCE | L1 | @kinvolk/flatcar-maintainers |  |  |
| Digital Ocean (VMs) | L1 | @kinvolk/flatcar-maintainers |  |  |
| Equinix Metal | L1 | @kinvolk/flatcar-maintainers |  |  |
| ESXi / vSphere | L1 | @kinvolk/flatcar-maintainers |  |  |
| Hetzner Cloud | L3 | [no owner] |  |  |
| Vultr VPS  | L3 | [no owner] |  |  |
| Cloudscale | L3 | [no owner] |  |  |
| Oracle Cloud | L3 / L4 | [no owner] |  | Bring-your-own-image on OCI VMs |  install via Ubuntu on OCI bare metal |
| Tencent | x | [no owner] |  |  |
| AliCloud | x | [no owner] |  |  |
| Yandex | ? | [no owner] |  |  |

## Private Cloud (machines)

| Environment | Support level | Owner | Reference (e.g. GH issue) | Notes |
|-------------|---------------|-------|---------------------------|-------|
| Azure Stack | L4 | [no owner] |  | |
| Tinkerbell | L3 | [no owner] |  | |
| Rancher (VMs) | L3 | [no owner] |  | |
| QEmu / KVM backed | L1 | @kinvolk/flatcar-maintainers |  | |
| OpenStack | L3 ? | [no owner] |  | https://docs.openstack.org/image-guide/obtain-images.html |
| VirtualBox | L3 | [no owner] |  |  |
| Vagrant | L3 | [no owner] |  | Isn't this plain qemu/kvm? |

## Public cloud (k8s)

| Environment | Support level | Owner | Reference (e.g. GH issue) | Notes |
|-------------|---------------|-------|---------------------------|-------|
| EKS | L2 | [no owner] |  |  |
| AKS Engine | L4 | [no owner] |  | https://kinvolk.io/blog/2020/12/supercharging-aks-engine-with-flatcar-container-linux/ |
| GiantSwarm | L1 | Provider |  |  |

## Cluster API

| Environment | Support level | Owner | Reference (e.g. GH issue) | Notes |
|-------------|---------------|-------|---------------------------|-------|
| CAPB | L1 | Upstream |  | Covered by CAPB release tests |
| CAPA | L1 | Upstream |  | Covered by CAPI release tests |
| CAPA EKS | x | [no owner] |  |  |
| CAPZ | L4 | @kinvolk/flatcar-maintainers |  | WIP Prototype |
| CAPV | x | [no owner] |  |  |
| CAPM3 | x | [no owner] |  |  |
| CAPG | x | [no owner] |  |  |

## k8s Distros

| Environment | Support level | Owner | Reference (e.g. GH issue) | Notes |
|-------------|---------------|-------|---------------------------|-------|
| Rancher (rke) | L3 | [no owner] |  |  |
| Rancher (rke2) | ? | [no owner] |  |  |
| Lokomotive | L1 | @kinvolk/lokomotive-developers |  |  |
| Tanzu KG | L3 ? | [no owner] |  |  |
| K3s | L3 | [no owner] |  |  |
| EKS-Distro | L3 | [no owner] |  |  |
| KOPS | L3 | Upstream |  |  |
| Kubematic | L3 | [no owner] |  |  |
| Gardener | L3 | [no owner] |  |  |

## Other


| Environment | Support level | Owner | Reference (e.g. GH issue) | Notes |
|-------------|---------------|-------|---------------------------|-------|
| COSI        | x             | [no owner] |                      |       |
