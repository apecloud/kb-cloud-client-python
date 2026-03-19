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
class BackupMethodOptionRestoreOption:
    """BackupMethodOptionRestoreOption"""
    # Required fields
    # Optional fields
    restore_on_components: Optional[List[str]] = None
    defer_post_ready_until_cluster_running: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BackupMethodOptionRestoreOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            restore_on_components=data.get("restoreOnComponents"),
            defer_post_ready_until_cluster_running=data.get("deferPostReadyUntilClusterRunning"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.restore_on_components is not None:
            _v = self.restore_on_components
            result["restoreOnComponents"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.defer_post_ready_until_cluster_running is not None:
            _v = self.defer_post_ready_until_cluster_running
            result["deferPostReadyUntilClusterRunning"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
