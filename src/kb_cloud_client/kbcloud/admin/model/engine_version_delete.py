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
class EngineVersionDelete:
    """EngineVersionRecord delete option"""
    # Required fields
    engine_name: str
    version: str
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EngineVersionDelete":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            engine_name=data.get("engineName"),
            version=data.get("version"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.engine_name is not None:
            _v = self.engine_name
            result["engineName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.version is not None:
            _v = self.version
            result["version"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
