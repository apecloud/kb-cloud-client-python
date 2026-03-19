# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .engine_definition_version import EngineDefinitionVersion
from .extra_config import ExtraConfig


@dataclass
class EngineDefinitionDetail:
    """EngineDefinitionDetail"""
    # Required fields
    # Optional fields
    definition_name: Optional[str] = None
    available_modes: Optional[List[str]] = None
    available_versions: Optional[List[EngineDefinitionVersion]] = None
    extra_cfgs: Optional[List[ExtraConfig]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EngineDefinitionDetail":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            definition_name=data.get("definitionName"),
            available_modes=data.get("availableModes"),
            available_versions=[EngineDefinitionVersion.from_dict(i) if isinstance(i, dict) else i for i in data.get("availableVersions")] if data.get("availableVersions") is not None else None,
            extra_cfgs=[ExtraConfig.from_dict(i) if isinstance(i, dict) else i for i in data.get("extraCfgs")] if data.get("extraCfgs") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.definition_name is not None:
            _v = self.definition_name
            result["definitionName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.available_modes is not None:
            _v = self.available_modes
            result["availableModes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.available_versions is not None:
            _v = self.available_versions
            result["availableVersions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extra_cfgs is not None:
            _v = self.extra_cfgs
            result["extraCfgs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
