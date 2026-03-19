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
class ModeObjectStorageAdditionalHelmValuePath:
    """The path in helm values that some object storage config will use. If empty, the values will not be set."""
    # Required fields
    bucket: str
    # Optional fields
    path: Optional[str] = None
    use_path_style: Optional[str] = None
    region: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ModeObjectStorageAdditionalHelmValuePath":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            bucket=data.get("bucket"),
            path=data.get("path"),
            use_path_style=data.get("usePathStyle"),
            region=data.get("region"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.bucket is not None:
            _v = self.bucket
            result["bucket"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.path is not None:
            _v = self.path
            result["path"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.use_path_style is not None:
            _v = self.use_path_style
            result["usePathStyle"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.region is not None:
            _v = self.region
            result["region"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
