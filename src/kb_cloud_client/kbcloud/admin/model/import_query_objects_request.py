# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .import_source_type import ImportSourceType


@dataclass
class ImportQueryObjectsRequest:
    """Request payload for querying import data source objects."""
    # Required fields
    source_type: ImportSourceType
    connection_config: Dict[str, Any]
    # Optional fields
    node_type: Optional[str] = None
    node_value: Optional[str] = None
    query_node_type: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ImportQueryObjectsRequest":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            source_type=ImportSourceType.from_dict(data.get("sourceType")) if isinstance(data.get("sourceType"), dict) else data.get("sourceType"),
            connection_config=data.get("connectionConfig"),
            node_type=data.get("nodeType"),
            node_value=data.get("nodeValue"),
            query_node_type=data.get("queryNodeType"),
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
        if self.node_type is not None:
            _v = self.node_type
            result["nodeType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.node_value is not None:
            _v = self.node_value
            result["nodeValue"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.query_node_type is not None:
            _v = self.query_node_type
            result["queryNodeType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
