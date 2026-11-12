#!/usr/bin/env bash
# Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause
pynq_add_board_layer() {
BOARD_REMOTE_LAYER="${BOARD_PATH}/edf_bsp/meta-remote"
while read -r _name _path _prio; do
    case "${_path}" in
        */edf_bsp/meta-remote)
            [ "${_path}" = "${BOARD_REMOTE_LAYER}" ] || \
                bitbake-layers remove-layer "${_path}" >/dev/null 2>&1 || true
            ;;
    esac
done < <(bitbake-layers show-layers 2>/dev/null)
if [ -d "${BOARD_REMOTE_LAYER}" ] && \
   ! bitbake-layers show-layers 2>/dev/null | grep -q "${BOARD_REMOTE_LAYER}"; then
    bitbake-layers add-layer "${BOARD_REMOTE_LAYER}"
fi

}
