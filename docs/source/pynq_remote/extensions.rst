.. Copyright (C) 2026 Advanced Micro Devices, Inc.
.. SPDX-License-Identifier: BSD-3-Clause

Board-specific remote services
==============================

You can extend PYNQ.remote with gRPC services for your board or application.
The services run as native code on the board and are called from Python on the
host. Keep their protocol definitions, implementation and Python driver in the
board repository, then include them when building the remote image.

Native service registration
---------------------------

Create a directory containing your service sources, generated protobuf bindings
and a ``CMakeLists.txt``. The Remote server uses a factory function to create the
services when it starts. Include ``extensions.h`` and return the service objects
as ``pynq_remote::Services``:

.. code-block:: cpp

   #include "extensions.h"
   #include "my_service.h"

   pynq_remote::Services create_my_services()
   {
       pynq_remote::Services services;
       services.emplace_back(std::make_unique<MyService>());
       return services;
   }

In ``CMakeLists.txt``, build the service as a library and register the factory
with ``pynq_remote_add_extension``:

.. code-block:: cmake

   add_library(my_services STATIC my_service.cc my_service.pb.cc my_service.grpc.pb.cc)
   target_include_directories(my_services PRIVATE "${CMAKE_SOURCE_DIR}")
   target_link_libraries(my_services PUBLIC gRPC::grpc++ protobuf::libprotobuf)
   pynq_remote_add_extension(my_services create_my_services)

Pass the extension directory to CMake through ``PYNQ_REMOTE_EXTENSION_DIRS``.
To include several extensions, separate their paths with semicolons and give
each a unique factory, target and protobuf package name. A factory can return
several services, which remain owned by the server until it stops.

Board package integration
-------------------------

For EDF builds, place a ``pynq-cpp.bbappend`` in the board's
``edf_bsp/meta-remote`` layer. For example:

.. code-block:: bitbake

   FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
   SRC_URI:append = " file://my_service"
   DEPENDS:append = " my-native-library"
   EXTRA_OECMAKE:append = " -DPYNQ_REMOTE_EXTENSION_DIRS=${WORKDIR}/my_service"

Add the extension's dependencies to ``DEPENDS`` and any required build classes,
such as ``pkgconfig``, to the append file. If the sources live outside
``edf_bsp``, also list them in ``REMOTE_DEPENDS_<board>`` in the board
specification so sdbuild rebuilds the image when they change.

Install the generated Python bindings with your host board package. Its Python
driver can create a gRPC stub using the board's existing
``device.client.channel`` connection.

Overlay reconfiguration
-----------------------

If your service uses FPGA resources, it must release them before an overlay is
loaded and reconnect to them afterward. Inherit ``pynq_remote::OverlayLifecycle``
and implement ``prepare_overlay(firmware_name)`` to stop activity and release
drivers. The filename identifies the uploaded firmware under ``/lib/firmware``.
Return a failing gRPC status if the service cannot safely release its resources;
this prevents programming from starting.

Implement ``finish_overlay(loaded)`` to recover or rediscover the resources.
``loaded`` is true only when preparation and programming both succeeded. After
a failed programming attempt, the service must treat the FPGA state as unknown.

The server allows one programming operation at a time. It calls preparation in
registration order, then calls ``finish_overlay`` in reverse order for every
service whose preparation was entered, including one that failed. These
callbacks apply to both overlay downloads and firmware-manager writes.
