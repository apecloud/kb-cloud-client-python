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


@dataclass
class BackupRepo:
    """backupRepo is the payload for KubeBlocks cluster backup repo"""
    # Required fields
    config: Dict[str, str]
    created_at: datetime
    default: bool
    environment_id: str
    environment_name: str
    name: str
    storage_provider: str
    # Optional fields
    access_method: Optional[BackupRepoAccessMethod] = None
    id_: Optional[str] = None
    backup_nums: Optional[int] = None
    status: Optional[str] = None
    storage_name: Optional[str] = None
    storage_id: Optional[str] = None
    total_size: Optional[str] = None
    failed_reason: Optional[str] = None
    failed_message: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BackupRepo":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            access_method=BackupRepoAccessMethod.from_dict(data.get("accessMethod")) if isinstance(data.get("accessMethod"), dict) else data.get("accessMethod"),
            id_=data.get("id"),
            backup_nums=data.get("backupNums"),
            config=data.get("config"),
            created_at=_parse_datetime(data.get("createdAt")),
            default=data.get("default"),
            environment_id=data.get("environmentId"),
            environment_name=data.get("environmentName"),
            name=data.get("name"),
            status=data.get("status"),
            storage_name=data.get("storageName"),
            storage_id=data.get("storageID"),
            storage_provider=data.get("storageProvider"),
            total_size=data.get("totalSize"),
            failed_reason=data.get("failedReason"),
            failed_message=data.get("failedMessage"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.access_method is not None:
            _v = self.access_method
            result["accessMethod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_nums is not None:
            _v = self.backup_nums
            result["backupNums"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.config is not None:
            _v = self.config
            result["config"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.default is not None:
            _v = self.default
            result["default"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.environment_id is not None:
            _v = self.environment_id
            result["environmentId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.environment_name is not None:
            _v = self.environment_name
            result["environmentName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.storage_name is not None:
            _v = self.storage_name
            result["storageName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.storage_id is not None:
            _v = self.storage_id
            result["storageID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.storage_provider is not None:
            _v = self.storage_provider
            result["storageProvider"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.total_size is not None:
            _v = self.total_size
            result["totalSize"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.failed_reason is not None:
            _v = self.failed_reason
            result["failedReason"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.failed_message is not None:
            _v = self.failed_message
            result["failedMessage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
