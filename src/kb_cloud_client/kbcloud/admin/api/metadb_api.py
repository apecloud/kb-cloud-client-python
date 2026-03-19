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


class MetadbApi:
    """Metadb API client.

    Provides methods for the metadb endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._delete_metadb_backups_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/metadb/backups",
                "http_method": "DELETE",
                "operation_id": "delete_metadb_backups",
                "deprecated": True,
            },
            params_map={
                "all": {
                    "required": True,
                    "location": "query",
                    "attribute": "all",
                },
                "backup_name": {
                    "location": "query",
                    "attribute": "backupName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_metadb_instances_metrics_endpoint = _Endpoint(
            settings={
                "response_type": Metadb_instanceMetricsList,
                "endpoint_path": "/admin/v1/metadb/instancesMetrics",
                "http_method": "GET",
                "operation_id": "get_metadb_instances_metrics",
                "deprecated": True,
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_postgres_cluster_info_endpoint = _Endpoint(
            settings={
                "response_type": Summary,
                "endpoint_path": "/admin/v1/metadb/summary",
                "http_method": "GET",
                "operation_id": "get_postgres_cluster_info",
                "deprecated": True,
            },
            params_map={
                "cluster_name": {
                    "location": "query",
                    "attribute": "clusterName",
                },
                "namespace": {
                    "location": "query",
                    "attribute": "namespace",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_metadb_backups_endpoint = _Endpoint(
            settings={
                "response_type": Metadb_backupList,
                "endpoint_path": "/admin/v1/metadb/backups",
                "http_method": "GET",
                "operation_id": "list_metadb_backups",
                "deprecated": True,
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._metadb_backup_endpoint = _Endpoint(
            settings={
                "response_type": Metadb_backup,
                "endpoint_path": "/admin/v1/metadb/backups",
                "http_method": "POST",
                "operation_id": "metadb_backup",
                "deprecated": True,
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._metadb_backup_config_endpoint = _Endpoint(
            settings={
                "response_type": BackupConfig,
                "endpoint_path": "/admin/v1/metadb/backupConfig",
                "http_method": "PATCH",
                "operation_id": "metadb_backup_config",
                "deprecated": True,
            },
            params_map={
                "body": {
                    "required": True,
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._metadb_backup_get_config_endpoint = _Endpoint(
            settings={
                "response_type": BackupConfig,
                "endpoint_path": "/admin/v1/metadb/backupConfig",
                "http_method": "GET",
                "operation_id": "metadb_backup_get_config",
                "deprecated": True,
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._metadb_list_instances_endpoint = _Endpoint(
            settings={
                "response_type": Metadb_instanceList,
                "endpoint_path": "/admin/v1/metadb/instances",
                "http_method": "GET",
                "operation_id": "metadb_list_instances",
                "deprecated": True,
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._metadb_restore_endpoint = _Endpoint(
            settings={
                "response_type": Metadb_restore,
                "endpoint_path": "/admin/v1/metadb/restore",
                "http_method": "POST",
                "operation_id": "metadb_restore",
                "deprecated": True,
            },
            params_map={
                "body": {
                    "required": True,
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._metadb_vertical_scale_endpoint = _Endpoint(
            settings={
                "response_type": Vscale,
                "endpoint_path": "/admin/v1/metadb/vscale",
                "http_method": "POST",
                "operation_id": "metadb_vertical_scale",
                "deprecated": True,
            },
            params_map={
                "body": {
                    "required": True,
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._metadb_volume_expand_endpoint = _Endpoint(
            settings={
                "response_type": VolumeExpand,
                "endpoint_path": "/admin/v1/metadb/volumeExpand",
                "http_method": "POST",
                "operation_id": "metadb_volume_expand",
                "deprecated": True,
            },
            params_map={
                "body": {
                    "required": True,
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )


    def delete_metadb_backups(
        self,
        all: str,
        *,
        backup_name: Union[str, UnsetType] = unset,
    ) -> APIErrorResponse:
        """Delete backups by name or delete all.
        :param all: Delete all backups in the storage
        :type all: str
        :param backup_name: Delete target backup by name
        :type backup_name: str, optional
        :rtype: APIErrorResponse
        """
        warnings.warn("delete_metadb_backups is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["all"] = all
        if backup_name is not unset:
            kwargs["backup_name"] = backup_name
        return self._delete_metadb_backups_endpoint.call_with_http_info(**kwargs)

    def get_metadb_instances_metrics(
        self,
    ) -> Metadb_instanceMetricsList:
        """Get instances metrics in metadb.
        :rtype: Metadb_instanceMetricsList
        """
        warnings.warn("get_metadb_instances_metrics is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        return self._get_metadb_instances_metrics_endpoint.call_with_http_info(**kwargs)

    def get_postgres_cluster_info(
        self,
        *,
        cluster_name: Union[str, UnsetType] = unset,
        namespace: Union[str, UnsetType] = unset,
    ) -> Summary:
        """Get summary of postgresql cluster..
        :param cluster_name: name of the cluster
        :type cluster_name: str, optional
        :param namespace: namespace of the cluster
        :type namespace: str, optional
        :rtype: Summary
        """
        warnings.warn("get_postgres_cluster_info is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        if cluster_name is not unset:
            kwargs["cluster_name"] = cluster_name
        if namespace is not unset:
            kwargs["namespace"] = namespace
        return self._get_postgres_cluster_info_endpoint.call_with_http_info(**kwargs)

    def list_metadb_backups(
        self,
    ) -> Metadb_backupList:
        """List all names of backups in S3..
        :rtype: Metadb_backupList
        """
        warnings.warn("list_metadb_backups is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        return self._list_metadb_backups_endpoint.call_with_http_info(**kwargs)

    def metadb_backup(
        self,
    ) -> Metadb_backup:
        """Backup metadb to S3(AWS S3 or minio).
        :rtype: Metadb_backup
        """
        warnings.warn("metadb_backup is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        return self._metadb_backup_endpoint.call_with_http_info(**kwargs)

    def metadb_backup_config(
        self,
        body: BackupConfig,
    ) -> BackupConfig:
        """set backup config.
        :type body: BackupConfig
        :rtype: BackupConfig
        """
        warnings.warn("metadb_backup_config is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._metadb_backup_config_endpoint.call_with_http_info(**kwargs)

    def metadb_backup_get_config(
        self,
    ) -> BackupConfig:
        """get backup config.
        :rtype: BackupConfig
        """
        warnings.warn("metadb_backup_get_config is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        return self._metadb_backup_get_config_endpoint.call_with_http_info(**kwargs)

    def metadb_list_instances(
        self,
    ) -> Metadb_instanceList:
        """List metadb cluster instances.
        :rtype: Metadb_instanceList
        """
        warnings.warn("metadb_list_instances is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        return self._metadb_list_instances_endpoint.call_with_http_info(**kwargs)

    def metadb_restore(
        self,
        body: Metadb_restore,
    ) -> Metadb_restore:
        """Restore metadb.
        :type body: Metadb_restore
        :rtype: Metadb_restore
        """
        warnings.warn("metadb_restore is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._metadb_restore_endpoint.call_with_http_info(**kwargs)

    def metadb_vertical_scale(
        self,
        body: Vscale,
    ) -> Vscale:
        """vertical scale.
        :type body: Vscale
        :rtype: Vscale
        """
        warnings.warn("metadb_vertical_scale is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._metadb_vertical_scale_endpoint.call_with_http_info(**kwargs)

    def metadb_volume_expand(
        self,
        body: VolumeExpand,
    ) -> VolumeExpand:
        """Expand cluster volume size.
        :type body: VolumeExpand
        :rtype: VolumeExpand
        """
        warnings.warn("metadb_volume_expand is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._metadb_volume_expand_endpoint.call_with_http_info(**kwargs)
