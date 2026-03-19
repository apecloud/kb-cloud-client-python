# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .backup_repo_access_method import BackupRepoAccessMethod
from .backup_repo_pv_reclaim_policy import BackupRepoPVReclaimPolicy


@dataclass
class BackupRepoCreate:
    """BackupRepoCreate is the payload to create a KubeBlocks cluster backup repo"""
    # Required fields
    storage_id: str
    name: str
    # Optional fields
    access_method: Optional[BackupRepoAccessMethod] = None
    default: Optional[bool] = None
    params: Optional[Dict[str, str]] = None
    pv_reclaim_policy: Optional[BackupRepoPVReclaimPolicy] = None
    volume_capacity: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BackupRepoCreate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            storage_id=data.get("storageID"),
            access_method=BackupRepoAccessMethod.from_dict(data.get("accessMethod")) if isinstance(data.get("accessMethod"), dict) else data.get("accessMethod"),
            default=data.get("default"),
            name=data.get("name"),
            params=data.get("params"),
            pv_reclaim_policy=BackupRepoPVReclaimPolicy.from_dict(data.get("pvReclaimPolicy")) if isinstance(data.get("pvReclaimPolicy"), dict) else data.get("pvReclaimPolicy"),
            volume_capacity=data.get("volumeCapacity"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.storage_id is not None:
            _v = self.storage_id
            result["storageID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.access_method is not None:
            _v = self.access_method
            result["accessMethod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.default is not None:
            _v = self.default
            result["default"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.params is not None:
            _v = self.params
            result["params"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pv_reclaim_policy is not None:
            _v = self.pv_reclaim_policy
            result["pvReclaimPolicy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.volume_capacity is not None:
            _v = self.volume_capacity
            result["volumeCapacity"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
