// Copyright (C) 2026 Advanced Micro Devices, Inc.
// SPDX-License-Identifier: BSD-3-Clause
#include "extensions.h"
#include <mutex>

namespace pynq_remote {
namespace {
template<typename Function>
grpc::Status call_status(Function&& function) {
    try { return function(); }
    catch (const std::exception& error) {
        return {grpc::StatusCode::FAILED_PRECONDITION, error.what()};
    }
}
}

grpc::Status program_overlay(const Services& services, const std::string& firmware_name,
                             const std::function<grpc::Status()>& program) {
    static std::mutex programming_mutex;
    std::lock_guard<std::mutex> lock(programming_mutex);
    std::vector<OverlayLifecycle*> prepared;
    grpc::Status result;
    for (const auto& service : services) {
        auto lifecycle = dynamic_cast<OverlayLifecycle*>(service.get());
        if (!lifecycle) continue;
        prepared.push_back(lifecycle);
        result = call_status([&] { return lifecycle->prepare_overlay(firmware_name); });
        if (!result.ok()) break;
    }
    const bool loaded = result.ok() && (result = call_status(program)).ok();
    for (auto item = prepared.rbegin(); item != prepared.rend(); ++item) {
        auto status = call_status([&] { return (*item)->finish_overlay(loaded); });
        if (!status.ok()) {
            result = result.ok() ? status : grpc::Status(result.error_code(),
                result.error_message() + "; overlay cleanup: " + status.error_message(),
                result.error_details());
        }
    }
    return result;
}
}
