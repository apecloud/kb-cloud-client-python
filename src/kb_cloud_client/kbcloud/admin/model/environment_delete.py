# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cloud_resource_clean_policy import CloudResourceCleanPolicy


@dataclass
class EnvironmentDelete:
    """Environment deletion option"""
    # Required fields
    # Optional fields
    clean_cloud_resources: Optional[bool] = None
    minio: Optional[CloudResourceCleanPolicy] = None
    victoria_metrics: Optional[CloudResourceCleanPolicy] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EnvironmentDelete":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            clean_cloud_resources=data.get("cleanCloudResources"),
            minio=CloudResourceCleanPolicy.from_dict(data.get("minio")) if isinstance(data.get("minio"), dict) else data.get("minio"),
            victoria_metrics=CloudResourceCleanPolicy.from_dict(data.get("victoriaMetrics")) if isinstance(data.get("victoriaMetrics"), dict) else data.get("victoriaMetrics"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.clean_cloud_resources is not None:
            _v = self.clean_cloud_resources
            result["cleanCloudResources"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.minio is not None:
            _v = self.minio
            result["minio"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.victoria_metrics is not None:
            _v = self.victoria_metrics
            result["victoriaMetrics"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
