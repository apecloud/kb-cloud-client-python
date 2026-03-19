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
class StorageConfigBackup:
    """the storage config for backup"""
    # Required fields
    storage_name: str
    backup_repo_name: str
    default_backup_repo: bool
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StorageConfigBackup":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            storage_name=data.get("storageName"),
            backup_repo_name=data.get("backupRepoName"),
            default_backup_repo=data.get("defaultBackupRepo"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.storage_name is not None:
            _v = self.storage_name
            result["storageName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_repo_name is not None:
            _v = self.backup_repo_name
            result["backupRepoName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.default_backup_repo is not None:
            _v = self.default_backup_repo
            result["defaultBackupRepo"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
