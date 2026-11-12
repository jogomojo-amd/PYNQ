#!/usr/bin/env bash
# Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause
set -euo pipefail

ROOTFS_TAR="$(realpath "${ROOTFS_TAR:?Set ROOTFS_TAR}")"
OUT_RAMDISK="$(realpath -m "${OUT_RAMDISK:?Set OUT_RAMDISK}")"
for tool in fakeroot tar cpio gzip; do
    command -v "${tool}" >/dev/null || { echo "Missing ${tool}" >&2; exit 1; }
done
mkdir -p "$(dirname "${OUT_RAMDISK}")"
staging=$(mktemp -d)
temporary=$(mktemp "${OUT_RAMDISK}.XXXXXX")
trap 'rm -rf "${staging}"; rm -f "${temporary}"' EXIT
export ROOTFS_TAR staging temporary
fakeroot bash -euo pipefail <<'EOF'
tar --numeric-owner -xpf "${ROOTFS_TAR}" -C "${staging}"
cd "${staging}"
if [ ! -e init ] && [ ! -L init ]; then
    [ -e sbin/init ] || [ -L sbin/init ] || { echo "Rootfs has no init" >&2; exit 1; }
    ln -s sbin/init init
fi
# A RAM root has no block device to grow.
if [ -e usr/lib/systemd/system/systemd-growfs-root.service ] || [ -e lib/systemd/system/systemd-growfs-root.service ]; then
    mkdir -p etc/systemd/system
    ln -sfn /dev/null etc/systemd/system/systemd-growfs-root.service
fi
find . -print0 | LC_ALL=C sort -z | cpio --null -o --format=newc --reproducible | gzip -n -9 > "${temporary}"
EOF
mv "${temporary}" "${OUT_RAMDISK}"
