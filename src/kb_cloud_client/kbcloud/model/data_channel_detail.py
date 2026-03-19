# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .data_channel_item import DataChannelItem
from .data_channel_progress import DataChannelProgress


@dataclass
class DataChannelDetail:
    """DataChannelDetail"""
    # Required fields
    # Optional fields
    channel: Optional[DataChannelItem] = None
    progress: Optional[DataChannelProgress] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataChannelDetail":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            channel=DataChannelItem.from_dict(data.get("channel")) if isinstance(data.get("channel"), dict) else data.get("channel"),
            progress=DataChannelProgress.from_dict(data.get("progress")) if isinstance(data.get("progress"), dict) else data.get("progress"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.channel is not None:
            _v = self.channel
            result["channel"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.progress is not None:
            _v = self.progress
            result["progress"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
