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


class BackuprepoApi:
    """BackupRepo API client.

    Provides methods for the backupRepo endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._check_backup_repo_endpoint = _Endpoint(
            settings={
                "response_type": BackupRepoCheck,
                "endpoint_path": "/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}/check",
                "http_method": "GET",
                "operation_id": "check_backup_repo",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "backup_repo_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "backupRepoName",
                },
                "org_name": {
                    "location": "query",
                    "attribute": "orgName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._create_backup_repo_endpoint = _Endpoint(
            settings={
                "response_type": BackupRepo,
                "endpoint_path": "/admin/v1/environments/{environmentName}/backupRepo",
                "http_method": "POST",
                "operation_id": "create_backup_repo",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
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
        self._delete_backup_repo_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}",
                "http_method": "DELETE",
                "operation_id": "delete_backup_repo",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "backup_repo_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "backupRepoName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_backup_repo_endpoint = _Endpoint(
            settings={
                "response_type": BackupRepo,
                "endpoint_path": "/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}",
                "http_method": "GET",
                "operation_id": "get_backup_repo",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "backup_repo_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "backupRepoName",
                },
                "org_name": {
                    "location": "query",
                    "attribute": "orgName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_backup_repo_stats_endpoint = _Endpoint(
            settings={
                "response_type": BackupRepoStatsList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}/stats",
                "http_method": "GET",
                "operation_id": "list_backup_repo_stats",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "backup_repo_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "backupRepoName",
                },
                "start": {
                    "location": "query",
                    "attribute": "start",
                },
                "end": {
                    "location": "query",
                    "attribute": "end",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_backup_repos_endpoint = _Endpoint(
            settings={
                "response_type": BackupRepoList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/backupRepo",
                "http_method": "GET",
                "operation_id": "list_backup_repos",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_backup_repo_endpoint = _Endpoint(
            settings={
                "response_type": BackupRepo,
                "endpoint_path": "/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}",
                "http_method": "POST",
                "operation_id": "update_backup_repo",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "backup_repo_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "backupRepoName",
                },
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
        self._view_backup_repo_endpoint = _Endpoint(
            settings={
                "response_type": FileEntryList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}/view",
                "http_method": "POST",
                "operation_id": "view_backup_repo",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "backup_repo_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "backupRepoName",
                },
                "body": {
                    "required": True,
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["*/*", "application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )


    def check_backup_repo(
        self,
        environment_name: str,
        backup_repo_name: str,
        *,
        org_name: Union[str, UnsetType] = unset,
    ) -> BackupRepoCheck:
        """check backup repo.
        :param environment_name: name of the environment
        :type environment_name: str
        :param backup_repo_name: name of the BackupRepo
        :type backup_repo_name: str
        :param org_name: name of the organization
        :type org_name: str, optional
        :rtype: BackupRepoCheck
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["backup_repo_name"] = backup_repo_name
        if org_name is not unset:
            kwargs["org_name"] = org_name
        return self._check_backup_repo_endpoint.call_with_http_info(**kwargs)

    def create_backup_repo(
        self,
        environment_name: str,
        body: BackupRepoCreate,
    ) -> BackupRepo:
        """Create backup repo.
        :param environment_name: name of the environment
        :type environment_name: str
        :type body: BackupRepoCreate
        :rtype: BackupRepo
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["body"] = body
        return self._create_backup_repo_endpoint.call_with_http_info(**kwargs)

    def delete_backup_repo(
        self,
        environment_name: str,
        backup_repo_name: str,
    ) -> APIErrorResponse:
        """Delete backup repo.
        :param environment_name: name of the environment
        :type environment_name: str
        :param backup_repo_name: name of the BackupRepo
        :type backup_repo_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["backup_repo_name"] = backup_repo_name
        return self._delete_backup_repo_endpoint.call_with_http_info(**kwargs)

    def get_backup_repo(
        self,
        environment_name: str,
        backup_repo_name: str,
        *,
        org_name: Union[str, UnsetType] = unset,
    ) -> BackupRepo:
        """Get backup repo.
        :param environment_name: name of the environment
        :type environment_name: str
        :param backup_repo_name: name of the BackupRepo
        :type backup_repo_name: str
        :param org_name: name of the organization
        :type org_name: str, optional
        :rtype: BackupRepo
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["backup_repo_name"] = backup_repo_name
        if org_name is not unset:
            kwargs["org_name"] = org_name
        return self._get_backup_repo_endpoint.call_with_http_info(**kwargs)

    def list_backup_repo_stats(
        self,
        environment_name: str,
        backup_repo_name: str,
        *,
        start: Union[str, UnsetType] = unset,
        end: Union[str, UnsetType] = unset,
    ) -> BackupRepoStatsList:
        """list backup repo stats.
        :param environment_name: name of the environment
        :type environment_name: str
        :param backup_repo_name: name of the environment
        :type backup_repo_name: str
        :param start: the start time
        :type start: str, optional
        :param end: the end time
        :type end: str, optional
        :rtype: BackupRepoStatsList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["backup_repo_name"] = backup_repo_name
        if start is not unset:
            kwargs["start"] = start
        if end is not unset:
            kwargs["end"] = end
        return self._list_backup_repo_stats_endpoint.call_with_http_info(**kwargs)

    def list_backup_repos(
        self,
        environment_name: str,
    ) -> BackupRepoList:
        """List backup repos.
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: BackupRepoList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._list_backup_repos_endpoint.call_with_http_info(**kwargs)

    def update_backup_repo(
        self,
        environment_name: str,
        backup_repo_name: str,
        body: BackupRepoUpdate,
    ) -> BackupRepo:
        """Update backup repo.
        :param environment_name: name of the environment
        :type environment_name: str
        :param backup_repo_name: name of the BackupRepo
        :type backup_repo_name: str
        :type body: BackupRepoUpdate
        :rtype: BackupRepo
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["backup_repo_name"] = backup_repo_name
        kwargs["body"] = body
        return self._update_backup_repo_endpoint.call_with_http_info(**kwargs)

    def view_backup_repo(
        self,
        environment_name: str,
        backup_repo_name: str,
        body: BackupRepoView,
    ) -> FileEntryList:
        """view backup repo.
        :param environment_name: name of the environment
        :type environment_name: str
        :param backup_repo_name: name of the environment
        :type backup_repo_name: str
        :type body: BackupRepoView
        :rtype: FileEntryList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["backup_repo_name"] = backup_repo_name
        kwargs["body"] = body
        return self._view_backup_repo_endpoint.call_with_http_info(**kwargs)
