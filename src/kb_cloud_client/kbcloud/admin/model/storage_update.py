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
class StorageUpdate:
    """storageUpdate is the schema for storage update request"""
    # Required fields
    # Optional fields
    params: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    engines: Optional[List[str]] = None
    storage_name: Optional[str] = None
    env_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StorageUpdate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            params=data.get("params"),
            tags=data.get("tags"),
            engines=data.get("engines"),
            storage_name=data.get("storageName"),
            env_name=data.get("envName"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.params is not None:
            _v = self.params
            result["params"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.tags is not None:
            _v = self.tags
            result["tags"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.engines is not None:
            _v = self.engines
            result["engines"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.storage_name is not None:
            _v = self.storage_name
            result["storageName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.env_name is not None:
            _v = self.env_name
            result["envName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
