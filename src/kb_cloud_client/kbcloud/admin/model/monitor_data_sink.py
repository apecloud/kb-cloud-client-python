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
class MonitorDataSink:
    """MonitorDataSink"""
    # Required fields
    id_: str
    exporter_url: str
    environment_id: str
    monitor_data_sink_type: str
    # Optional fields
    index_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MonitorDataSink":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            exporter_url=data.get("exporterUrl"),
            environment_id=data.get("environmentID"),
            index_name=data.get("indexName"),
            monitor_data_sink_type=data.get("monitorDataSinkType"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.exporter_url is not None:
            _v = self.exporter_url
            result["exporterUrl"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.environment_id is not None:
            _v = self.environment_id
            result["environmentID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.index_name is not None:
            _v = self.index_name
            result["indexName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.monitor_data_sink_type is not None:
            _v = self.monitor_data_sink_type
            result["monitorDataSinkType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
