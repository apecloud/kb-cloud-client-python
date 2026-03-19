# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .backup_status import BackupStatus
from .backup_type import BackupType


@dataclass
class Backup:
    """backup is the payload for KubeBlocks cluster backup"""
    # Required fields
    auto_backup: bool
    backup_method: str
    backup_policy_name: str
    backup_type: BackupType
    creation_timestamp: datetime
    name: str
    org_name: str
    snapshot_volumes: bool
    source_cluster: str
    status: BackupStatus
    total_size: str
    retention_period: str
    cloud_provider: str
    cloud_region: str
    environment_name: str
    engine: str
    # Optional fields
    backup_repo: Optional[str] = None
    completion_timestamp: Optional[datetime] = None
    duration: Optional[str] = None
    start_timestamp: Optional[datetime] = None
    time_range_end: Optional[datetime] = None
    time_range_start: Optional[datetime] = None
    failure_reason: Optional[str] = None
    extras: Optional[str] = None
    target_pods: Optional[List[str]] = None
    path: Optional[str] = None
    expiration: Optional[datetime] = None
    id_: Optional[str] = None
    cluster_id: Optional[str] = None
    parent_backup_name: Optional[str] = None
    base_backup_name: Optional[str] = None
    encryption_master_key: Optional[str] = None
    encryption_data_key: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Backup":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            auto_backup=data.get("autoBackup"),
            backup_method=data.get("backupMethod"),
            backup_policy_name=data.get("backupPolicyName"),
            backup_repo=data.get("backupRepo"),
            backup_type=BackupType.from_dict(data.get("backupType")) if isinstance(data.get("backupType"), dict) else data.get("backupType"),
            completion_timestamp=_parse_datetime(data.get("completionTimestamp")),
            creation_timestamp=_parse_datetime(data.get("creationTimestamp")),
            duration=data.get("duration"),
            name=data.get("name"),
            org_name=data.get("orgName"),
            snapshot_volumes=data.get("snapshotVolumes"),
            source_cluster=data.get("sourceCluster"),
            start_timestamp=_parse_datetime(data.get("startTimestamp")),
            status=BackupStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
            time_range_end=_parse_datetime(data.get("timeRangeEnd")),
            time_range_start=_parse_datetime(data.get("timeRangeStart")),
            total_size=data.get("totalSize"),
            failure_reason=data.get("failureReason"),
            extras=data.get("extras"),
            target_pods=data.get("targetPods"),
            path=data.get("path"),
            retention_period=data.get("retentionPeriod"),
            expiration=_parse_datetime(data.get("expiration")),
            id_=data.get("id"),
            cluster_id=data.get("clusterId"),
            cloud_provider=data.get("cloudProvider"),
            cloud_region=data.get("cloudRegion"),
            environment_name=data.get("environmentName"),
            engine=data.get("engine"),
            parent_backup_name=data.get("parentBackupName"),
            base_backup_name=data.get("baseBackupName"),
            encryption_master_key=data.get("encryptionMasterKey"),
            encryption_data_key=data.get("encryptionDataKey"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.auto_backup is not None:
            _v = self.auto_backup
            result["autoBackup"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_method is not None:
            _v = self.backup_method
            result["backupMethod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_policy_name is not None:
            _v = self.backup_policy_name
            result["backupPolicyName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_repo is not None:
            _v = self.backup_repo
            result["backupRepo"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_type is not None:
            _v = self.backup_type
            result["backupType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.completion_timestamp is not None:
            _v = self.completion_timestamp
            result["completionTimestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.creation_timestamp is not None:
            _v = self.creation_timestamp
            result["creationTimestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.duration is not None:
            _v = self.duration
            result["duration"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.org_name is not None:
            _v = self.org_name
            result["orgName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.snapshot_volumes is not None:
            _v = self.snapshot_volumes
            result["snapshotVolumes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.source_cluster is not None:
            _v = self.source_cluster
            result["sourceCluster"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.start_timestamp is not None:
            _v = self.start_timestamp
            result["startTimestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.time_range_end is not None:
            _v = self.time_range_end
            result["timeRangeEnd"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.time_range_start is not None:
            _v = self.time_range_start
            result["timeRangeStart"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.total_size is not None:
            _v = self.total_size
            result["totalSize"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.failure_reason is not None:
            _v = self.failure_reason
            result["failureReason"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extras is not None:
            _v = self.extras
            result["extras"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.target_pods is not None:
            _v = self.target_pods
            result["targetPods"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.path is not None:
            _v = self.path
            result["path"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.retention_period is not None:
            _v = self.retention_period
            result["retentionPeriod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.expiration is not None:
            _v = self.expiration
            result["expiration"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_id is not None:
            _v = self.cluster_id
            result["clusterId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cloud_provider is not None:
            _v = self.cloud_provider
            result["cloudProvider"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cloud_region is not None:
            _v = self.cloud_region
            result["cloudRegion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.environment_name is not None:
            _v = self.environment_name
            result["environmentName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.engine is not None:
            _v = self.engine
            result["engine"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parent_backup_name is not None:
            _v = self.parent_backup_name
            result["parentBackupName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.base_backup_name is not None:
            _v = self.base_backup_name
            result["baseBackupName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.encryption_master_key is not None:
            _v = self.encryption_master_key
            result["encryptionMasterKey"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.encryption_data_key is not None:
            _v = self.encryption_data_key
            result["encryptionDataKey"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
