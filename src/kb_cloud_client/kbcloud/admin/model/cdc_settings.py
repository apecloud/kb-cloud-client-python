# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cdc_cluster_account import CdcClusterAccount
from .cdc_cluster_config import CdcClusterConfig
from .cdc_cluster_endpoint import CdcClusterEndpoint
from .cdc_lifecycle import CdcLifecycle


@dataclass
class CdcSettings:
    """CdcSettings"""
    # Required fields
    # Optional fields
    config: Optional[CdcClusterConfig] = None
    account: Optional[CdcClusterAccount] = None
    endpoint: Optional[CdcClusterEndpoint] = None
    lifecycle: Optional[CdcLifecycle] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CdcSettings":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            config=CdcClusterConfig.from_dict(data.get("config")) if isinstance(data.get("config"), dict) else data.get("config"),
            account=CdcClusterAccount.from_dict(data.get("account")) if isinstance(data.get("account"), dict) else data.get("account"),
            endpoint=CdcClusterEndpoint.from_dict(data.get("endpoint")) if isinstance(data.get("endpoint"), dict) else data.get("endpoint"),
            lifecycle=CdcLifecycle.from_dict(data.get("lifecycle")) if isinstance(data.get("lifecycle"), dict) else data.get("lifecycle"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.config is not None:
            _v = self.config
            result["config"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.account is not None:
            _v = self.account
            result["account"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.endpoint is not None:
            _v = self.endpoint
            result["endpoint"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.lifecycle is not None:
            _v = self.lifecycle
            result["lifecycle"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
