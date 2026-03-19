# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .pgbench_step import PgbenchStep


@dataclass
class Pgbench:
    """pgbench is the pgbench benchmark object"""
    # Required fields
    cluster: str
    database: str
    username: str
    password: str
    address: str
    # Optional fields
    step: Optional[PgbenchStep] = None
    limit_cpu: Optional[str] = None
    limit_memory: Optional[str] = None
    request_cpu: Optional[str] = None
    request_memory: Optional[str] = None
    name: Optional[str] = None
    scale: Optional[int] = None
    clients: Optional[int] = None
    threads: Optional[int] = None
    duration: Optional[int] = None
    select_only: Optional[bool] = None
    extra_args: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Pgbench":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            step=PgbenchStep.from_dict(data.get("step")) if isinstance(data.get("step"), dict) else data.get("step"),
            limit_cpu=data.get("limitCpu"),
            limit_memory=data.get("limitMemory"),
            request_cpu=data.get("requestCpu"),
            request_memory=data.get("requestMemory"),
            name=data.get("name"),
            cluster=data.get("cluster"),
            database=data.get("database"),
            username=data.get("username"),
            password=data.get("password"),
            address=data.get("address"),
            scale=data.get("scale"),
            clients=data.get("clients"),
            threads=data.get("threads"),
            duration=data.get("duration"),
            select_only=data.get("selectOnly"),
            extra_args=data.get("extraArgs"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.step is not None:
            _v = self.step
            result["step"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.limit_cpu is not None:
            _v = self.limit_cpu
            result["limitCpu"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.limit_memory is not None:
            _v = self.limit_memory
            result["limitMemory"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.request_cpu is not None:
            _v = self.request_cpu
            result["requestCpu"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.request_memory is not None:
            _v = self.request_memory
            result["requestMemory"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster is not None:
            _v = self.cluster
            result["cluster"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.database is not None:
            _v = self.database
            result["database"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.username is not None:
            _v = self.username
            result["username"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.password is not None:
            _v = self.password
            result["password"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.address is not None:
            _v = self.address
            result["address"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.scale is not None:
            _v = self.scale
            result["scale"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.clients is not None:
            _v = self.clients
            result["clients"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.threads is not None:
            _v = self.threads
            result["threads"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.duration is not None:
            _v = self.duration
            result["duration"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.select_only is not None:
            _v = self.select_only
            result["selectOnly"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extra_args is not None:
            _v = self.extra_args
            result["extraArgs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
