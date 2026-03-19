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
class ClusterExecutionLogItem:
    """Cluster execution log item represents a single log entry"""
    # Required fields
    # Optional fields
    client: Optional[str] = None
    command: Optional[str] = None
    db_name: Optional[str] = None
    execution_time: Optional[float] = None
    extra: Optional[Dict[str, Any]] = None
    timestamp: Optional[int] = None
    user: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClusterExecutionLogItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            client=data.get("client"),
            command=data.get("command"),
            db_name=data.get("dbName"),
            execution_time=data.get("executionTime"),
            extra=data.get("extra"),
            timestamp=data.get("timestamp"),
            user=data.get("user"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.client is not None:
            _v = self.client
            result["client"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.command is not None:
            _v = self.command
            result["command"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.db_name is not None:
            _v = self.db_name
            result["dbName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.execution_time is not None:
            _v = self.execution_time
            result["executionTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extra is not None:
            _v = self.extra
            result["extra"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.timestamp is not None:
            _v = self.timestamp
            result["timestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.user is not None:
            _v = self.user
            result["user"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
