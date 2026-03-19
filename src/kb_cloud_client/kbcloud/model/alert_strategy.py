# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .alert_receiver import AlertReceiver
from .alter_rule_ref import AlterRuleRef


@dataclass
class AlertStrategy:
    """Alert strategy information"""
    # Required fields
    receiver_ids: List[int]
    # Optional fields
    id_: Optional[int] = None
    org_name: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    receivers: Optional[List[AlertReceiver]] = None
    envs: Optional[List[str]] = None
    severities: Optional[List[str]] = None
    rules: Optional[List[str]] = None
    rule_objs: Optional[List[AlterRuleRef]] = None
    engines: Optional[List[str]] = None
    clusters: Optional[List[str]] = None
    disabled: Optional[bool] = None
    repeat_interval: Optional[str] = None
    mute_time_interval: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AlertStrategy":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            org_name=data.get("orgName"),
            name=data.get("name"),
            description=data.get("description"),
            created_at=_parse_datetime(data.get("createdAt")),
            updated_at=_parse_datetime(data.get("updatedAt")),
            receiver_ids=data.get("receiverIds"),
            receivers=[AlertReceiver.from_dict(i) if isinstance(i, dict) else i for i in data.get("receivers")] if data.get("receivers") is not None else None,
            envs=data.get("envs"),
            severities=data.get("severities"),
            rules=data.get("rules"),
            rule_objs=[AlterRuleRef.from_dict(i) if isinstance(i, dict) else i for i in data.get("ruleObjs")] if data.get("ruleObjs") is not None else None,
            engines=data.get("engines"),
            clusters=data.get("clusters"),
            disabled=data.get("disabled"),
            repeat_interval=data.get("repeatInterval"),
            mute_time_interval=data.get("muteTimeInterval"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.org_name is not None:
            _v = self.org_name
            result["orgName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.updated_at is not None:
            _v = self.updated_at
            result["updatedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.receiver_ids is not None:
            _v = self.receiver_ids
            result["receiverIds"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.receivers is not None:
            _v = self.receivers
            result["receivers"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.envs is not None:
            _v = self.envs
            result["envs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.severities is not None:
            _v = self.severities
            result["severities"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.rules is not None:
            _v = self.rules
            result["rules"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.rule_objs is not None:
            _v = self.rule_objs
            result["ruleObjs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.engines is not None:
            _v = self.engines
            result["engines"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.clusters is not None:
            _v = self.clusters
            result["clusters"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.disabled is not None:
            _v = self.disabled
            result["disabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.repeat_interval is not None:
            _v = self.repeat_interval
            result["repeatInterval"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mute_time_interval is not None:
            _v = self.mute_time_interval
            result["muteTimeInterval"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
