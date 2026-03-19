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
        self._get_backup_repo_endpoint = _Endpoint(
            settings={
                "response_type": BackupRepo,
                "endpoint_path": "/api/v1/environments/{environmentName}/backupRepo/{backupRepoName}",
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
        self._list_backup_repos_endpoint = _Endpoint(
            settings={
                "response_type": BackupRepoList,
                "endpoint_path": "/api/v1/organizations/{orgName}/backupRepo",
                "http_method": "GET",
                "operation_id": "list_backup_repos",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


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

    def list_backup_repos(
        self,
        org_name: str,
    ) -> BackupRepoList:
        """List backup repos.
        :param org_name: name of the organization
        :type org_name: str
        :rtype: BackupRepoList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._list_backup_repos_endpoint.call_with_http_info(**kwargs)
