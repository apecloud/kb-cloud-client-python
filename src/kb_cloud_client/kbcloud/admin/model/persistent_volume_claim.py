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
class PersistentVolumeClaim:
    """persistentVolumeClaim provides detailed information about the PVC ."""
    # Required fields
    name_space: str
    name: str
    phase: str
    # Optional fields
    capacity: Optional[float] = None
    usage: Optional[float] = None
    access_mode: Optional[str] = None
    volume_name: Optional[str] = None
    node: Optional[str] = None
    org_name: Optional[str] = None
    cluster_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PersistentVolumeClaim":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name_space=data.get("nameSpace"),
            name=data.get("name"),
            phase=data.get("phase"),
            capacity=data.get("capacity"),
            usage=data.get("usage"),
            access_mode=data.get("accessMode"),
            volume_name=data.get("volumeName"),
            node=data.get("node"),
            org_name=data.get("orgName"),
            cluster_name=data.get("clusterName"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name_space is not None:
            _v = self.name_space
            result["nameSpace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.phase is not None:
            _v = self.phase
            result["phase"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.capacity is not None:
            _v = self.capacity
            result["capacity"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.usage is not None:
            _v = self.usage
            result["usage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.access_mode is not None:
            _v = self.access_mode
            result["accessMode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.volume_name is not None:
            _v = self.volume_name
            result["volumeName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.node is not None:
            _v = self.node
            result["node"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.org_name is not None:
            _v = self.org_name
            result["orgName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_name is not None:
            _v = self.cluster_name
            result["clusterName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
