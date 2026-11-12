# Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause
FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
COMPATIBLE_HOST:arm = ".*"
DEPENDS:remove:arm = "libdfx"
EXTRA_OECMAKE:remove:arm = "-DXRT_LIBDFX=true"
PACKAGECONFIG:remove:arm = "aie"
SRC_URI:append:arm = " file://0001-arm32-build.patch;striplevel=2"

# Keep the native runtime available without command-line tools and examples.
PACKAGES =+ "${PN}-runtime"
FILES:${PN}-runtime = "${libdir}/libxrt_core.so* ${libdir}/libxrt_coreutil.so*"
INSANE_SKIP:${PN}-runtime += "dev-so"
RDEPENDS:${PN}-runtime = "zocl (= ${PV})"
RDEPENDS:${PN} += "${PN}-runtime"
