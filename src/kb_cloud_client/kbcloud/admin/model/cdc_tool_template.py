# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cdc_config_format_type import CdcConfigFormatType
from .cdc_config_resource_type import CdcConfigResourceType


@dataclass
class CdcToolTemplate:
    """CdcToolTemplate"""
    # Required fields
    # Optional fields
    image: Optional[str] = None
    command: Optional[List[str]] = None
    args: Optional[List[str]] = None
    replicas: Optional[int] = None
    config_file_name: Optional[str] = None
    config_file_path: Optional[str] = None
    config_resource_type: Optional[CdcConfigResourceType] = None
    config_format: Optional[CdcConfigFormatType] = None
    local_recovery_enabled: Optional[bool] = None
    local_recovery_storage_class: Optional[str] = None
    local_recovery_storage_size: Optional[int] = None
    local_recovery_path: Optional[str] = None
    log_path: Optional[str] = None
    startup_timeout_minutes: Optional[int] = None
    properties: Optional[Dict[str, str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CdcToolTemplate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            image=data.get("image"),
            command=data.get("command"),
            args=data.get("args"),
            replicas=data.get("replicas"),
            config_file_name=data.get("configFileName"),
            config_file_path=data.get("configFilePath"),
            config_resource_type=CdcConfigResourceType.from_dict(data.get("configResourceType")) if isinstance(data.get("configResourceType"), dict) else data.get("configResourceType"),
            config_format=CdcConfigFormatType.from_dict(data.get("configFormat")) if isinstance(data.get("configFormat"), dict) else data.get("configFormat"),
            local_recovery_enabled=data.get("localRecoveryEnabled"),
            local_recovery_storage_class=data.get("localRecoveryStorageClass"),
            local_recovery_storage_size=data.get("localRecoveryStorageSize"),
            local_recovery_path=data.get("localRecoveryPath"),
            log_path=data.get("LogPath"),
            startup_timeout_minutes=data.get("startupTimeoutMinutes"),
            properties=data.get("properties"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.image is not None:
            _v = self.image
            result["image"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.command is not None:
            _v = self.command
            result["command"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.args is not None:
            _v = self.args
            result["args"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replicas is not None:
            _v = self.replicas
            result["replicas"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.config_file_name is not None:
            _v = self.config_file_name
            result["configFileName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.config_file_path is not None:
            _v = self.config_file_path
            result["configFilePath"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.config_resource_type is not None:
            _v = self.config_resource_type
            result["configResourceType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.config_format is not None:
            _v = self.config_format
            result["configFormat"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.local_recovery_enabled is not None:
            _v = self.local_recovery_enabled
            result["localRecoveryEnabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.local_recovery_storage_class is not None:
            _v = self.local_recovery_storage_class
            result["localRecoveryStorageClass"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.local_recovery_storage_size is not None:
            _v = self.local_recovery_storage_size
            result["localRecoveryStorageSize"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.local_recovery_path is not None:
            _v = self.local_recovery_path
            result["localRecoveryPath"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.log_path is not None:
            _v = self.log_path
            result["LogPath"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.startup_timeout_minutes is not None:
            _v = self.startup_timeout_minutes
            result["startupTimeoutMinutes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.properties is not None:
            _v = self.properties
            result["properties"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
