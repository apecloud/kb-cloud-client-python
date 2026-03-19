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
class AlertTemplate:
    """Alert template"""
    # Required fields
    name: str
    # Optional fields
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    email_subject: Optional[str] = None
    email_text: Optional[str] = None
    feishu_text: Optional[str] = None
    feishu_title: Optional[str] = None
    dingding_text: Optional[str] = None
    dingding_title: Optional[str] = None
    weixin_text: Optional[str] = None
    weixin_title: Optional[str] = None
    webhook_text: Optional[str] = None
    webhook_title: Optional[str] = None
    id_: Optional[str] = None
    updated_at: Optional[datetime] = None
    is_default: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AlertTemplate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            created_at=_parse_datetime(data.get("createdAt")),
            description=data.get("description"),
            email_subject=data.get("emailSubject"),
            email_text=data.get("emailText"),
            feishu_text=data.get("feishuText"),
            feishu_title=data.get("feishuTitle"),
            dingding_text=data.get("dingdingText"),
            dingding_title=data.get("dingdingTitle"),
            weixin_text=data.get("weixinText"),
            weixin_title=data.get("weixinTitle"),
            webhook_text=data.get("webhookText"),
            webhook_title=data.get("webhookTitle"),
            id_=data.get("id"),
            name=data.get("name"),
            updated_at=_parse_datetime(data.get("updatedAt")),
            is_default=data.get("isDefault"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.email_subject is not None:
            _v = self.email_subject
            result["emailSubject"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.email_text is not None:
            _v = self.email_text
            result["emailText"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.feishu_text is not None:
            _v = self.feishu_text
            result["feishuText"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.feishu_title is not None:
            _v = self.feishu_title
            result["feishuTitle"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.dingding_text is not None:
            _v = self.dingding_text
            result["dingdingText"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.dingding_title is not None:
            _v = self.dingding_title
            result["dingdingTitle"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.weixin_text is not None:
            _v = self.weixin_text
            result["weixinText"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.weixin_title is not None:
            _v = self.weixin_title
            result["weixinTitle"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.webhook_text is not None:
            _v = self.webhook_text
            result["webhookText"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.webhook_title is not None:
            _v = self.webhook_title
            result["webhookTitle"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.updated_at is not None:
            _v = self.updated_at
            result["updatedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.is_default is not None:
            _v = self.is_default
            result["isDefault"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
