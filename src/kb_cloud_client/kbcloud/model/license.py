# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict



@dataclass
class License:
    """License info"""
    # Required fields
    cluster_id: str
    not_after: datetime
    not_before: datetime
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "License":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            cluster_id=data.get("clusterID"),
            not_after=_parse_datetime(data.get("notAfter")),
            not_before=_parse_datetime(data.get("notBefore")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.cluster_id is not None:
            _v = self.cluster_id
            result["clusterID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.not_after is not None:
            _v = self.not_after
            result["notAfter"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.not_before is not None:
            _v = self.not_before
            result["notBefore"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
