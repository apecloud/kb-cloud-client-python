# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .service_ref import ServiceRef


@dataclass
class ClusterObjectStorageConfig:
    """Specify the object storage config for cluster like starrocks"""
    # Required fields
    service_ref: ServiceRef
    bucket: str
    # Optional fields
    use_path_style: Optional[bool] = None
    region: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClusterObjectStorageConfig":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            service_ref=ServiceRef.from_dict(data.get("serviceRef")) if isinstance(data.get("serviceRef"), dict) else data.get("serviceRef"),
            bucket=data.get("bucket"),
            use_path_style=data.get("usePathStyle"),
            region=data.get("region"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.service_ref is not None:
            _v = self.service_ref
            result["serviceRef"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.bucket is not None:
            _v = self.bucket
            result["bucket"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
