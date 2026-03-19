# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .backup_retention_policy import BackupRetentionPolicy


@dataclass
class ClusterBackup:
    """clusterBackup is the payload for cluster backup"""
    # Required fields
    # Optional fields
    pitr_enabled: Optional[bool] = None
    continuous_backup_method: Optional[str] = None
    auto_backup: Optional[bool] = None
    auto_backup_method: Optional[str] = None
    backup_repo: Optional[str] = None
    cron_expression: Optional[str] = None
    retention_period: Optional[str] = None
    retention_policy: Optional[BackupRetentionPolicy] = None
    snapshot_volumes: Optional[bool] = None
    incremental_backup_enabled: Optional[bool] = None
    incremental_cron_expression: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClusterBackup":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            pitr_enabled=data.get("pitrEnabled"),
            continuous_backup_method=data.get("continuousBackupMethod"),
            auto_backup=data.get("autoBackup"),
            auto_backup_method=data.get("autoBackupMethod"),
            backup_repo=data.get("backupRepo"),
            cron_expression=data.get("cronExpression"),
            retention_period=data.get("retentionPeriod"),
            retention_policy=BackupRetentionPolicy.from_dict(data.get("retentionPolicy")) if isinstance(data.get("retentionPolicy"), dict) else data.get("retentionPolicy"),
            snapshot_volumes=data.get("snapshotVolumes"),
            incremental_backup_enabled=data.get("incrementalBackupEnabled"),
            incremental_cron_expression=data.get("incrementalCronExpression"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.pitr_enabled is not None:
            _v = self.pitr_enabled
            result["pitrEnabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.continuous_backup_method is not None:
            _v = self.continuous_backup_method
            result["continuousBackupMethod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.auto_backup is not None:
            _v = self.auto_backup
            result["autoBackup"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.auto_backup_method is not None:
            _v = self.auto_backup_method
            result["autoBackupMethod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_repo is not None:
            _v = self.backup_repo
            result["backupRepo"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cron_expression is not None:
            _v = self.cron_expression
            result["cronExpression"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.retention_period is not None:
            _v = self.retention_period
            result["retentionPeriod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.retention_policy is not None:
            _v = self.retention_policy
            result["retentionPolicy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.snapshot_volumes is not None:
            _v = self.snapshot_volumes
            result["snapshotVolumes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.incremental_backup_enabled is not None:
            _v = self.incremental_backup_enabled
            result["incrementalBackupEnabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.incremental_cron_expression is not None:
            _v = self.incremental_cron_expression
            result["incrementalCronExpression"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
