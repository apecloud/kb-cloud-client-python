# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .backup_method_option import BackupMethodOption


@dataclass
class BackupOption:
    """If present, it must be set defaultMethod and fullMethod"""
    # Required fields
    default_method: str
    full_method: List[BackupMethodOption]
    # Optional fields
    default_component: Optional[str] = None
    restore_option: Optional[Dict[str, Any]] = None
    incremental_method: Optional[List[BackupMethodOption]] = None
    continuous_method: Optional[List[BackupMethodOption]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BackupOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            default_method=data.get("defaultMethod"),
            default_component=data.get("defaultComponent"),
            restore_option=data.get("restoreOption"),
            full_method=[BackupMethodOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("fullMethod")] if data.get("fullMethod") is not None else None,
            incremental_method=[BackupMethodOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("incrementalMethod")] if data.get("incrementalMethod") is not None else None,
            continuous_method=[BackupMethodOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("continuousMethod")] if data.get("continuousMethod") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.default_method is not None:
            _v = self.default_method
            result["defaultMethod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.default_component is not None:
            _v = self.default_component
            result["defaultComponent"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.restore_option is not None:
            _v = self.restore_option
            result["restoreOption"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.full_method is not None:
            _v = self.full_method
            result["fullMethod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.incremental_method is not None:
            _v = self.incremental_method
            result["incrementalMethod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.continuous_method is not None:
            _v = self.continuous_method
            result["continuousMethod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
