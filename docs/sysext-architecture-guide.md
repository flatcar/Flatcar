# Flatcar System Extension (sysext/confext) Architecture & Lifecycle Guide

This document defines the architectural standards, lifecycle state machine, and security guidelines for `systemd-sysext` and `systemd-confext` integration in Flatcar Container Linux.

---

## 1. Overview & Architecture

Flatcar Container Linux uses immutable root filesystems (`/usr` mounted read-only). `systemd-sysext` and `systemd-confext` allow extenders (such as container runtimes, OEM tools, Kubernetes binaries, and kernel driver modules) to be layered dynamically over `/usr` and `/etc` without mutating the underlying OS image.

```
       +-------------------------------------------------------+
       |                  Merged /usr View                     |
       +-------------------------------------------------------+
       | Overlay lowerdir:                                     |
       |  1. Extension image (e.g. /var/lib/extensions/docker) |
       |  2. Immutable Base OS /usr                            |
       +-------------------------------------------------------+
```

---

## 2. Extension Release Compatibility Matrix

Every system extension MUST contain an extension release file under:
`usr/lib/extension-release.d/extension-release.<name>`

### Metadata Fields
```ini
ID=flatcar
VERSION_ID=_any
ARCHITECTURE=x86-64
```

### Compatibility Rules Across A/B OS Updates
1. **OS ID Match**: `ID=flatcar` (or `ID=alpha`, `ID=beta`, `ID=stable` where permitted).
2. **Flexible Version Matching**: Use `VERSION_ID=_any` for OS-agnostic binaries (static binaries, standalone tools). For OS-version bound extensions (glibc or kernel dependent), specify target minor releases or rely on Flatcar's sysext bakery automated build matrix.
3. **Architecture Match**: `ARCHITECTURE` MUST match `uname -m` (e.g. `x86-64` or `arm64`).

---

## 3. Safe Atomic Extension Refresh Workflow

To prevent service disruption or race conditions during runtime extension updates (`systemd-sysext refresh`), system services MUST follow this atomic sequence:

```
  +-------------------+
  | 1. Mask Services  |  Prevent systemd from spawning processes during reload
  +---------+---------+
            |
            v
  +-------------------+
  | 2. Sysext Refresh |  Execute `systemd-sysext refresh`
  +---------+---------+
            |
            v
  +-------------------+
  | 3. Daemon Reload  |  Execute `systemctl daemon-reload`
  +---------+---------+
            |
            v
  +-------------------+
  | 4. Unmask & Start |  Restore service availability
  +-------------------+
```

---

## 4. SELinux Extended Attribute (`security.selinux`) Propagation

When SELinux is active in enforcing mode:

1. Executable files within sysext images MUST be labeled with valid SELinux security contexts (e.g. `system_u:object_r:bin_t:s0`).
2. When mounting custom raw or squashfs sysext images, ensure extended attributes (`xattr`) are preserved during build time.
3. Post-merge, if new binaries are introduced, trigger targeted context restoration:
   ```bash
   restorecon -R /usr/bin /usr/sbin
   ```

---

## 5. Kernel Module Extension Verification

Driver extensions containing out-of-tree kernel modules (`usr/lib/modules/$(uname -r)`) MUST comply with the following verification rules:

1. **Kernel Release Match**: Modules must match `uname -r` exactly.
2. **`vermagic` Verification**: Module `vermagic` strings must align with the active running kernel release to avoid module loading failures or kernel panic.
3. **Pre-mount Check**: Use `scripts/validate-sysext.sh` during image preparation to catch ABI mismatches before deployment.

---

## 6. Verification Tooling

Flatcar provides a dedicated validation script to check sysext image directory trees prior to packaging:

```bash
bash scripts/validate-sysext.sh /path/to/extension/rootfs
```
