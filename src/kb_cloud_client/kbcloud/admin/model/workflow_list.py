# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .workflow import Workflow


@dataclass
class WorkflowList:
    """component management workflow list"""
    # Required fields
    # Optional fields
    install: Optional[Workflow] = None
    uninstall: Optional[Workflow] = None
    upgrade_kubeblocks: Optional[Workflow] = None
    upgrade_gemini: Optional[Workflow] = None
    upgrade_victoria_metrics: Optional[Workflow] = None
    upgrade_loki: Optional[Workflow] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "WorkflowList":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            install=Workflow.from_dict(data.get("install")) if isinstance(data.get("install"), dict) else data.get("install"),
            uninstall=Workflow.from_dict(data.get("uninstall")) if isinstance(data.get("uninstall"), dict) else data.get("uninstall"),
            upgrade_kubeblocks=Workflow.from_dict(data.get("upgradeKubeblocks")) if isinstance(data.get("upgradeKubeblocks"), dict) else data.get("upgradeKubeblocks"),
            upgrade_gemini=Workflow.from_dict(data.get("upgradeGemini")) if isinstance(data.get("upgradeGemini"), dict) else data.get("upgradeGemini"),
            upgrade_victoria_metrics=Workflow.from_dict(data.get("upgradeVictoriaMetrics")) if isinstance(data.get("upgradeVictoriaMetrics"), dict) else data.get("upgradeVictoriaMetrics"),
            upgrade_loki=Workflow.from_dict(data.get("upgradeLoki")) if isinstance(data.get("upgradeLoki"), dict) else data.get("upgradeLoki"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.install is not None:
            _v = self.install
            result["install"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.uninstall is not None:
            _v = self.uninstall
            result["uninstall"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.upgrade_kubeblocks is not None:
            _v = self.upgrade_kubeblocks
            result["upgradeKubeblocks"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.upgrade_gemini is not None:
            _v = self.upgrade_gemini
            result["upgradeGemini"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.upgrade_victoria_metrics is not None:
            _v = self.upgrade_victoria_metrics
            result["upgradeVictoriaMetrics"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.upgrade_loki is not None:
            _v = self.upgrade_loki
            result["upgradeLoki"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
