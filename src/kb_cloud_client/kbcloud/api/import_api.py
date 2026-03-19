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


class ImportApi:
    """Import API client.

    Provides methods for the import endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_import_task_endpoint = _Endpoint(
            settings={
                "response_type": ImportTaskResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/import",
                "http_method": "POST",
                "operation_id": "create_import_task",
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
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_import_task_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/import/{id}",
                "http_method": "DELETE",
                "operation_id": "delete_import_task",
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
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._get_import_preflight_task_endpoint = _Endpoint(
            settings={
                "response_type": PreCheckTaskDetail,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/import/preflight/{taskId}",
                "http_method": "GET",
                "operation_id": "get_import_preflight_task",
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
                "task_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "taskId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_import_task_endpoint = _Endpoint(
            settings={
                "response_type": ImportTaskResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/import/{id}",
                "http_method": "GET",
                "operation_id": "get_import_task",
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
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._import_preflight_endpoint = _Endpoint(
            settings={
                "response_type": PreCheckTaskResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/import/preflight",
                "http_method": "POST",
                "operation_id": "import_preflight",
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
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_import_task_endpoint = _Endpoint(
            settings={
                "response_type": ImportTaskListResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/import",
                "http_method": "GET",
                "operation_id": "list_import_task",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._query_import_objects_endpoint = _Endpoint(
            settings={
                "response_type": ReplicationObjectTree,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/import/objects",
                "http_method": "POST",
                "operation_id": "query_import_objects",
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
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_import_task_ops_endpoint = _Endpoint(
            settings={
                "response_type": ImportTaskResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/import/{id}/ops/{opsType}",
                "http_method": "PATCH",
                "operation_id": "update_import_task_ops",
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
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
                "ops_type": {
                    "required": True,
                    "location": "path",
                    "attribute": "opsType",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def create_import_task(
        self,
        org_name: str,
        cluster_name: str,
        body: ImportTaskCreateRequest,
    ) -> ImportTaskResponse:
        """Create import task.

        Creates new data import task based on data source configuration and import options
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :param body: Import task configuration including data source connection, object selection and import options
        :type body: ImportTaskCreateRequest
        :rtype: ImportTaskResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._create_import_task_endpoint.call_with_http_info(**kwargs)

    def delete_import_task(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
    ) -> APIErrorResponse:
        """Delete import task.

        Stops and deletes specified import task, will clean up related Kubernetes resources
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :param id_: Import task ID
        :type id_: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        return self._delete_import_task_endpoint.call_with_http_info(**kwargs)

    def get_import_preflight_task(
        self,
        org_name: str,
        cluster_name: str,
        task_id: str,
    ) -> PreCheckTaskDetail:
        """Get preflight task details.

        Retrieves detailed information about a specific data import preflight task by its ID
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :param task_id: Preflight task ID
        :type task_id: str
        :rtype: PreCheckTaskDetail
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["task_id"] = task_id
        return self._get_import_preflight_task_endpoint.call_with_http_info(**kwargs)

    def get_import_task(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
    ) -> ImportTaskResponse:
        """Get import task details.

        Gets detailed information about a specific import task by its ID
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :param id_: Import task ID
        :type id_: str
        :rtype: ImportTaskResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        return self._get_import_task_endpoint.call_with_http_info(**kwargs)

    def import_preflight(
        self,
        org_name: str,
        cluster_name: str,
        body: ImportPreflightRequest,
    ) -> PreCheckTaskResponse:
        """Data source preflight check.

        Initiates async validation with the selected source configuration
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :param body: Data source connection configuration and selection rules
        :type body: ImportPreflightRequest
        :rtype: PreCheckTaskResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._import_preflight_endpoint.call_with_http_info(**kwargs)

    def list_import_task(
        self,
        org_name: str,
        cluster_name: str,
    ) -> ImportTaskListResponse:
        """Query import task list.

        Gets import task list for specified cluster, supports filtering by status and pagination
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :rtype: ImportTaskListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._list_import_task_endpoint.call_with_http_info(**kwargs)

    def query_import_objects(
        self,
        org_name: str,
        cluster_name: str,
        body: ImportQueryObjectsRequest,
    ) -> ReplicationObjectTree:
        """Query replication objects for import.

        Enumerates replication objects (databases, schemas, tables, etc.) for the requested node. The metadata levels depend on the source engine (for example MySQL uses `database -> table`, PostgreSQL uses `schema -> table`).
        
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :param body: Connection configuration and current object tree position
        :type body: ImportQueryObjectsRequest
        :rtype: ReplicationObjectTree
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._query_import_objects_endpoint.call_with_http_info(**kwargs)

    def update_import_task_ops(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
        ops_type: ImportOpsType,
    ) -> ImportTaskResponse:
        """Create a import task operation.

        Performs pause or resume operation on import task based on opsType parameter
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :param id_: Import task ID
        :type id_: str
        :param ops_type: Operation type
        :type ops_type: ImportOpsType
        :rtype: ImportTaskResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        kwargs["ops_type"] = ops_type
        return self._update_import_task_ops_endpoint.call_with_http_info(**kwargs)
