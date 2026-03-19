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
class MonitorDataSinkUpdate:
    """External Endpoint update option"""
    # Required fields
    monitor_data_sink_type: str
    environment_name: str
    # Optional fields
    exporter_url: Optional[str] = None
    name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    api_key: Optional[str] = None
    index_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MonitorDataSinkUpdate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            monitor_data_sink_type=data.get("monitorDataSinkType"),
            environment_name=data.get("environmentName"),
            exporter_url=data.get("exporterUrl"),
            name=data.get("name"),
            username=data.get("username"),
            password=data.get("password"),
            api_key=data.get("apiKey"),
            index_name=data.get("indexName"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.monitor_data_sink_type is not None:
            _v = self.monitor_data_sink_type
            result["monitorDataSinkType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.environment_name is not None:
            _v = self.environment_name
            result["environmentName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.exporter_url is not None:
            _v = self.exporter_url
            result["exporterUrl"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.api_key is not None:
            _v = self.api_key
            result["apiKey"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.index_name is not None:
            _v = self.index_name
            result["indexName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
