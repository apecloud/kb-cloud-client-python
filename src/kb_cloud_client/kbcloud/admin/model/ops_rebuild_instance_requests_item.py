# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .ops_rebuild_instance_instance_param import OpsRebuildInstanceInstanceParam


@dataclass
class OpsRebuildInstanceRequestsItem:
    """OpsRebuildInstanceRequestsItem"""
    # Required fields
    instances: List[OpsRebuildInstanceInstanceParam]
    # Optional fields
    backup_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OpsRebuildInstanceRequestsItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            backup_name=data.get("backupName"),
            instances=[OpsRebuildInstanceInstanceParam.from_dict(i) if isinstance(i, dict) else i for i in data.get("instances")] if data.get("instances") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.backup_name is not None:
            _v = self.backup_name
            result["backupName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.instances is not None:
            _v = self.instances
            result["instances"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
