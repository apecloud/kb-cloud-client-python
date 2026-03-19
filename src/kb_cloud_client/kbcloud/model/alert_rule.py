# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .alert_metric import AlertMetric
from .alert_severity import AlertSeverity


@dataclass
class AlertRule:
    """Alert rule information. Either provide 'expr' for custom expressions, or 'metric' for predefined metrics."""
    # Required fields
    alert_name: str
    for_: str
    group_name: str
    severity: AlertSeverity
    # Optional fields
    description: Optional[str] = None
    summary: Optional[str] = None
    expr: Optional[str] = None
    disabled: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    metric: Optional[AlertMetric] = None
    org_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AlertRule":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            description=data.get("description"),
            summary=data.get("summary"),
            alert_name=data.get("alertName"),
            expr=data.get("expr"),
            for_=data.get("for"),
            group_name=data.get("groupName"),
            disabled=data.get("disabled"),
            severity=AlertSeverity.from_dict(data.get("severity")) if isinstance(data.get("severity"), dict) else data.get("severity"),
            created_at=_parse_datetime(data.get("createdAt")),
            updated_at=_parse_datetime(data.get("updatedAt")),
            metric=AlertMetric.from_dict(data.get("metric")) if isinstance(data.get("metric"), dict) else data.get("metric"),
            org_name=data.get("orgName"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.summary is not None:
            _v = self.summary
            result["summary"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.alert_name is not None:
            _v = self.alert_name
            result["alertName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.expr is not None:
            _v = self.expr
            result["expr"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.for_ is not None:
            _v = self.for_
            result["for"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.group_name is not None:
            _v = self.group_name
            result["groupName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.disabled is not None:
            _v = self.disabled
            result["disabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.severity is not None:
            _v = self.severity
            result["severity"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.metric is not None:
            _v = self.metric
            result["metric"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.org_name is not None:
            _v = self.org_name
            result["orgName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
