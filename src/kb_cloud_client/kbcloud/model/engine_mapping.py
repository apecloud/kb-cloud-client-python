# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .mapping_description import MappingDescription
from .replication_metadata_object import ReplicationMetadataObject


@dataclass
class EngineMapping:
    """EngineMapping"""
    # Required fields
    # Optional fields
    source: Optional[str] = None
    target: Optional[str] = None
    modules: Optional[List[str]] = None
    events: Optional[List[List[EventObject]]] = None
    replication_metadata: Optional[ReplicationMetadataObject] = None
    descriptions: Optional[MappingDescription] = None
    pre_checkers: Optional[List[str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EngineMapping":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            source=data.get("source"),
            target=data.get("target"),
            modules=data.get("modules"),
            events=data.get("events"),
            replication_metadata=ReplicationMetadataObject.from_dict(data.get("replicationMetadata")) if isinstance(data.get("replicationMetadata"), dict) else data.get("replicationMetadata"),
            descriptions=MappingDescription.from_dict(data.get("descriptions")) if isinstance(data.get("descriptions"), dict) else data.get("descriptions"),
            pre_checkers=data.get("preCheckers"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.source is not None:
            _v = self.source
            result["source"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.target is not None:
            _v = self.target
            result["target"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.modules is not None:
            _v = self.modules
            result["modules"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.events is not None:
            _v = self.events
            result["events"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replication_metadata is not None:
            _v = self.replication_metadata
            result["replicationMetadata"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.descriptions is not None:
            _v = self.descriptions
            result["descriptions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pre_checkers is not None:
            _v = self.pre_checkers
            result["preCheckers"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
