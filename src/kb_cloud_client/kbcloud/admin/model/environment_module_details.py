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
from .pod import Pod


@dataclass
class EnvironmentModuleDetails:
    """Detailed information about a specific environment module, including its configuration, status and associated pods"""
    # Required fields
    # Optional fields
    environment_name: Optional[str] = None
    module_info: Optional[EnvironmentModule] = None
    last_updated: Optional[datetime] = None
    module_pods: Optional[List[Pod]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EnvironmentModuleDetails":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            environment_name=data.get("environmentName"),
            module_info=EnvironmentModule.from_dict(data.get("moduleInfo")) if isinstance(data.get("moduleInfo"), dict) else data.get("moduleInfo"),
            last_updated=_parse_datetime(data.get("lastUpdated")),
            module_pods=[Pod.from_dict(i) if isinstance(i, dict) else i for i in data.get("modulePods")] if data.get("modulePods") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.environment_name is not None:
            _v = self.environment_name
            result["environmentName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.module_info is not None:
            _v = self.module_info
            result["moduleInfo"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.last_updated is not None:
            _v = self.last_updated
            result["lastUpdated"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.module_pods is not None:
            _v = self.module_pods
            result["modulePods"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
