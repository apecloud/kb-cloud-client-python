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


class StorageApi:
    """Storage API client.

    Provides methods for the storage endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._check_storage_endpoint = _Endpoint(
            settings={
                "response_type": StorageCheckResult,
                "endpoint_path": "/admin/v1/storageCheck",
                "http_method": "POST",
                "operation_id": "check_storage",
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
        self._create_storage_endpoint = _Endpoint(
            settings={
                "response_type": Storage,
                "endpoint_path": "/admin/v1/environments/{environmentName}/storages",
                "http_method": "POST",
                "operation_id": "create_storage",
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
        self._delete_storage_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/environments/{environmentName}/storages/{storageName}",
                "http_method": "DELETE",
                "operation_id": "delete_storage",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "storage_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "storageName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_storage_endpoint = _Endpoint(
            settings={
                "response_type": Storage,
                "endpoint_path": "/admin/v1/environments/{environmentName}/storages/{storageName}",
                "http_method": "GET",
                "operation_id": "get_storage",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "storage_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "storageName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._import_backup_endpoint = _Endpoint(
            settings={
                "response_type": BackupList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/storages/{storageName}/importbackup",
                "http_method": "POST",
                "operation_id": "import_backup",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "storage_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "storageName",
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
        self._list_storage_providers_endpoint = _Endpoint(
            settings={
                "response_type": List[StorageProvider],
                "endpoint_path": "/admin/v1/storageProviders",
                "http_method": "GET",
                "operation_id": "list_storage_providers",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_storages_endpoint = _Endpoint(
            settings={
                "response_type": List[Storage],
                "endpoint_path": "/admin/v1/environments/{environmentName}/storages",
                "http_method": "GET",
                "operation_id": "list_storages",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "name": {
                    "location": "query",
                    "attribute": "name",
                },
                "key": {
                    "location": "query",
                    "attribute": "key",
                },
                "value": {
                    "location": "query",
                    "attribute": "value",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_storage_endpoint = _Endpoint(
            settings={
                "response_type": Storage,
                "endpoint_path": "/admin/v1/environments/{environmentName}/storages/{storageName}",
                "http_method": "POST",
                "operation_id": "update_storage",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "storage_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "storageName",
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


    def check_storage(
        self,
        body: StorageCreate,
    ) -> StorageCheckResult:
        """Check if storage can be accessed.
        :type body: StorageCreate
        :rtype: StorageCheckResult
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._check_storage_endpoint.call_with_http_info(**kwargs)

    def create_storage(
        self,
        environment_name: str,
        body: StorageCreate,
    ) -> Storage:
        """Create a storage.
        :param environment_name: name of the environment
        :type environment_name: str
        :type body: StorageCreate
        :rtype: Storage
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["body"] = body
        return self._create_storage_endpoint.call_with_http_info(**kwargs)

    def delete_storage(
        self,
        environment_name: str,
        storage_name: str,
    ) -> APIErrorResponse:
        """Delete a storage.
        :param environment_name: name of the environment
        :type environment_name: str
        :param storage_name: name of the storage
        :type storage_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["storage_name"] = storage_name
        return self._delete_storage_endpoint.call_with_http_info(**kwargs)

    def get_storage(
        self,
        environment_name: str,
        storage_name: str,
    ) -> Storage:
        """Get a storage.
        :param environment_name: name of the environment
        :type environment_name: str
        :param storage_name: name of the storage
        :type storage_name: str
        :rtype: Storage
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["storage_name"] = storage_name
        return self._get_storage_endpoint.call_with_http_info(**kwargs)

    def import_backup(
        self,
        environment_name: str,
        storage_name: str,
        body: ImportBackup,
    ) -> BackupList:
        """scan and import backup records from storage.
        :param environment_name: name of the environment
        :type environment_name: str
        :param storage_name: name of the storage
        :type storage_name: str
        :type body: ImportBackup
        :rtype: BackupList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["storage_name"] = storage_name
        kwargs["body"] = body
        return self._import_backup_endpoint.call_with_http_info(**kwargs)

    def list_storage_providers(
        self,
    ) -> List[StorageProvider]:
        """List storage providers for storage.
        :rtype: List[StorageProvider]
        """
        kwargs: Dict[str, Any] = {}
        return self._list_storage_providers_endpoint.call_with_http_info(**kwargs)

    def list_storages(
        self,
        environment_name: str,
        *,
        name: Union[str, UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        value: Union[str, UnsetType] = unset,
    ) -> List[Storage]:
        """List storages.
        :param environment_name: name of the environment
        :type environment_name: str
        :param name: the search key to search storage's name
        :type name: str, optional
        :param key: key to search storage's tag
        :type key: str, optional
        :param value: value to search storage's tag
        :type value: str, optional
        :rtype: List[Storage]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        if name is not unset:
            kwargs["name"] = name
        if key is not unset:
            kwargs["key"] = key
        if value is not unset:
            kwargs["value"] = value
        return self._list_storages_endpoint.call_with_http_info(**kwargs)

    def update_storage(
        self,
        environment_name: str,
        storage_name: str,
        body: StorageUpdate,
    ) -> Storage:
        """Update a storage.
        :param environment_name: name of the environment
        :type environment_name: str
        :param storage_name: name of storage
        :type storage_name: str
        :type body: StorageUpdate
        :rtype: Storage
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["storage_name"] = storage_name
        kwargs["body"] = body
        return self._update_storage_endpoint.call_with_http_info(**kwargs)
