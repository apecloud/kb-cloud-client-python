# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

import warnings
from typing import Any, Dict, List, Optional, Union

from kb_cloud_client.api_client import ApiClient, Endpoint as _Endpoint, UnsetType, unset
from kb_cloud_client.configuration import Configuration
from ..model import *  # noqa: F401, F403


class BackupmethodApi:
    """BackupMethod API client.

    Provides methods for the backupMethod endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_backup_method_endpoint = _Endpoint(
            settings={
                "response_type": ClusterBackupMethod,
                "endpoint_path": "/admin/v1/organizations/{orgName}/{engineName}/clusterBackupMethod",
                "http_method": "GET",
                "operation_id": "get_backup_method",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
                "cluster_id": {
                    "location": "query",
                    "attribute": "clusterID",
                },
                "enable_pitr": {
                    "location": "query",
                    "attribute": "enablePITR",
                },
                "with_rebuild_instance": {
                    "location": "query",
                    "attribute": "withRebuildInstance",
                },
                "with_h_scale": {
                    "location": "query",
                    "attribute": "withHScale",
                },
                "component": {
                    "location": "query",
                    "attribute": "component",
                },
            },
            headers_map={
                "accept": ["*/*", "application/json"],
            },
            api_client=api_client,
        )


    def get_backup_method(
        self,
        org_name: str,
        engine_name: str,
        *,
        cluster_id: Union[str, UnsetType] = unset,
        enable_pitr: Union[bool, UnsetType] = unset,
        with_rebuild_instance: Union[bool, UnsetType] = unset,
        with_h_scale: Union[bool, UnsetType] = unset,
        component: Union[str, UnsetType] = unset,
    ) -> ClusterBackupMethod:
        """get backup method.
        :param org_name: name of the org
        :type org_name: str
        :param engine_name: engine name
        :type engine_name: str
        :param cluster_id: clusterID is required when you want to get the backup method of a existing cluster
        :type cluster_id: str, optional
        :param enable_pitr: define whether to enable PITR (Point-In-Time Recovery). This setting is required when clusterId is not empty.
        :type enable_pitr: bool, optional
        :param with_rebuild_instance: defined whether to search for rebuilding instance.
        :type with_rebuild_instance: bool, optional
        :param with_h_scale: defined whether to search for rebuilding instance.
        :type with_h_scale: bool, optional
        :param component: The component type is required when withRebuildInstance/withHScale is true.
        :type component: str, optional
        :rtype: ClusterBackupMethod
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["engine_name"] = engine_name
        if cluster_id is not unset:
            kwargs["cluster_id"] = cluster_id
        if enable_pitr is not unset:
            kwargs["enable_pitr"] = enable_pitr
        if with_rebuild_instance is not unset:
            kwargs["with_rebuild_instance"] = with_rebuild_instance
        if with_h_scale is not unset:
            kwargs["with_h_scale"] = with_h_scale
        if component is not unset:
            kwargs["component"] = component
        return self._get_backup_method_endpoint.call_with_http_info(**kwargs)
