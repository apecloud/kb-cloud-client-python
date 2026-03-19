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
class FileEntry:
    """the entry of files"""
    # Required fields
    # Optional fields
    is_dir: Optional[bool] = None
    full_path: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FileEntry":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            is_dir=data.get("IsDir"),
            full_path=data.get("fullPath"),
            filename=data.get("filename"),
            size=data.get("size"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.is_dir is not None:
            _v = self.is_dir
            result["IsDir"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.full_path is not None:
            _v = self.full_path
            result["fullPath"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.filename is not None:
            _v = self.filename
            result["filename"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.size is not None:
            _v = self.size
            result["size"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
