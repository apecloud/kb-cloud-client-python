# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cluster_create import ClusterCreate
from .volume_restore_policy import VolumeRestorePolicy


@dataclass
class RestoreCreate:
    """RestoreCreate is the payload to restore a KubeBlocks cluster"""
    # Required fields
    environment_name: str
    backup_id: str
    cluster: ClusterCreate
    # Optional fields
    restore_time_str: Optional[str] = None
    do_ready_restore_after_cluster_running: Optional[bool] = None
    volume_restore_policy: Optional[VolumeRestorePolicy] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RestoreCreate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            environment_name=data.get("environmentName"),
            backup_id=data.get("backupId"),
            cluster=ClusterCreate.from_dict(data.get("cluster")) if isinstance(data.get("cluster"), dict) else data.get("cluster"),
            restore_time_str=data.get("restoreTimeStr"),
            do_ready_restore_after_cluster_running=data.get("doReadyRestoreAfterClusterRunning"),
            volume_restore_policy=VolumeRestorePolicy.from_dict(data.get("volumeRestorePolicy")) if isinstance(data.get("volumeRestorePolicy"), dict) else data.get("volumeRestorePolicy"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.environment_name is not None:
            _v = self.environment_name
            result["environmentName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_id is not None:
            _v = self.backup_id
            result["backupId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster is not None:
            _v = self.cluster
            result["cluster"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.restore_time_str is not None:
            _v = self.restore_time_str
            result["restoreTimeStr"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.do_ready_restore_after_cluster_running is not None:
            _v = self.do_ready_restore_after_cluster_running
            result["doReadyRestoreAfterClusterRunning"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.volume_restore_policy is not None:
            _v = self.volume_restore_policy
            result["volumeRestorePolicy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
