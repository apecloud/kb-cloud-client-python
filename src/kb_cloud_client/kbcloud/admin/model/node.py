# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .node_status import NodeStatus
from .resource_stats import ResourceStats


@dataclass
class Node:
    """node info"""
    # Required fields
    created_at: datetime
    host_name: str
    ip: str
    status: NodeStatus
    # Optional fields
    cpu: Optional[int] = None
    cpu_stats: Optional[ResourceStats] = None
    instance_type: Optional[str] = None
    memory: Optional[int] = None
    memory_stats: Optional[ResourceStats] = None
    zone: Optional[str] = None
    region: Optional[str] = None
    node_group: Optional[str] = None
    control_plane: Optional[bool] = None
    data_plane: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Node":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            cpu=data.get("cpu"),
            cpu_stats=ResourceStats.from_dict(data.get("cpuStats")) if isinstance(data.get("cpuStats"), dict) else data.get("cpuStats"),
            created_at=_parse_datetime(data.get("createdAt")),
            host_name=data.get("hostName"),
            instance_type=data.get("instanceType"),
            ip=data.get("ip"),
            memory=data.get("memory"),
            memory_stats=ResourceStats.from_dict(data.get("memoryStats")) if isinstance(data.get("memoryStats"), dict) else data.get("memoryStats"),
            zone=data.get("zone"),
            region=data.get("region"),
            node_group=data.get("nodeGroup"),
            control_plane=data.get("controlPlane"),
            data_plane=data.get("dataPlane"),
            status=NodeStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.cpu is not None:
            _v = self.cpu
            result["cpu"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu_stats is not None:
            _v = self.cpu_stats
            result["cpuStats"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.host_name is not None:
            _v = self.host_name
            result["hostName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.instance_type is not None:
            _v = self.instance_type
            result["instanceType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.ip is not None:
            _v = self.ip
            result["ip"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory is not None:
            _v = self.memory
            result["memory"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory_stats is not None:
            _v = self.memory_stats
            result["memoryStats"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.zone is not None:
            _v = self.zone
            result["zone"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.region is not None:
            _v = self.region
            result["region"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.node_group is not None:
            _v = self.node_group
            result["nodeGroup"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.control_plane is not None:
            _v = self.control_plane
            result["controlPlane"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.data_plane is not None:
            _v = self.data_plane
            result["dataPlane"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
