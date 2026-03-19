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
class HaHistory:
    """HA history is the records of HA operations, include `switchover` and `failover`"""
    # Required fields
    component_name: str
    type_: str
    old_primary: str
    new_primary: str
    status: str
    message: str
    start_at: datetime
    end_at: datetime
    created_at: datetime
    # Optional fields
    operator_id: Optional[str] = None
    operator_name: Optional[str] = None
    opsrequest_name: Optional[str] = None
    opsrequest_namespace: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "HaHistory":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            component_name=data.get("componentName"),
            type_=data.get("type"),
            old_primary=data.get("oldPrimary"),
            new_primary=data.get("newPrimary"),
            status=data.get("status"),
            message=data.get("message"),
            operator_id=data.get("operatorID"),
            operator_name=data.get("operatorName"),
            opsrequest_name=data.get("opsrequestName"),
            opsrequest_namespace=data.get("opsrequestNamespace"),
            start_at=_parse_datetime(data.get("startAt")),
            end_at=_parse_datetime(data.get("endAt")),
            created_at=_parse_datetime(data.get("createdAt")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.component_name is not None:
            _v = self.component_name
            result["componentName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.old_primary is not None:
            _v = self.old_primary
            result["oldPrimary"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.new_primary is not None:
            _v = self.new_primary
            result["newPrimary"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.message is not None:
            _v = self.message
            result["message"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.operator_id is not None:
            _v = self.operator_id
            result["operatorID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.operator_name is not None:
            _v = self.operator_name
            result["operatorName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.opsrequest_name is not None:
            _v = self.opsrequest_name
            result["opsrequestName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.opsrequest_namespace is not None:
            _v = self.opsrequest_namespace
            result["opsrequestNamespace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.start_at is not None:
            _v = self.start_at
            result["startAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.end_at is not None:
            _v = self.end_at
            result["endAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
