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
class StorageClassNodeStats:
    """storageClassNodeStats is a storage class node stats."""
    # Required fields
    node_name: str
    node_status: str
    requests: float
    usage: float
    capacity: float
    pvc_count: int
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StorageClassNodeStats":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            node_name=data.get("nodeName"),
            node_status=data.get("nodeStatus"),
            requests=data.get("requests"),
            usage=data.get("usage"),
            capacity=data.get("capacity"),
            pvc_count=data.get("pvcCount"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.node_name is not None:
            _v = self.node_name
            result["nodeName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.node_status is not None:
            _v = self.node_status
            result["nodeStatus"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.requests is not None:
            _v = self.requests
            result["requests"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.usage is not None:
            _v = self.usage
            result["usage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.capacity is not None:
            _v = self.capacity
            result["capacity"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pvc_count is not None:
            _v = self.pvc_count
            result["pvcCount"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
