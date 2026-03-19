# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .integer_option import IntegerOption
from .storage_option import StorageOption


@dataclass
class ResourceConstraintUpdate:
    """ResourceConstraintUpdate"""
    # Required fields
    # Optional fields
    replicas: Optional[IntegerOption] = None
    shards: Optional[IntegerOption] = None
    volumes: Optional[List[StorageOption]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ResourceConstraintUpdate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            replicas=IntegerOption.from_dict(data.get("replicas")) if isinstance(data.get("replicas"), dict) else data.get("replicas"),
            shards=IntegerOption.from_dict(data.get("shards")) if isinstance(data.get("shards"), dict) else data.get("shards"),
            volumes=[StorageOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("volumes")] if data.get("volumes") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.replicas is not None:
            _v = self.replicas
            result["replicas"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.shards is not None:
            _v = self.shards
            result["shards"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.volumes is not None:
            _v = self.volumes
            result["volumes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
