# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .encryption_algorithm import EncryptionAlgorithm
from .encryption_key_usage import EncryptionKeyUsage


@dataclass
class Key:
    """mutiple kv pair"""
    # Required fields
    # Optional fields
    id_: Optional[str] = None
    name: Optional[str] = None
    algorithm: Optional[EncryptionAlgorithm] = None
    key_usage: Optional[EncryptionKeyUsage] = None
    clusters: Optional[List[str]] = None
    backups: Optional[List[str]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    data_key_name: Optional[str] = None
    sysmetric_key: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Key":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            name=data.get("name"),
            algorithm=EncryptionAlgorithm.from_dict(data.get("algorithm")) if isinstance(data.get("algorithm"), dict) else data.get("algorithm"),
            key_usage=EncryptionKeyUsage.from_dict(data.get("keyUsage")) if isinstance(data.get("keyUsage"), dict) else data.get("keyUsage"),
            clusters=data.get("clusters"),
            backups=data.get("backups"),
            created_at=_parse_datetime(data.get("createdAt")),
            updated_at=_parse_datetime(data.get("updatedAt")),
            data_key_name=data.get("dataKeyName"),
            sysmetric_key=data.get("sysmetricKey"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.algorithm is not None:
            _v = self.algorithm
            result["algorithm"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.key_usage is not None:
            _v = self.key_usage
            result["keyUsage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.clusters is not None:
            _v = self.clusters
            result["clusters"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backups is not None:
            _v = self.backups
            result["backups"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.data_key_name is not None:
            _v = self.data_key_name
            result["dataKeyName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.sysmetric_key is not None:
            _v = self.sysmetric_key
            result["sysmetricKey"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
