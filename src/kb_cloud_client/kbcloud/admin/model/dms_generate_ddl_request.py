# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .dms_generate_ddl_operation_type import DmsGenerateDdlOperationType
from .dms_table_metadata import DmsTableMetadata
from .dms_view_metadata import DmsViewMetadata


@dataclass
class DmsGenerateDDLRequest:
    """DmsGenerateDDLRequest"""
    # Required fields
    type_: DmsGenerateDdlOperationType
    # Optional fields
    table_metadata: Optional[DmsTableMetadata] = None
    view_metadata: Optional[DmsViewMetadata] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsGenerateDDLRequest":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            type_=DmsGenerateDdlOperationType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
            table_metadata=DmsTableMetadata.from_dict(data.get("tableMetadata")) if isinstance(data.get("tableMetadata"), dict) else data.get("tableMetadata"),
            view_metadata=DmsViewMetadata.from_dict(data.get("viewMetadata")) if isinstance(data.get("viewMetadata"), dict) else data.get("viewMetadata"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.table_metadata is not None:
            _v = self.table_metadata
            result["tableMetadata"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.view_metadata is not None:
            _v = self.view_metadata
            result["viewMetadata"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
