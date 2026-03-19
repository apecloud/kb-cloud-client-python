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
class ImportReplicationMetadata:
    """Replication metadata tree definition for import object selection."""
    # Required fields
    metadata_type: str
    # Optional fields
    children: Optional[List[ImportReplicationMetadata]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ImportReplicationMetadata":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            metadata_type=data.get("metadataType"),
            children=[ImportReplicationMetadata.from_dict(i) if isinstance(i, dict) else i for i in data.get("children")] if data.get("children") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.metadata_type is not None:
            _v = self.metadata_type
            result["metadataType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.children is not None:
            _v = self.children
            result["children"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
