# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union


from enum import Enum


class OpsType(str, Enum):
    """OpsType"""
    VERTICALSCALING = "VerticalScaling"
    HORIZONTALSCALING = "HorizontalScaling"
    VOLUMEEXPANSION = "VolumeExpansion"
    UPGRADE = "Upgrade"
    RECONFIGURING = "Reconfiguring"
    SWITCHOVER = "Switchover"
    RESTART = "Restart"
    STOP = "Stop"
    START = "Start"
    EXPOSE = "Expose"
    BACKUP = "Backup"
    RESTORE = "Restore"
    REBUILDINSTANCE = "RebuildInstance"
    CUSTOM = "Custom"
