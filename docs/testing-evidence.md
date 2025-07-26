# Evidence of Test Policy Adherence

This document provides evidence that tests were added for major functionality in recent Flatcar releases, as required by the OpenSSF Best Practices Badge.

---

## Example: Version 3888.0.0

**Feature:** Updated Ignition support  
- Feature PR: #1785  
- Test PR: #1787  
- Test File: `tests/ignition/ignition_test.go`

---

## Example: Version 3815.2.1

**Feature:** Added Containerd v1.7 support  
- Feature PR: #1750  
- Test added in the same PR

---

## Version: 4152.2.1

**Feature:** Added new image signing public key to flatcar-install for release verification  
- Feature PR: `init#92`  
- Expected Test Evidence: Check whether unit or integration tests were added in either the same PR or a follow-up PR (e.g., init-related tests covering validation of signing key logic)

**Feature:** Changed kernel configuration (e.g., `CONFIG_WIREGUARD` module, disabled unsupported ARM64 arch-specific kernel options)  
- PR: `coreos-overlay#2239`  
- Expected Test Evidence: Confirm whether tests were added to validate boot image size, wireguard module, and edge workloads

**Feature:** Ignition behavior change — specifying OEM filesystem to `/usr/share/oem` no longer required  
- PR: `bootengine#58`  
- Expected Test Evidence: Look for test files covering Ignition parsing or boot behavior regression
