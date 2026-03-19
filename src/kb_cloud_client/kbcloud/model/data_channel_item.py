# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .channel_status import ChannelStatus
from .data_channel_list_endpoint import DataChannelListEndpoint
from .data_channel_object import DataChannelObject
from .event_object import EventObject


@dataclass
class DataChannelItem:
    """DataChannelItem"""
    # Required fields
    # Optional fields
    channel_id: Optional[str] = None
    channel_name: Optional[str] = None
    channel_status: Optional[ChannelStatus] = None
    environment_id: Optional[str] = None
    environment_name: Optional[str] = None
    project: Optional[str] = None
    kubernetes_name: Optional[str] = None
    standard_definition: Optional[str] = None
    source: Optional[DataChannelListEndpoint] = None
    target: Optional[DataChannelListEndpoint] = None
    replication_objects: Optional[DataChannelObject] = None
    modules: Optional[List[str]] = None
    events: Optional[List[EventObject]] = None
    created_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataChannelItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            channel_id=data.get("channelID"),
            channel_name=data.get("channelName"),
            channel_status=ChannelStatus.from_dict(data.get("channelStatus")) if isinstance(data.get("channelStatus"), dict) else data.get("channelStatus"),
            environment_id=data.get("environmentID"),
            environment_name=data.get("environmentName"),
            project=data.get("project"),
            kubernetes_name=data.get("kubernetesName"),
            standard_definition=data.get("standardDefinition"),
            source=DataChannelListEndpoint.from_dict(data.get("source")) if isinstance(data.get("source"), dict) else data.get("source"),
            target=DataChannelListEndpoint.from_dict(data.get("target")) if isinstance(data.get("target"), dict) else data.get("target"),
            replication_objects=DataChannelObject.from_dict(data.get("replicationObjects")) if isinstance(data.get("replicationObjects"), dict) else data.get("replicationObjects"),
            modules=data.get("modules"),
            events=[EventObject.from_dict(i) if isinstance(i, dict) else i for i in data.get("events")] if data.get("events") is not None else None,
            created_at=_parse_datetime(data.get("createdAt")),
            finished_at=_parse_datetime(data.get("FinishedAt")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.channel_id is not None:
            _v = self.channel_id
            result["channelID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.channel_name is not None:
            _v = self.channel_name
            result["channelName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.channel_status is not None:
            _v = self.channel_status
            result["channelStatus"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.environment_id is not None:
            _v = self.environment_id
            result["environmentID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.environment_name is not None:
            _v = self.environment_name
            result["environmentName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.project is not None:
            _v = self.project
            result["project"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.kubernetes_name is not None:
            _v = self.kubernetes_name
            result["kubernetesName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.finished_at is not None:
            _v = self.finished_at
            result["FinishedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
