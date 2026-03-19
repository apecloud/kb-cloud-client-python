# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .engine_definition_detail import EngineDefinitionDetail


@dataclass
class EngineDefinition:
    """EngineDefinition"""
    # Required fields
    # Optional fields
    name: Optional[str] = None
    engine_name: Optional[str] = None
    escapes: Optional[List[str]] = None
    source: Optional[EngineDefinitionDetail] = None
    target: Optional[EngineDefinitionDetail] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EngineDefinition":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            engine_name=data.get("engineName"),
            escapes=data.get("escapes"),
            source=EngineDefinitionDetail.from_dict(data.get("source")) if isinstance(data.get("source"), dict) else data.get("source"),
            target=EngineDefinitionDetail.from_dict(data.get("target")) if isinstance(data.get("target"), dict) else data.get("target"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.engine_name is not None:
            _v = self.engine_name
            result["engineName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.escapes is not None:
            _v = self.escapes
            result["escapes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.source is not None:
            _v = self.source
            result["source"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.target is not None:
            _v = self.target
            result["target"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
