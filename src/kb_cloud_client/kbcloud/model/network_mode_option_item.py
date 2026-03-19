# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .network_mode import NetworkMode


@dataclass
class NetworkModeOptionItem:
    """NetworkModeOptionItem"""
    # Required fields
    supported: List[NetworkMode]
    # Optional fields
    not_supported_versions: Optional[Dict[str, List[str]]] = None
    modes: Optional[List[str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "NetworkModeOptionItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            supported=[NetworkMode.from_dict(i) if isinstance(i, dict) else i for i in data.get("supported")] if data.get("supported") is not None else None,
            not_supported_versions=data.get("notSupportedVersions"),
            modes=data.get("modes"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.supported is not None:
            _v = self.supported
            result["supported"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.not_supported_versions is not None:
            _v = self.not_supported_versions
            result["notSupportedVersions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.modes is not None:
            _v = self.modes
            result["modes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
