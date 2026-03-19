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
class ComponentOpsOption:
    """ComponentOpsOption"""
    # Required fields
    component: str
    # Optional fields
    modes: Optional[List[str]] = None
    disable_ha: Optional[bool] = None
    in_place: Optional[bool] = None
    need_backup_when_in_place: Optional[bool] = None
    backup_required: Optional[bool] = None
    backup_method: Optional[Dict[str, Any]] = None
    restore_env: Optional[List[Dict[str, Any]]] = None
    dependent_custom_ops: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ComponentOpsOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            modes=data.get("modes"),
            component=data.get("component"),
            disable_ha=data.get("disableHA"),
            in_place=data.get("inPlace"),
            need_backup_when_in_place=data.get("needBackupWhenInPlace"),
            backup_required=data.get("backupRequired"),
            backup_method=data.get("backupMethod"),
            restore_env=data.get("restoreEnv"),
            dependent_custom_ops=data.get("dependentCustomOps"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.modes is not None:
            _v = self.modes
            result["modes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.disable_ha is not None:
            _v = self.disable_ha
            result["disableHA"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.in_place is not None:
            _v = self.in_place
            result["inPlace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.need_backup_when_in_place is not None:
            _v = self.need_backup_when_in_place
            result["needBackupWhenInPlace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_required is not None:
            _v = self.backup_required
            result["backupRequired"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_method is not None:
            _v = self.backup_method
            result["backupMethod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.restore_env is not None:
            _v = self.restore_env
            result["restoreEnv"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.dependent_custom_ops is not None:
            _v = self.dependent_custom_ops
            result["dependentCustomOps"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
