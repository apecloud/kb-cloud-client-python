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
class GlobalPricing:
    """the global information of pricing"""
    # Required fields
    # Optional fields
    enabled: Optional[bool] = None
    currency_unit: Optional[str] = None
    bill_schedule_time: Optional[str] = None
    last_billing_time: Optional[datetime] = None
    cpu_price: Optional[str] = None
    memory_price: Optional[str] = None
    storage_price: Optional[str] = None
    timezone: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GlobalPricing":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            enabled=data.get("enabled"),
            currency_unit=data.get("currencyUnit"),
            bill_schedule_time=data.get("billScheduleTime"),
            last_billing_time=_parse_datetime(data.get("lastBillingTime")),
            cpu_price=data.get("cpuPrice"),
            memory_price=data.get("memoryPrice"),
            storage_price=data.get("storagePrice"),
            timezone=data.get("timezone"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.enabled is not None:
            _v = self.enabled
            result["enabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.currency_unit is not None:
            _v = self.currency_unit
            result["currencyUnit"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.bill_schedule_time is not None:
            _v = self.bill_schedule_time
            result["billScheduleTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.last_billing_time is not None:
            _v = self.last_billing_time
            result["lastBillingTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu_price is not None:
            _v = self.cpu_price
            result["cpuPrice"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory_price is not None:
            _v = self.memory_price
            result["memoryPrice"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.storage_price is not None:
            _v = self.storage_price
            result["storagePrice"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.timezone is not None:
            _v = self.timezone
            result["timezone"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
