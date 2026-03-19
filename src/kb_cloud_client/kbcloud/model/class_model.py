# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict



@dataclass
class Class:
    """Class"""
    # Required fields
    engine: str
    mode: str
    class_type: str
    # Optional fields
    code: Optional[str] = None
    code_short: Optional[str] = None
    cpu: Optional[float] = None
    cpu_request: Optional[float] = None
    cpu_limit: Optional[float] = None
    memory: Optional[float] = None
    memory_request: Optional[float] = None
    memory_limit: Optional[float] = None
    component: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Class":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            engine=data.get("engine"),
            code=data.get("code"),
            code_short=data.get("codeShort"),
            mode=data.get("mode"),
            cpu=data.get("cpu"),
            cpu_request=data.get("cpuRequest"),
            cpu_limit=data.get("cpuLimit"),
            memory=data.get("memory"),
            memory_request=data.get("memoryRequest"),
            memory_limit=data.get("memoryLimit"),
            component=data.get("component"),
            class_type=data.get("classType"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.engine is not None:
            _v = self.engine
            result["engine"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.code is not None:
            _v = self.code
            result["code"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.code_short is not None:
            _v = self.code_short
            result["codeShort"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mode is not None:
            _v = self.mode
            result["mode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu is not None:
            _v = self.cpu
            result["cpu"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu_request is not None:
            _v = self.cpu_request
            result["cpuRequest"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu_limit is not None:
            _v = self.cpu_limit
            result["cpuLimit"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory is not None:
            _v = self.memory
            result["memory"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory_request is not None:
            _v = self.memory_request
            result["memoryRequest"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory_limit is not None:
            _v = self.memory_limit
            result["memoryLimit"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.class_type is not None:
            _v = self.class_type
            result["classType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
