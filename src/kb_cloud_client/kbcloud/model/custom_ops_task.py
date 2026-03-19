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
class CustomOpsTask:
    """customOpsTask is the information of custom ops task"""
    # Required fields
    # Optional fields
    object_key: Optional[str] = None
    namespace: Optional[str] = None
    status: Optional[str] = None
    target_pod_name: Optional[str] = None
    retries: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CustomOpsTask":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            object_key=data.get("objectKey"),
            namespace=data.get("namespace"),
            status=data.get("status"),
            target_pod_name=data.get("targetPodName"),
            retries=data.get("retries"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.object_key is not None:
            _v = self.object_key
            result["objectKey"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.namespace is not None:
            _v = self.namespace
            result["namespace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.target_pod_name is not None:
            _v = self.target_pod_name
            result["targetPodName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.retries is not None:
            _v = self.retries
            result["retries"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
