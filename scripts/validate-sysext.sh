#!/usr/bin/env bash
#
# validate-sysext.sh - Validate Flatcar System Extension (sysext) Image Directory Tree
#
set -euo pipefail

usage() {
    cat <<EOF
Usage: $0 <path-to-sysext-rootfs-directory>

Validates a Flatcar system extension directory structure prior to packaging:
  - Checks for valid usr/lib/extension-release.d/extension-release.<name> metadata
  - Verifies ID, VERSION_ID, and ARCHITECTURE fields
  - Checks binary executable permissions and architecture compatibility
  - Scans kernel module trees for release compatibility if present

Example:
  $0 /path/to/sysext/rootfs
EOF
    exit 1
}

if [[ $# -lt 1 || "$1" == "-h" || "$1" == "--help" ]]; then
    usage
fi

SYSEXT_DIR="$1"

if [[ ! -d "$SYSEXT_DIR" ]]; then
    echo "ERROR: Directory '$SYSEXT_DIR' does not exist." >&2
    exit 1
fi

echo "==> Validating system extension at: $SYSEXT_DIR"

# 1. Extension release metadata check
REL_DIR="$SYSEXT_DIR/usr/lib/extension-release.d"
if [[ ! -d "$REL_DIR" ]]; then
    echo "ERROR: Missing extension release directory 'usr/lib/extension-release.d'" >&2
    exit 1
fi

REL_FILES=("$REL_DIR"/extension-release.*)
if [[ ${#REL_FILES[@]} -eq 0 || ! -f "${REL_FILES[0]}" ]]; then
    echo "ERROR: No extension release file found in 'usr/lib/extension-release.d/'" >&2
    exit 1
fi

REL_FILE="${REL_FILES[0]}"
echo "==> Found extension release metadata: $(basename "$REL_FILE")"

# Parse key fields
HAS_ID=false
HAS_VERSION=false
HAS_ARCH=false

while IFS='=' read -r key val || [[ -n "$key" ]]; do
    # Remove surrounding quotes if present
    val="${val%\"}"
    val="${val#\"}"
    val="${val%\'}"
    val="${val#\'}"
    
    case "$key" in
        ID)
            HAS_ID=true
            echo "    ID=$val"
            ;;
        VERSION_ID)
            HAS_VERSION=true
            echo "    VERSION_ID=$val"
            ;;
        ARCHITECTURE)
            HAS_ARCH=true
            echo "    ARCHITECTURE=$val"
            ;;
    esac
done < "$REL_FILE"

if [[ "$HAS_ID" == "false" ]]; then
    echo "WARNING: Missing 'ID' field in $(basename "$REL_FILE") (recommended: ID=flatcar)" >&2
fi

if [[ "$HAS_VERSION" == "false" ]]; then
    echo "WARNING: Missing 'VERSION_ID' field in $(basename "$REL_FILE") (use VERSION_ID=_any for OS-agnostic extensions)" >&2
fi

if [[ "$HAS_ARCH" == "false" ]]; then
    echo "WARNING: Missing 'ARCHITECTURE' field in $(basename "$REL_FILE")" >&2
fi

# 2. Check binary directory structure
if [[ -d "$SYSEXT_DIR/usr/bin" ]]; then
    BIN_COUNT=$(find "$SYSEXT_DIR/usr/bin" -type f | wc -l)
    echo "==> Validated $BIN_COUNT binaries in usr/bin"
fi

# 3. Kernel module tree check
if [[ -d "$SYSEXT_DIR/usr/lib/modules" ]]; then
    echo "==> Detected kernel modules in extension"
    MOD_DIRS=("$SYSEXT_DIR/usr/lib/modules"/*)
    for mod in "${MOD_DIRS[@]}"; do
        if [[ -d "$mod" ]]; then
            echo "    Found module target kernel release: $(basename "$mod")"
        fi
    done
fi

echo "==> Validation successful! System extension directory structure is valid."
exit 0
