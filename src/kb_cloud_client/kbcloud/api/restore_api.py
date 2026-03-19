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


class RestoreApi:
    """Restore API client.

    Provides methods for the restore endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_restore_log_endpoint = _Endpoint(
            settings={
                "response_type": RestoreLog,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/restore/{restoreId}/logs",
                "http_method": "GET",
                "operation_id": "get_restore_log",
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
                "restore_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "restoreId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_restore_object_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/restore",
                "http_method": "DELETE",
                "operation_id": "delete_restore_object",
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
                "restore_name": {
                    "required": True,
                    "location": "query",
                    "attribute": "restoreName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._do_restore_endpoint = _Endpoint(
            settings={
                "response_type": Restore,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/restore",
                "http_method": "POST",
                "operation_id": "do_restore",
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
        self._get_restore_time_range_endpoint = _Endpoint(
            settings={
                "response_type": Backup,
                "endpoint_path": "/api/v1/organizations/{orgName}/clustersWithDelete/restoreTimeRange",
                "http_method": "GET",
                "operation_id": "get_restore_time_range",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "cluster_id": {
                    "required": True,
                    "location": "query",
                    "attribute": "clusterID",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_cluster_restore_endpoint = _Endpoint(
            settings={
                "response_type": RestoreList,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/restore",
                "http_method": "GET",
                "operation_id": "list_cluster_restore",
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
        self._list_restores_endpoint = _Endpoint(
            settings={
                "response_type": RestoreList,
                "endpoint_path": "/api/v1/organizations/{orgName}/restore",
                "http_method": "GET",
                "operation_id": "list_restores",
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
        self._restore_cluster_endpoint = _Endpoint(
            settings={
                "response_type": Cluster,
                "endpoint_path": "/api/v1/organizations/{orgName}/restore",
                "http_method": "POST",
                "operation_id": "restore_cluster",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
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


    def get_restore_log(
        self,
        org_name: str,
        cluster_name: str,
        restore_id: str,
    ) -> RestoreLog:
        """get restore workload logs of the cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :param restore_id: id of the restore
        :type restore_id: str
        :rtype: RestoreLog
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["restore_id"] = restore_id
        return self._get_restore_log_endpoint.call_with_http_info(**kwargs)

    def delete_restore_object(
        self,
        org_name: str,
        cluster_name: str,
        restore_name: str,
    ) -> APIErrorResponse:
        """Delete restore task.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :param restore_name: name of the restore
        :type restore_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["restore_name"] = restore_name
        return self._delete_restore_object_endpoint.call_with_http_info(**kwargs)

    def do_restore(
        self,
        org_name: str,
        cluster_name: str,
        body: Restore,
    ) -> Restore:
        """Restore current cluster or instance.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: Restore
        :rtype: Restore
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._do_restore_endpoint.call_with_http_info(**kwargs)

    def get_restore_time_range(
        self,
        org_name: str,
        cluster_id: str,
    ) -> Backup:
        """Get cluster restore time ragne.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_id: ID of the KubeBlocks cluster
        :type cluster_id: str
        :rtype: Backup
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_id"] = cluster_id
        return self._get_restore_time_range_endpoint.call_with_http_info(**kwargs)

    def list_cluster_restore(
        self,
        org_name: str,
        cluster_name: str,
    ) -> RestoreList:
        """List restore tasks.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :rtype: RestoreList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._list_cluster_restore_endpoint.call_with_http_info(**kwargs)

    def list_restores(
        self,
        org_name: str,
    ) -> RestoreList:
        """List restore tasks.
        :param org_name: name of the Org
        :type org_name: str
        :rtype: RestoreList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._list_restores_endpoint.call_with_http_info(**kwargs)

    def restore_cluster(
        self,
        org_name: str,
        body: RestoreCreate,
    ) -> Cluster:
        """Restore new cluster.
        :param org_name: name of the Org
        :type org_name: str
        :type body: RestoreCreate
        :rtype: Cluster
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._restore_cluster_endpoint.call_with_http_info(**kwargs)
