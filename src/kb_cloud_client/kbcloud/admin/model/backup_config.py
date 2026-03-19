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
class BackupConfig:
    """BackupConfig"""
    # Required fields
    # Optional fields
    provider: Optional[str] = None
    schedule: Optional[str] = None
    access_key_id: Optional[str] = None
    secret_access_key: Optional[str] = None
    endpoint: Optional[str] = None
    region: Optional[str] = None
    bucket: Optional[str] = None
    auto_backup: Optional[bool] = None
    next_backup_time: Optional[str] = None
    retention_day: Optional[int] = None
    last_backup_time: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BackupConfig":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            provider=data.get("provider"),
            schedule=data.get("schedule"),
            access_key_id=data.get("accessKeyId"),
            secret_access_key=data.get("secretAccessKey"),
            endpoint=data.get("endpoint"),
            region=data.get("region"),
            bucket=data.get("bucket"),
            auto_backup=data.get("autoBackup"),
            next_backup_time=data.get("nextBackupTime"),
            retention_day=data.get("retentionDay"),
            last_backup_time=data.get("lastBackupTime"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.provider is not None:
            _v = self.provider
            result["provider"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.schedule is not None:
            _v = self.schedule
            result["schedule"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.access_key_id is not None:
            _v = self.access_key_id
            result["accessKeyId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.secret_access_key is not None:
            _v = self.secret_access_key
            result["secretAccessKey"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.endpoint is not None:
            _v = self.endpoint
            result["endpoint"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.region is not None:
            _v = self.region
            result["region"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.bucket is not None:
            _v = self.bucket
            result["bucket"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.auto_backup is not None:
            _v = self.auto_backup
            result["autoBackup"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.next_backup_time is not None:
            _v = self.next_backup_time
            result["nextBackupTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.retention_day is not None:
            _v = self.retention_day
            result["retentionDay"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.last_backup_time is not None:
            _v = self.last_backup_time
            result["lastBackupTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
