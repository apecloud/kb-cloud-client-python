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
class EngineVersionUpdate:
    """EngineVersionRecord update option"""
    # Required fields
    engine_name: str
    version: str
    # Optional fields
    kb_version_constraint: Optional[str] = None
    cluster_chart_url: Optional[str] = None
    chart_url: Optional[str] = None
    set_values: Optional[str] = None
    charts_image: Optional[str] = None
    set_image_registry: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EngineVersionUpdate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            engine_name=data.get("engineName"),
            version=data.get("version"),
            kb_version_constraint=data.get("kbVersionConstraint"),
            cluster_chart_url=data.get("clusterChartUrl"),
            chart_url=data.get("chartUrl"),
            set_values=data.get("setValues"),
            charts_image=data.get("chartsImage"),
            set_image_registry=data.get("setImageRegistry"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.engine_name is not None:
            _v = self.engine_name
            result["engineName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.version is not None:
            _v = self.version
            result["version"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.kb_version_constraint is not None:
            _v = self.kb_version_constraint
            result["kbVersionConstraint"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_chart_url is not None:
            _v = self.cluster_chart_url
            result["clusterChartUrl"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.chart_url is not None:
            _v = self.chart_url
            result["chartUrl"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.set_values is not None:
            _v = self.set_values
            result["setValues"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.charts_image is not None:
            _v = self.charts_image
            result["chartsImage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.set_image_registry is not None:
            _v = self.set_image_registry
            result["setImageRegistry"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
