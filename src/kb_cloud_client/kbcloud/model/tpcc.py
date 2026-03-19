# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .tpcc_step import TpccStep


@dataclass
class Tpcc:
    """tpcc is the tpcc benchmark object"""
    # Required fields
    cluster: str
    database: str
    username: str
    password: str
    address: str
    # Optional fields
    step: Optional[TpccStep] = None
    limit_cpu: Optional[str] = None
    limit_memory: Optional[str] = None
    request_cpu: Optional[str] = None
    request_memory: Optional[str] = None
    name: Optional[str] = None
    threads: Optional[int] = None
    warehouses: Optional[int] = None
    duration: Optional[int] = None
    limit_tx_per_min: Optional[int] = None
    new_order_weight: Optional[int] = None
    payment_weight: Optional[int] = None
    order_status_weight: Optional[int] = None
    delivery_weight: Optional[int] = None
    stock_level_weight: Optional[int] = None
    load_workers: Optional[int] = None
    run_txns_per_terminal: Optional[int] = None
    extra_args: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Tpcc":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            step=TpccStep.from_dict(data.get("step")) if isinstance(data.get("step"), dict) else data.get("step"),
            limit_cpu=data.get("limitCpu"),
            limit_memory=data.get("limitMemory"),
            request_cpu=data.get("requestCpu"),
            request_memory=data.get("requestMemory"),
            name=data.get("name"),
            cluster=data.get("cluster"),
            database=data.get("database"),
            username=data.get("username"),
            password=data.get("password"),
            address=data.get("address"),
            threads=data.get("threads"),
            warehouses=data.get("warehouses"),
            duration=data.get("duration"),
            limit_tx_per_min=data.get("limitTxPerMin"),
            new_order_weight=data.get("newOrderWeight"),
            payment_weight=data.get("paymentWeight"),
            order_status_weight=data.get("orderStatusWeight"),
            delivery_weight=data.get("deliveryWeight"),
            stock_level_weight=data.get("stockLevelWeight"),
            load_workers=data.get("loadWorkers"),
            run_txns_per_terminal=data.get("runTxnsPerTerminal"),
            extra_args=data.get("extraArgs"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.step is not None:
            _v = self.step
            result["step"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.limit_cpu is not None:
            _v = self.limit_cpu
            result["limitCpu"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.limit_memory is not None:
            _v = self.limit_memory
            result["limitMemory"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.request_cpu is not None:
            _v = self.request_cpu
            result["requestCpu"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.request_memory is not None:
            _v = self.request_memory
            result["requestMemory"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster is not None:
            _v = self.cluster
            result["cluster"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.database is not None:
            _v = self.database
            result["database"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.username is not None:
            _v = self.username
            result["username"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.password is not None:
            _v = self.password
            result["password"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.address is not None:
            _v = self.address
            result["address"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.threads is not None:
            _v = self.threads
            result["threads"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.warehouses is not None:
            _v = self.warehouses
            result["warehouses"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.duration is not None:
            _v = self.duration
            result["duration"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.limit_tx_per_min is not None:
            _v = self.limit_tx_per_min
            result["limitTxPerMin"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.new_order_weight is not None:
            _v = self.new_order_weight
            result["newOrderWeight"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.payment_weight is not None:
            _v = self.payment_weight
            result["paymentWeight"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.order_status_weight is not None:
            _v = self.order_status_weight
            result["orderStatusWeight"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.delivery_weight is not None:
            _v = self.delivery_weight
            result["deliveryWeight"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.stock_level_weight is not None:
            _v = self.stock_level_weight
            result["stockLevelWeight"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.load_workers is not None:
            _v = self.load_workers
            result["loadWorkers"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.run_txns_per_terminal is not None:
            _v = self.run_txns_per_terminal
            result["runTxnsPerTerminal"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extra_args is not None:
            _v = self.extra_args
            result["extraArgs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
