# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .engine_service_versions_item import EngineServiceVersionsItem


@dataclass
class EngineServiceVersions:
    """EngineServiceVersions"""
    # Required fields
    # Optional fields
    component: Optional[str] = None
    upgradeable_versions: Optional[List[str]] = None
    current_version: Optional[str] = None
    versions: Optional[List[EngineServiceVersionsItem]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EngineServiceVersions":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            component=data.get("component"),
            upgradeable_versions=data.get("upgradeableVersions"),
            current_version=data.get("currentVersion"),
            versions=[EngineServiceVersionsItem.from_dict(i) if isinstance(i, dict) else i for i in data.get("versions")] if data.get("versions") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.upgradeable_versions is not None:
            _v = self.upgradeable_versions
            result["upgradeableVersions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.current_version is not None:
            _v = self.current_version
            result["currentVersion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.versions is not None:
            _v = self.versions
            result["versions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
