# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .backup_stats_engine import BackupStatsEngine
from .backup_stats_status import BackupStatsStatus
from .backup_stats_type import BackupStatsType


@dataclass
class BackupRepoStats:
    """BackupRepoStats"""
    # Required fields
    # Optional fields
    total_backup: Optional[int] = None
    total_size: Optional[str] = None
    backup_stats_status: Optional[List[BackupStatsStatus]] = None
    backup_stats_engine: Optional[List[BackupStatsEngine]] = None
    backup_stats_type: Optional[List[BackupStatsType]] = None
    created_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BackupRepoStats":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            total_backup=data.get("totalBackup"),
            total_size=data.get("totalSize"),
            backup_stats_status=[BackupStatsStatus.from_dict(i) if isinstance(i, dict) else i for i in data.get("backupStatsStatus")] if data.get("backupStatsStatus") is not None else None,
            backup_stats_engine=[BackupStatsEngine.from_dict(i) if isinstance(i, dict) else i for i in data.get("backupStatsEngine")] if data.get("backupStatsEngine") is not None else None,
            backup_stats_type=[BackupStatsType.from_dict(i) if isinstance(i, dict) else i for i in data.get("backupStatsType")] if data.get("backupStatsType") is not None else None,
            created_at=_parse_datetime(data.get("createdAt")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.total_backup is not None:
            _v = self.total_backup
            result["totalBackup"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.total_size is not None:
            _v = self.total_size
            result["totalSize"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_stats_status is not None:
            _v = self.backup_stats_status
            result["backupStatsStatus"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_stats_engine is not None:
            _v = self.backup_stats_engine
            result["backupStatsEngine"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_stats_type is not None:
            _v = self.backup_stats_type
            result["backupStatsType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
