# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cpu import CPU
from .data_disk import DataDisk
from .log_disk import LogDisk
from .memory import Memory


@dataclass
class Tenant:
    """Tenant"""
    # Required fields
    # Optional fields
    id_: Optional[str] = None
    name: Optional[str] = None
    mode: Optional[str] = None
    create_at: Optional[str] = None
    role: Optional[str] = None
    primary_zone: Optional[str] = None
    status: Optional[str] = None
    primary_zone_proxy: Optional[str] = None
    chart_set: Optional[str] = None
    resource: Optional[str] = None
    cpu: Optional[CPU] = None
    memory: Optional[Memory] = None
    log_disk: Optional[LogDisk] = None
    data_disk: Optional[DataDisk] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Tenant":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            name=data.get("name"),
            mode=data.get("mode"),
            create_at=data.get("create_at"),
            role=data.get("role"),
            primary_zone=data.get("primary_zone"),
            status=data.get("status"),
            primary_zone_proxy=data.get("primary_zone_proxy"),
            chart_set=data.get("chart_set"),
            resource=data.get("resource"),
            cpu=CPU.from_dict(data.get("cpu")) if isinstance(data.get("cpu"), dict) else data.get("cpu"),
            memory=Memory.from_dict(data.get("memory")) if isinstance(data.get("memory"), dict) else data.get("memory"),
            log_disk=LogDisk.from_dict(data.get("log_disk")) if isinstance(data.get("log_disk"), dict) else data.get("log_disk"),
            data_disk=DataDisk.from_dict(data.get("data_disk")) if isinstance(data.get("data_disk"), dict) else data.get("data_disk"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mode is not None:
            _v = self.mode
            result["mode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.create_at is not None:
            _v = self.create_at
            result["create_at"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.role is not None:
            _v = self.role
            result["role"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.primary_zone is not None:
            _v = self.primary_zone
            result["primary_zone"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.primary_zone_proxy is not None:
            _v = self.primary_zone_proxy
            result["primary_zone_proxy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.chart_set is not None:
            _v = self.chart_set
            result["chart_set"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.resource is not None:
            _v = self.resource
            result["resource"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu is not None:
            _v = self.cpu
            result["cpu"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory is not None:
            _v = self.memory
            result["memory"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.log_disk is not None:
            _v = self.log_disk
            result["log_disk"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.data_disk is not None:
            _v = self.data_disk
            result["data_disk"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
