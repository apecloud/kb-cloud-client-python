# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .ycsb_redis_mode import YcsbRedisMode
from .ycsb_step import YcsbStep


@dataclass
class Ycsb:
    """ycsb is the ycsb benchmark object"""
    # Required fields
    cluster: str
    username: str
    password: str
    address: str
    # Optional fields
    step: Optional[YcsbStep] = None
    limit_cpu: Optional[str] = None
    limit_memory: Optional[str] = None
    request_cpu: Optional[str] = None
    request_memory: Optional[str] = None
    name: Optional[str] = None
    database: Optional[str] = None
    record_count: Optional[int] = None
    operation_count: Optional[int] = None
    read_proportion: Optional[int] = None
    update_proportion: Optional[int] = None
    insert_proportion: Optional[int] = None
    read_modify_write_proportion: Optional[int] = None
    scan_proportion: Optional[int] = None
    threads: Optional[int] = None
    extra_args: Optional[str] = None
    redis_mode: Optional[YcsbRedisMode] = None
    redis_sentinel_master: Optional[str] = None
    redis_sentinel_username: Optional[str] = None
    redis_sentinel_password: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Ycsb":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            step=YcsbStep.from_dict(data.get("step")) if isinstance(data.get("step"), dict) else data.get("step"),
            limit_cpu=data.get("limitCpu"),
            limit_memory=data.get("limitMemory"),
            request_cpu=data.get("requestCpu"),
            request_memory=data.get("requestMemory"),
            name=data.get("name"),
            database=data.get("database"),
            cluster=data.get("cluster"),
            username=data.get("username"),
            password=data.get("password"),
            address=data.get("address"),
            record_count=data.get("recordCount"),
            operation_count=data.get("operationCount"),
            read_proportion=data.get("readProportion"),
            update_proportion=data.get("updateProportion"),
            insert_proportion=data.get("insertProportion"),
            read_modify_write_proportion=data.get("readModifyWriteProportion"),
            scan_proportion=data.get("scanProportion"),
            threads=data.get("threads"),
            extra_args=data.get("extraArgs"),
            redis_mode=YcsbRedisMode.from_dict(data.get("redisMode")) if isinstance(data.get("redisMode"), dict) else data.get("redisMode"),
            redis_sentinel_master=data.get("redisSentinelMaster"),
            redis_sentinel_username=data.get("redisSentinelUsername"),
            redis_sentinel_password=data.get("redisSentinelPassword"),
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
        if self.database is not None:
            _v = self.database
            result["database"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster is not None:
            _v = self.cluster
            result["cluster"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.record_count is not None:
            _v = self.record_count
            result["recordCount"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.operation_count is not None:
            _v = self.operation_count
            result["operationCount"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.read_proportion is not None:
            _v = self.read_proportion
            result["readProportion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.update_proportion is not None:
            _v = self.update_proportion
            result["updateProportion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.insert_proportion is not None:
            _v = self.insert_proportion
            result["insertProportion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.read_modify_write_proportion is not None:
            _v = self.read_modify_write_proportion
            result["readModifyWriteProportion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.scan_proportion is not None:
            _v = self.scan_proportion
            result["scanProportion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.threads is not None:
            _v = self.threads
            result["threads"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extra_args is not None:
            _v = self.extra_args
            result["extraArgs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.redis_mode is not None:
            _v = self.redis_mode
            result["redisMode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.redis_sentinel_master is not None:
            _v = self.redis_sentinel_master
            result["redisSentinelMaster"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.redis_sentinel_username is not None:
            _v = self.redis_sentinel_username
            result["redisSentinelUsername"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.redis_sentinel_password is not None:
            _v = self.redis_sentinel_password
            result["redisSentinelPassword"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
