# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .alert_receiver_category import AlertReceiverCategory
from .webhook_config import WebhookConfig


@dataclass
class AlertReceiver:
    """Alert receiver information"""
    # Required fields
    # Optional fields
    created_at: Optional[datetime] = None
    id_: Optional[str] = None
    name: Optional[str] = None
    category: Optional[AlertReceiverCategory] = None
    updated_at: Optional[datetime] = None
    user_group: Optional[Dict[str, Any]] = None
    webhook_config: Optional[WebhookConfig] = None
    org_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AlertReceiver":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            created_at=_parse_datetime(data.get("createdAt")),
            id_=data.get("id"),
            name=data.get("name"),
            category=AlertReceiverCategory.from_dict(data.get("category")) if isinstance(data.get("category"), dict) else data.get("category"),
            updated_at=_parse_datetime(data.get("updatedAt")),
            user_group=data.get("userGroup"),
            webhook_config=WebhookConfig.from_dict(data.get("webhookConfig")) if isinstance(data.get("webhookConfig"), dict) else data.get("webhookConfig"),
            org_name=data.get("orgName"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.category is not None:
            _v = self.category
            result["category"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.updated_at is not None:
            _v = self.updated_at
            result["updatedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.user_group is not None:
            _v = self.user_group
            result["userGroup"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.webhook_config is not None:
            _v = self.webhook_config
            result["webhookConfig"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.org_name is not None:
            _v = self.org_name
            result["orgName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
