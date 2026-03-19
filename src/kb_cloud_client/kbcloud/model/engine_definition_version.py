# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .engine_definition_version_query import EngineDefinitionVersionQuery


@dataclass
class EngineDefinitionVersion:
    """EngineDefinitionVersion"""
    # Required fields
    # Optional fields
    version: Optional[str] = None
    query: Optional[EngineDefinitionVersionQuery] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EngineDefinitionVersion":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            version=data.get("version"),
            query=EngineDefinitionVersionQuery.from_dict(data.get("query")) if isinstance(data.get("query"), dict) else data.get("query"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.version is not None:
            _v = self.version
            result["version"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.query is not None:
            _v = self.query
            result["query"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
