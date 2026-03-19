# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .log_entry import LogEntry


@dataclass
class EnvironmentModuleLogs:
    """Environment module pod logs"""
    # Required fields
    # Optional fields
    environment_id: Optional[str] = None
    module_name: Optional[str] = None
    pod_name: Optional[str] = None
    container_name: Optional[str] = None
    logs: Optional[List[LogEntry]] = None
    next_timestamp: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EnvironmentModuleLogs":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            environment_id=data.get("environmentId"),
            module_name=data.get("moduleName"),
            pod_name=data.get("podName"),
            container_name=data.get("containerName"),
            logs=[LogEntry.from_dict(i) if isinstance(i, dict) else i for i in data.get("logs")] if data.get("logs") is not None else None,
            next_timestamp=_parse_datetime(data.get("nextTimestamp")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.environment_id is not None:
            _v = self.environment_id
            result["environmentId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.module_name is not None:
            _v = self.module_name
            result["moduleName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pod_name is not None:
            _v = self.pod_name
            result["podName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.container_name is not None:
            _v = self.container_name
            result["containerName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.logs is not None:
            _v = self.logs
            result["logs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.next_timestamp is not None:
            _v = self.next_timestamp
            result["nextTimestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
