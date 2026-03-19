# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .ssh_config import SshConfig
from .ssh_node_spec import SshNodeSpec


@dataclass
class SshConfigCheckRequest:
    """SshConfigCheckRequest"""
    # Required fields
    nodes: List[SshNodeSpec]
    # Optional fields
    masters: Optional[List[SshNodeSpec]] = None
    default_ssh: Optional[SshConfig] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SshConfigCheckRequest":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            masters=[SshNodeSpec.from_dict(i) if isinstance(i, dict) else i for i in data.get("masters")] if data.get("masters") is not None else None,
            nodes=[SshNodeSpec.from_dict(i) if isinstance(i, dict) else i for i in data.get("nodes")] if data.get("nodes") is not None else None,
            default_ssh=SshConfig.from_dict(data.get("defaultSSH")) if isinstance(data.get("defaultSSH"), dict) else data.get("defaultSSH"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.masters is not None:
            _v = self.masters
            result["masters"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.nodes is not None:
            _v = self.nodes
            result["nodes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.default_ssh is not None:
            _v = self.default_ssh
            result["defaultSSH"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
