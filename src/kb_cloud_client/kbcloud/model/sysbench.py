# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .sysbench_step import SysbenchStep
from .sysbench_test_type import SysbenchTestType


@dataclass
class Sysbench:
    """sysbench is the sysbench benchmark object"""
    # Required fields
    cluster: str
    database: str
    username: str
    password: str
    address: str
    # Optional fields
    step: Optional[SysbenchStep] = None
    limit_cpu: Optional[str] = None
    limit_memory: Optional[str] = None
    request_cpu: Optional[str] = None
    request_memory: Optional[str] = None
    name: Optional[str] = None
    threads: Optional[int] = None
    duration: Optional[int] = None
    table_size: Optional[int] = None
    table_num: Optional[int] = None
    test_type: Optional[SysbenchTestType] = None
    read_percent: Optional[int] = None
    write_percent: Optional[int] = None
    extra_args: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Sysbench":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            step=SysbenchStep.from_dict(data.get("step")) if isinstance(data.get("step"), dict) else data.get("step"),
            limit_cpu=data.get("limitCpu"),
            limit_memory=data.get("limitMemory"),
            request_cpu=data.get("requestCpu"),
            request_memory=data.get("requestMemory"),
            name=data.get("name"),
            cluster=data.get("cluster"),
            database=data.get("database"),
            threads=data.get("threads"),
            duration=data.get("duration"),
            table_size=data.get("tableSize"),
            table_num=data.get("tableNum"),
            test_type=SysbenchTestType.from_dict(data.get("testType")) if isinstance(data.get("testType"), dict) else data.get("testType"),
            read_percent=data.get("readPercent"),
            write_percent=data.get("writePercent"),
            username=data.get("username"),
            password=data.get("password"),
            address=data.get("address"),
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
        if self.table_size is not None:
            _v = self.table_size
            result["tableSize"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.table_num is not None:
            _v = self.table_num
            result["tableNum"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.test_type is not None:
            _v = self.test_type
            result["testType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.read_percent is not None:
            _v = self.read_percent
            result["readPercent"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.write_percent is not None:
            _v = self.write_percent
            result["writePercent"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.extra_args is not None:
            _v = self.extra_args
            result["extraArgs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
