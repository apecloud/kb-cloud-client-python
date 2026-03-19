# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .data_channel_object import DataChannelObject


@dataclass
class ImportPreflightRequest:
    """Data source preflight request"""
    # Required fields
    source_type: str
    connection_config: Dict[str, Any]
    # Optional fields
    object_selection: Optional[DataChannelObject] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ImportPreflightRequest":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            source_type=data.get("sourceType"),
            connection_config=data.get("connectionConfig"),
            object_selection=DataChannelObject.from_dict(data.get("objectSelection")) if isinstance(data.get("objectSelection"), dict) else data.get("objectSelection"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.source_type is not None:
            _v = self.source_type
            result["sourceType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.connection_config is not None:
            _v = self.connection_config
            result["connectionConfig"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.object_selection is not None:
            _v = self.object_selection
            result["objectSelection"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
