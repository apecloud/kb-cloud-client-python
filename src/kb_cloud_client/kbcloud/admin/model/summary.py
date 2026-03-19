# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict



@dataclass
class Summary:
    """Summary"""
    # Required fields
    # Optional fields
    namespace: Optional[str] = None
    name: Optional[str] = None
    cpu_requests: Optional[str] = None
    cpu_limits: Optional[str] = None
    memory_requests: Optional[str] = None
    memory_limits: Optional[str] = None
    storage_size: Optional[str] = None
    replicas: Optional[int] = None
    backup_endpoint: Optional[str] = None
    backup_path: Optional[str] = None
    backup_schedule: Optional[str] = None
    status: Optional[str] = None
    creation_time: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Summary":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            namespace=data.get("namespace"),
            name=data.get("name"),
            cpu_requests=data.get("cpuRequests"),
            cpu_limits=data.get("cpuLimits"),
            memory_requests=data.get("memoryRequests"),
            memory_limits=data.get("memoryLimits"),
            storage_size=data.get("storageSize"),
            replicas=data.get("replicas"),
            backup_endpoint=data.get("backupEndpoint"),
            backup_path=data.get("backupPath"),
            backup_schedule=data.get("backupSchedule"),
            status=data.get("status"),
            creation_time=data.get("creationTime"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.namespace is not None:
            _v = self.namespace
            result["namespace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu_requests is not None:
            _v = self.cpu_requests
            result["cpuRequests"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu_limits is not None:
            _v = self.cpu_limits
            result["cpuLimits"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory_requests is not None:
            _v = self.memory_requests
            result["memoryRequests"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory_limits is not None:
            _v = self.memory_limits
            result["memoryLimits"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.storage_size is not None:
            _v = self.storage_size
            result["storageSize"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replicas is not None:
            _v = self.replicas
            result["replicas"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_endpoint is not None:
            _v = self.backup_endpoint
            result["backupEndpoint"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_path is not None:
            _v = self.backup_path
            result["backupPath"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_schedule is not None:
            _v = self.backup_schedule
            result["backupSchedule"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.creation_time is not None:
            _v = self.creation_time
            result["creationTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
