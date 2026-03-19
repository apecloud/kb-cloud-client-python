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
from .encryption_config import EncryptionConfig


@dataclass
class BackupPolicy:
    """BackupPolicy is the payload for KubeBlocks cluster backup policy"""
    # Required fields
    # Optional fields
    auto_backup: Optional[bool] = None
    auto_backup_method: Optional[str] = None
    pitr_enabled: Optional[bool] = None
    continuous_backup_method: Optional[str] = None
    cron_expression: Optional[str] = None
    incremental_backup_enabled: Optional[bool] = None
    incremental_cron_expression: Optional[str] = None
    retention_period: Optional[str] = None
    backup_repo: Optional[str] = None
    retention_policy: Optional[BackupRetentionPolicy] = None
    next_backup_time: Optional[datetime] = None
    encryption_config: Optional[EncryptionConfig] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BackupPolicy":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            auto_backup=data.get("autoBackup"),
            auto_backup_method=data.get("autoBackupMethod"),
            pitr_enabled=data.get("pitrEnabled"),
            continuous_backup_method=data.get("continuousBackupMethod"),
            cron_expression=data.get("cronExpression"),
            incremental_backup_enabled=data.get("incrementalBackupEnabled"),
            incremental_cron_expression=data.get("incrementalCronExpression"),
            retention_period=data.get("retentionPeriod"),
            backup_repo=data.get("backupRepo"),
            retention_policy=BackupRetentionPolicy.from_dict(data.get("retentionPolicy")) if isinstance(data.get("retentionPolicy"), dict) else data.get("retentionPolicy"),
            next_backup_time=_parse_datetime(data.get("nextBackupTime")),
            encryption_config=EncryptionConfig.from_dict(data.get("encryptionConfig")) if isinstance(data.get("encryptionConfig"), dict) else data.get("encryptionConfig"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
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
        if self.cron_expression is not None:
            _v = self.cron_expression
            result["cronExpression"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.retention_period is not None:
            _v = self.retention_period
            result["retentionPeriod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_repo is not None:
            _v = self.backup_repo
            result["backupRepo"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.retention_policy is not None:
            _v = self.retention_policy
            result["retentionPolicy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.next_backup_time is not None:
            _v = self.next_backup_time
            result["nextBackupTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.encryption_config is not None:
            _v = self.encryption_config
            result["encryptionConfig"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
