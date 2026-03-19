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


class BackupApi:
    """Backup API client.

    Provides methods for the backup endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_cluster_backup_endpoint = _Endpoint(
            settings={
                "response_type": Backup,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/backups",
                "http_method": "POST",
                "operation_id": "create_cluster_backup",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "cluster_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "clusterName",
                },
                "body": {
                    "required": True,
                    "location": "body",
                },
                "component": {
                    "location": "query",
                    "attribute": "component",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_backup_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/backups/{backupId}",
                "http_method": "DELETE",
                "operation_id": "delete_backup",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "backup_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "backupId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._download_backup_endpoint = _Endpoint(
            settings={
                "response_type": bytes,
                "endpoint_path": "/admin/v1/organizations/{orgName}/backups/{backupId}/download",
                "http_method": "GET",
                "operation_id": "download_backup",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "backup_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "backupId",
                },
            },
            headers_map={
                "accept": ["application/octet-stream"],
            },
            api_client=api_client,
        )
        self._download_multiple_backups_endpoint = _Endpoint(
            settings={
                "response_type": bytes,
                "endpoint_path": "/admin/v1/organizations/{orgName}/backups/{backupId}/download",
                "http_method": "POST",
                "operation_id": "download_multiple_backups",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "backup_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "backupId",
                },
                "body": {
                    "required": True,
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["application/octet-stream"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_backup_endpoint = _Endpoint(
            settings={
                "response_type": Backup,
                "endpoint_path": "/admin/v1/organizations/{orgName}/backups/{backupId}",
                "http_method": "GET",
                "operation_id": "get_backup",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "backup_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "backupId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_backup_log_endpoint = _Endpoint(
            settings={
                "response_type": BackupLog,
                "endpoint_path": "/admin/v1/organizations/{orgName}/backups/{backupId}/logs",
                "http_method": "GET",
                "operation_id": "get_backup_log",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "backup_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "backupId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_backup_stats_endpoint = _Endpoint(
            settings={
                "response_type": BackupStats,
                "endpoint_path": "/admin/v1/backupStats",
                "http_method": "GET",
                "operation_id": "get_backup_stats",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_cluster_backup_policy_endpoint = _Endpoint(
            settings={
                "response_type": BackupPolicy,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/backupPolicy",
                "http_method": "GET",
                "operation_id": "get_cluster_backup_policy",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "cluster_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "clusterName",
                },
                "use_volume_snapshot": {
                    "location": "query",
                    "attribute": "useVolumeSnapshot",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_backups_endpoint = _Endpoint(
            settings={
                "response_type": BackupList,
                "endpoint_path": "/admin/v1/backups",
                "http_method": "GET",
                "operation_id": "list_backups",
            },
            params_map={
                "org_name": {
                    "location": "query",
                    "attribute": "orgName",
                },
                "cluster_name": {
                    "location": "query",
                    "attribute": "clusterName",
                },
                "cluster_id": {
                    "location": "query",
                    "attribute": "clusterID",
                },
                "backup_repo": {
                    "location": "query",
                    "attribute": "backupRepo",
                },
                "fetch_with_deleted_cluster": {
                    "location": "query",
                    "attribute": "fetchWithDeletedCluster",
                },
                "with_deleted_backups": {
                    "location": "query",
                    "attribute": "withDeletedBackups",
                },
                "backup_type": {
                    "location": "query",
                    "attribute": "backupType",
                },
                "component_name": {
                    "location": "query",
                    "attribute": "componentName",
                },
                "page": {
                    "location": "query",
                    "attribute": "page",
                },
                "page_size": {
                    "location": "query",
                    "attribute": "pageSize",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_backup_policy_endpoint = _Endpoint(
            settings={
                "response_type": BackupPolicy,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/backupPolicy",
                "http_method": "PATCH",
                "operation_id": "update_backup_policy",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "cluster_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "clusterName",
                },
                "body": {
                    "required": True,
                    "location": "body",
                },
                "use_volume_snapshot": {
                    "location": "query",
                    "attribute": "useVolumeSnapshot",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._view_backup_endpoint = _Endpoint(
            settings={
                "response_type": FileEntryList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/backups/{backupId}/view",
                "http_method": "POST",
                "operation_id": "view_backup",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "backup_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "backupId",
                },
                "body": {
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["*/*", "application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )


    def create_cluster_backup(
        self,
        org_name: str,
        cluster_name: str,
        body: BackupCreate,
        *,
        component: Union[str, UnsetType] = unset,
    ) -> Backup:
        """Create backup.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: BackupCreate
        :param component: name of the component
        :type component: str, optional
        :rtype: Backup
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        if component is not unset:
            kwargs["component"] = component
        return self._create_cluster_backup_endpoint.call_with_http_info(**kwargs)

    def delete_backup(
        self,
        org_name: str,
        backup_id: str,
    ) -> APIErrorResponse:
        """Delete backup.
        :param org_name: name of the Org
        :type org_name: str
        :param backup_id: id of the Backup
        :type backup_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["backup_id"] = backup_id
        return self._delete_backup_endpoint.call_with_http_info(**kwargs)

    def download_backup(
        self,
        org_name: str,
        backup_id: str,
    ) -> bytes:
        """Download full backup.
        :param org_name: name of the org
        :type org_name: str
        :param backup_id: the id of backup
        :type backup_id: str
        :rtype: bytes
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["backup_id"] = backup_id
        return self._download_backup_endpoint.call_with_http_info(**kwargs)

    def download_multiple_backups(
        self,
        org_name: str,
        backup_id: str,
        body: BackupDownload,
    ) -> bytes:
        """Download multiple backup files.
        :param org_name: name of the org
        :type org_name: str
        :param backup_id: the id of backup
        :type backup_id: str
        :type body: BackupDownload
        :rtype: bytes
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["backup_id"] = backup_id
        kwargs["body"] = body
        return self._download_multiple_backups_endpoint.call_with_http_info(**kwargs)

    def get_backup(
        self,
        org_name: str,
        backup_id: str,
    ) -> Backup:
        """Get backup.
        :param org_name: name of the Org
        :type org_name: str
        :param backup_id: id of the Backup
        :type backup_id: str
        :rtype: Backup
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["backup_id"] = backup_id
        return self._get_backup_endpoint.call_with_http_info(**kwargs)

    def get_backup_log(
        self,
        org_name: str,
        backup_id: str,
    ) -> BackupLog:
        """Get backup log.
        :param org_name: name of the Org
        :type org_name: str
        :param backup_id: id of the Backup
        :type backup_id: str
        :rtype: BackupLog
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["backup_id"] = backup_id
        return self._get_backup_log_endpoint.call_with_http_info(**kwargs)

    def get_backup_stats(
        self,
    ) -> BackupStats:
        """Get backup statistics.
        :rtype: BackupStats
        """
        kwargs: Dict[str, Any] = {}
        return self._get_backup_stats_endpoint.call_with_http_info(**kwargs)

    def get_cluster_backup_policy(
        self,
        org_name: str,
        cluster_name: str,
        *,
        use_volume_snapshot: Union[bool, UnsetType] = unset,
    ) -> BackupPolicy:
        """Get backup policy.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :param use_volume_snapshot: use volume snapshot to back up
        :type use_volume_snapshot: bool, optional
        :rtype: BackupPolicy
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if use_volume_snapshot is not unset:
            kwargs["use_volume_snapshot"] = use_volume_snapshot
        return self._get_cluster_backup_policy_endpoint.call_with_http_info(**kwargs)

    def list_backups(
        self,
        *,
        org_name: Union[str, UnsetType] = unset,
        cluster_name: Union[str, UnsetType] = unset,
        cluster_id: Union[str, UnsetType] = unset,
        backup_repo: Union[str, UnsetType] = unset,
        fetch_with_deleted_cluster: Union[bool, UnsetType] = unset,
        with_deleted_backups: Union[bool, UnsetType] = unset,
        backup_type: Union[str, UnsetType] = unset,
        component_name: Union[str, UnsetType] = unset,
        page: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
    ) -> BackupList:
        """List backups.
        :param org_name: name of the Org
        :type org_name: str, optional
        :param cluster_name: cluster name of the Backup
        :type cluster_name: str, optional
        :param cluster_id: cluster ID of the Backup
        :type cluster_id: str, optional
        :param backup_repo: backup repo of the Backup
        :type backup_repo: str, optional
        :param fetch_with_deleted_cluster: defined whether to search for deleted clusters. if not set, returns all backups
        :type fetch_with_deleted_cluster: bool, optional
        :param with_deleted_backups: defined whether to search for deleted backups. if not set, only return backups that are not deleted
        :type with_deleted_backups: bool, optional
        :param backup_type: type of the backup
        :type backup_type: str, optional
        :param component_name: get the backups belong to the component
        :type component_name: str, optional
        :param page: page number
        :type page: int, optional
        :param page_size: page size
        :type page_size: int, optional
        :rtype: BackupList
        """
        kwargs: Dict[str, Any] = {}
        if org_name is not unset:
            kwargs["org_name"] = org_name
        if cluster_name is not unset:
            kwargs["cluster_name"] = cluster_name
        if cluster_id is not unset:
            kwargs["cluster_id"] = cluster_id
        if backup_repo is not unset:
            kwargs["backup_repo"] = backup_repo
        if fetch_with_deleted_cluster is not unset:
            kwargs["fetch_with_deleted_cluster"] = fetch_with_deleted_cluster
        if with_deleted_backups is not unset:
            kwargs["with_deleted_backups"] = with_deleted_backups
        if backup_type is not unset:
            kwargs["backup_type"] = backup_type
        if component_name is not unset:
            kwargs["component_name"] = component_name
        if page is not unset:
            kwargs["page"] = page
        if page_size is not unset:
            kwargs["page_size"] = page_size
        return self._list_backups_endpoint.call_with_http_info(**kwargs)

    def update_backup_policy(
        self,
        org_name: str,
        cluster_name: str,
        body: BackupPolicy,
        *,
        use_volume_snapshot: Union[bool, UnsetType] = unset,
    ) -> BackupPolicy:
        """Update backup policy.

        partially update the specified Backup Policy
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: BackupPolicy
        :param use_volume_snapshot: use volume snapshot to back up
        :type use_volume_snapshot: bool, optional
        :rtype: BackupPolicy
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        if use_volume_snapshot is not unset:
            kwargs["use_volume_snapshot"] = use_volume_snapshot
        return self._update_backup_policy_endpoint.call_with_http_info(**kwargs)

    def view_backup(
        self,
        org_name: str,
        backup_id: str,
        *,
        body: Union[BackupView, UnsetType] = unset,
    ) -> FileEntryList:
        """view backup info.
        :param org_name: name of the org
        :type org_name: str
        :param backup_id: the id of backup
        :type backup_id: str
        :type body: BackupView, optional
        :rtype: FileEntryList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["backup_id"] = backup_id
        if body is not unset:
            kwargs["body"] = body
        return self._view_backup_endpoint.call_with_http_info(**kwargs)
