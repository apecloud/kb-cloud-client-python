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
class Metadb_restore:
    """Metadb_restore"""
    # Required fields
    cluster_name: str
    # Optional fields
    namespace: Optional[str] = None
    backup_name: Optional[str] = None
    timestamp: Optional[str] = None
    duration: Optional[str] = None
    completion_timestamp: Optional[datetime] = None
    start_timestamp: Optional[datetime] = None
    cpu: Optional[float] = None
    memory: Optional[float] = None
    storage: Optional[float] = None
    replicas: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Metadb_restore":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            namespace=data.get("namespace"),
            backup_name=data.get("backupName"),
            cluster_name=data.get("clusterName"),
            timestamp=data.get("timestamp"),
            duration=data.get("duration"),
            completion_timestamp=_parse_datetime(data.get("completionTimestamp")),
            start_timestamp=_parse_datetime(data.get("startTimestamp")),
            cpu=data.get("cpu"),
            memory=data.get("memory"),
            storage=data.get("storage"),
            replicas=data.get("replicas"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.namespace is not None:
            _v = self.namespace
            result["namespace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_name is not None:
            _v = self.backup_name
            result["backupName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_name is not None:
            _v = self.cluster_name
            result["clusterName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.timestamp is not None:
            _v = self.timestamp
            result["timestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.duration is not None:
            _v = self.duration
            result["duration"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.completion_timestamp is not None:
            _v = self.completion_timestamp
            result["completionTimestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.start_timestamp is not None:
            _v = self.start_timestamp
            result["startTimestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.storage is not None:
            _v = self.storage
            result["storage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replicas is not None:
            _v = self.replicas
            result["replicas"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
