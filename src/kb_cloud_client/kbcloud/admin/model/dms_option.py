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
class DmsOption:
    """DmsOption"""
    # Required fields
    enabled: bool
    # Optional fields
    protocol: Optional[str] = None
    feature: Optional[Dict[str, Any]] = None
    default_account: Optional[str] = None
    table_metadata: Optional[List[Dict[str, Any]]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            enabled=data.get("enabled"),
            protocol=data.get("protocol"),
            feature=data.get("feature"),
            default_account=data.get("defaultAccount"),
            table_metadata=data.get("tableMetadata"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.enabled is not None:
            _v = self.enabled
            result["enabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.protocol is not None:
            _v = self.protocol
            result["protocol"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.feature is not None:
            _v = self.feature
            result["feature"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.default_account is not None:
            _v = self.default_account
            result["defaultAccount"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.table_metadata is not None:
            _v = self.table_metadata
            result["tableMetadata"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
