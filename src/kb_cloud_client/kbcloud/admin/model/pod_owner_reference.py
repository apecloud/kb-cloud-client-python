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
class PodOwnerReference:
    """Reference to pod owner"""
    # Required fields
    # Optional fields
    kind: Optional[str] = None
    name: Optional[str] = None
    uid: Optional[str] = None
    api_version: Optional[str] = None
    controller: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PodOwnerReference":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            kind=data.get("kind"),
            name=data.get("name"),
            uid=data.get("uid"),
            api_version=data.get("apiVersion"),
            controller=data.get("controller"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.kind is not None:
            _v = self.kind
            result["kind"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.uid is not None:
            _v = self.uid
            result["uid"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.api_version is not None:
            _v = self.api_version
            result["apiVersion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.controller is not None:
            _v = self.controller
            result["controller"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
