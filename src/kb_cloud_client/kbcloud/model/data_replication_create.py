# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .data_channel_endpoint_create import DataChannelEndpointCreate
from .data_channel_object import DataChannelObject
from .event_object import EventObject


@dataclass
class DataReplicationCreate:
    """DataReplicationCreate"""
    # Required fields
    # Optional fields
    channel_name: Optional[str] = None
    modules: Optional[List[str]] = None
    environment_id: Optional[str] = None
    project: Optional[str] = None
    standard_definition: Optional[str] = None
    source: Optional[DataChannelEndpointCreate] = None
    target: Optional[DataChannelEndpointCreate] = None
    replication_objects: Optional[DataChannelObject] = None
    events: Optional[List[EventObject]] = None
    parameters: Optional[Dict[str, List[DataChannelParameterKeyValue]]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataReplicationCreate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            channel_name=data.get("channelName"),
            modules=data.get("modules"),
            environment_id=data.get("environmentID"),
            project=data.get("project"),
            standard_definition=data.get("standardDefinition"),
            source=DataChannelEndpointCreate.from_dict(data.get("source")) if isinstance(data.get("source"), dict) else data.get("source"),
            target=DataChannelEndpointCreate.from_dict(data.get("target")) if isinstance(data.get("target"), dict) else data.get("target"),
            replication_objects=DataChannelObject.from_dict(data.get("replicationObjects")) if isinstance(data.get("replicationObjects"), dict) else data.get("replicationObjects"),
            events=[EventObject.from_dict(i) if isinstance(i, dict) else i for i in data.get("events")] if data.get("events") is not None else None,
            parameters=data.get("parameters"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.channel_name is not None:
            _v = self.channel_name
            result["channelName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.modules is not None:
            _v = self.modules
            result["modules"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.environment_id is not None:
            _v = self.environment_id
            result["environmentID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.project is not None:
            _v = self.project
            result["project"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.standard_definition is not None:
            _v = self.standard_definition
            result["standardDefinition"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
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
        if self.replication_objects is not None:
            _v = self.replication_objects
            result["replicationObjects"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.events is not None:
            _v = self.events
            result["events"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parameters is not None:
            _v = self.parameters
            result["parameters"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
