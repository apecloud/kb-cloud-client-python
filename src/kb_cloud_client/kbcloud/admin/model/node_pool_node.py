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
class NodePoolNode:
    """Node info for environment"""
    # Required fields
    name: str
    availability_zone: str
    # Optional fields
    mark_control_plane: Optional[bool] = None
    mark_data_plane: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "NodePoolNode":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            availability_zone=data.get("availabilityZone"),
            mark_control_plane=data.get("markControlPlane"),
            mark_data_plane=data.get("markDataPlane"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.availability_zone is not None:
            _v = self.availability_zone
            result["availabilityZone"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mark_control_plane is not None:
            _v = self.mark_control_plane
            result["markControlPlane"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mark_data_plane is not None:
            _v = self.mark_data_plane
            result["markDataPlane"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
