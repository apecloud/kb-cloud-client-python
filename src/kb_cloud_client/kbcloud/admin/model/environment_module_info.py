# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .environment_module import EnvironmentModule


@dataclass
class EnvironmentModuleInfo:
    """Environment module information in an environment"""
    # Required fields
    # Optional fields
    environment_id: Optional[str] = None
    last_updated: Optional[datetime] = None
    environment_modules: Optional[List[EnvironmentModule]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EnvironmentModuleInfo":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            environment_id=data.get("environmentId"),
            last_updated=_parse_datetime(data.get("lastUpdated")),
            environment_modules=[EnvironmentModule.from_dict(i) if isinstance(i, dict) else i for i in data.get("environmentModules")] if data.get("environmentModules") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.environment_id is not None:
            _v = self.environment_id
            result["environmentId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.last_updated is not None:
            _v = self.last_updated
            result["lastUpdated"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.environment_modules is not None:
            _v = self.environment_modules
            result["environmentModules"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
