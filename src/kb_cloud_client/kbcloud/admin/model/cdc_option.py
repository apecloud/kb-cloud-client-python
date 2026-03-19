# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cdc_settings import CdcSettings
from .cdc_worker_template import CdcWorkerTemplate


@dataclass
class CdcOption:
    """CdcOption"""
    # Required fields
    # Optional fields
    versions: Optional[List[str]] = None
    source: Optional[CdcSettings] = None
    sink: Optional[CdcSettings] = None
    worker: Optional[CdcWorkerTemplate] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CdcOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            versions=data.get("versions"),
            source=CdcSettings.from_dict(data.get("source")) if isinstance(data.get("source"), dict) else data.get("source"),
            sink=CdcSettings.from_dict(data.get("sink")) if isinstance(data.get("sink"), dict) else data.get("sink"),
            worker=CdcWorkerTemplate.from_dict(data.get("worker")) if isinstance(data.get("worker"), dict) else data.get("worker"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.versions is not None:
            _v = self.versions
            result["versions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.source is not None:
            _v = self.source
            result["source"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.sink is not None:
            _v = self.sink
            result["sink"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.worker is not None:
            _v = self.worker
            result["worker"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
