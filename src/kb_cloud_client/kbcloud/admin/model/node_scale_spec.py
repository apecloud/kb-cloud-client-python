# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .ssh_config import SshConfig


@dataclass
class NodeScaleSpec:
    """NodeScaleSpec"""
    # Required fields
    ip: str
    availability_zone: str
    mark_control_plane: bool
    mark_data_plane: bool
    # Optional fields
    ssh: Optional[SshConfig] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "NodeScaleSpec":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            ip=data.get("ip"),
            availability_zone=data.get("availabilityZone"),
            mark_control_plane=data.get("markControlPlane"),
            mark_data_plane=data.get("markDataPlane"),
            ssh=SshConfig.from_dict(data.get("ssh")) if isinstance(data.get("ssh"), dict) else data.get("ssh"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.ip is not None:
            _v = self.ip
            result["ip"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.ssh is not None:
            _v = self.ssh
            result["ssh"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
