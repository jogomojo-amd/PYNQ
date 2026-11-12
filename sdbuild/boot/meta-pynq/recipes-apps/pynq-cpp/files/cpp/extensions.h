// Copyright (C) 2026 Advanced Micro Devices, Inc.
// SPDX-License-Identifier: BSD-3-Clause
#pragma once

#include <grpcpp/grpcpp.h>
#include <grpcpp/impl/service_type.h>
#include <memory>
#include <functional>
#include <string>
#include <vector>

namespace pynq_remote {
using Services = std::vector<std::unique_ptr<grpc::Service>>;
Services create_extension_services();

class OverlayLifecycle {
public:
    virtual ~OverlayLifecycle() = default;
    virtual grpc::Status prepare_overlay(const std::string& firmware_name) = 0;
    virtual grpc::Status finish_overlay(bool loaded) = 0;
};

grpc::Status program_overlay(const Services& services, const std::string& firmware_name,
                             const std::function<grpc::Status()>& program);
}
