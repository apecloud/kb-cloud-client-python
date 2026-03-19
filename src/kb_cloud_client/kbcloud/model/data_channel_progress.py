# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .data_channel_module_progress import DataChannelModuleProgress


@dataclass
class DataChannelProgress:
    """DataChannelProgress"""
    # Required fields
    # Optional fields
    progress: Optional[float] = None
    module_progress: Optional[List[DataChannelModuleProgress]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataChannelProgress":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            progress=data.get("progress"),
            module_progress=[DataChannelModuleProgress.from_dict(i) if isinstance(i, dict) else i for i in data.get("moduleProgress")] if data.get("moduleProgress") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.progress is not None:
            _v = self.progress
            result["progress"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.module_progress is not None:
            _v = self.module_progress
            result["moduleProgress"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
