# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .account_option import AccountOption
from .backup_option import BackupOption
from .bench_option import BenchOption
from .cdc_option import CdcOption
from .component_ops_option import ComponentOpsOption
from .component_option import ComponentOption
from .dashboard_option import DashboardOption
from .database_option import DatabaseOption
from .data_replication_option import DataReplicationOption
from .disaster_recovery_option import DisasterRecoveryOption
from .dms_option import DmsOption
from .endpoint_option import EndpointOption
from .engine_option_status import EngineOptionStatus
from .import_option import ImportOption
from .localized_description import LocalizedDescription
from .log_option import LogOption
from .metrics_option import MetricsOption
from .mode_option import ModeOption
from .network_mode_option import NetworkModeOption
from .parameter_option import ParameterOption


@dataclass
class EngineOption:
    """EngineOption"""
    # Required fields
    engine_name: str
    title: str
    description: LocalizedDescription
    versions: List[str]
    components: List[ComponentOption]
    modes: List[ModeOption]
    dms: DmsOption
    endpoints: List[EndpointOption]
    promote: List[ComponentOpsOption]
    stop: List[ComponentOpsOption]
    start: List[ComponentOpsOption]
    restart: List[ComponentOpsOption]
    hscale: List[ComponentOpsOption]
    vscale: List[ComponentOpsOption]
    dashboards: List[DashboardOption]
    logs: List[LogOption]
    parameters: List[ParameterOption]
    # Optional fields
    maturity_level: Optional[str] = None
    status: Optional[EngineOptionStatus] = None
    account: Optional[AccountOption] = None
    database: Optional[DatabaseOption] = None
    backup: Optional[BackupOption] = None
    bench: Optional[BenchOption] = None
    network_modes: Optional[List[Dict[str, Any]]] = None
    license: Optional[Dict[str, Any]] = None
    storage_expansion: Optional[List[ComponentOpsOption]] = None
    rebuild_instance: Optional[List[ComponentOpsOption]] = None
    upgrade: Optional[List[ComponentOpsOption]] = None
    metrics: Optional[MetricsOption] = None
    disaster_recovery: Optional[DisasterRecoveryOption] = None
    cdc: Optional[List[CdcOption]] = None
    data_replication: Optional[DataReplicationOption] = None
    import_: Optional[ImportOption] = None
    architectures: Optional[List[str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EngineOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            engine_name=data.get("engineName"),
            maturity_level=data.get("maturityLevel"),
            title=data.get("title"),
            status=EngineOptionStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
            description=LocalizedDescription.from_dict(data.get("description")) if isinstance(data.get("description"), dict) else data.get("description"),
            versions=data.get("versions"),
            components=[ComponentOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("components")] if data.get("components") is not None else None,
            modes=[ModeOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("modes")] if data.get("modes") is not None else None,
            account=AccountOption.from_dict(data.get("account")) if isinstance(data.get("account"), dict) else data.get("account"),
            database=DatabaseOption.from_dict(data.get("database")) if isinstance(data.get("database"), dict) else data.get("database"),
            dms=DmsOption.from_dict(data.get("dms")) if isinstance(data.get("dms"), dict) else data.get("dms"),
            backup=BackupOption.from_dict(data.get("backup")) if isinstance(data.get("backup"), dict) else data.get("backup"),
            bench=BenchOption.from_dict(data.get("bench")) if isinstance(data.get("bench"), dict) else data.get("bench"),
            endpoints=[EndpointOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("endpoints")] if data.get("endpoints") is not None else None,
            network_modes=NetworkModeOption.from_dict(data.get("networkModes")) if isinstance(data.get("networkModes"), dict) else data.get("networkModes"),
            promote=[ComponentOpsOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("promote")] if data.get("promote") is not None else None,
            stop=[ComponentOpsOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("stop")] if data.get("stop") is not None else None,
            start=[ComponentOpsOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("start")] if data.get("start") is not None else None,
            restart=[ComponentOpsOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("restart")] if data.get("restart") is not None else None,
            hscale=[ComponentOpsOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("hscale")] if data.get("hscale") is not None else None,
            vscale=[ComponentOpsOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("vscale")] if data.get("vscale") is not None else None,
            license=data.get("license"),
            storage_expansion=[ComponentOpsOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("storageExpansion")] if data.get("storageExpansion") is not None else None,
            rebuild_instance=[ComponentOpsOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("rebuildInstance")] if data.get("rebuildInstance") is not None else None,
            upgrade=[ComponentOpsOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("upgrade")] if data.get("upgrade") is not None else None,
            metrics=MetricsOption.from_dict(data.get("metrics")) if isinstance(data.get("metrics"), dict) else data.get("metrics"),
            dashboards=[DashboardOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("dashboards")] if data.get("dashboards") is not None else None,
            logs=[LogOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("logs")] if data.get("logs") is not None else None,
            parameters=[ParameterOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("parameters")] if data.get("parameters") is not None else None,
            disaster_recovery=DisasterRecoveryOption.from_dict(data.get("disasterRecovery")) if isinstance(data.get("disasterRecovery"), dict) else data.get("disasterRecovery"),
            cdc=[CdcOption.from_dict(i) if isinstance(i, dict) else i for i in data.get("cdc")] if data.get("cdc") is not None else None,
            data_replication=DataReplicationOption.from_dict(data.get("dataReplication")) if isinstance(data.get("dataReplication"), dict) else data.get("dataReplication"),
            import_=ImportOption.from_dict(data.get("import")) if isinstance(data.get("import"), dict) else data.get("import"),
            architectures=data.get("architectures"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.engine_name is not None:
            _v = self.engine_name
            result["engineName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.maturity_level is not None:
            _v = self.maturity_level
            result["maturityLevel"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.title is not None:
            _v = self.title
            result["title"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.versions is not None:
            _v = self.versions
            result["versions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.components is not None:
            _v = self.components
            result["components"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.modes is not None:
            _v = self.modes
            result["modes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.account is not None:
            _v = self.account
            result["account"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.database is not None:
            _v = self.database
            result["database"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.dms is not None:
            _v = self.dms
            result["dms"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup is not None:
            _v = self.backup
            result["backup"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.bench is not None:
            _v = self.bench
            result["bench"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.endpoints is not None:
            _v = self.endpoints
            result["endpoints"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.network_modes is not None:
            _v = self.network_modes
            result["networkModes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.promote is not None:
            _v = self.promote
            result["promote"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.stop is not None:
            _v = self.stop
            result["stop"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.start is not None:
            _v = self.start
            result["start"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.restart is not None:
            _v = self.restart
            result["restart"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.hscale is not None:
            _v = self.hscale
            result["hscale"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.vscale is not None:
            _v = self.vscale
            result["vscale"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.license is not None:
            _v = self.license
            result["license"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.storage_expansion is not None:
            _v = self.storage_expansion
            result["storageExpansion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.rebuild_instance is not None:
            _v = self.rebuild_instance
            result["rebuildInstance"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.upgrade is not None:
            _v = self.upgrade
            result["upgrade"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.metrics is not None:
            _v = self.metrics
            result["metrics"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.dashboards is not None:
            _v = self.dashboards
            result["dashboards"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.logs is not None:
            _v = self.logs
            result["logs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parameters is not None:
            _v = self.parameters
            result["parameters"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.disaster_recovery is not None:
            _v = self.disaster_recovery
            result["disasterRecovery"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cdc is not None:
            _v = self.cdc
            result["cdc"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.data_replication is not None:
            _v = self.data_replication
            result["dataReplication"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.import_ is not None:
            _v = self.import_
            result["import"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.architectures is not None:
            _v = self.architectures
            result["architectures"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
