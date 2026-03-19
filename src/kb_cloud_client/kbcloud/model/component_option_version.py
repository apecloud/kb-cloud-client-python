# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .component_version_architecture import ComponentVersionArchitecture


@dataclass
class ComponentOptionVersion:
    """ComponentOptionVersion"""
    # Required fields
    component_version_name: str
    major_version: Dict[str, Any]
    # Optional fields
    minor_version: Optional[Dict[str, Any]] = None
    architecture: Optional[ComponentVersionArchitecture] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ComponentOptionVersion":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            component_version_name=data.get("componentVersionName"),
            minor_version=data.get("minorVersion"),
            major_version=data.get("majorVersion"),
            architecture=ComponentVersionArchitecture.from_dict(data.get("architecture")) if isinstance(data.get("architecture"), dict) else data.get("architecture"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.component_version_name is not None:
            _v = self.component_version_name
            result["componentVersionName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.minor_version is not None:
            _v = self.minor_version
            result["minorVersion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.major_version is not None:
            _v = self.major_version
            result["majorVersion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.architecture is not None:
            _v = self.architecture
            result["architecture"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
