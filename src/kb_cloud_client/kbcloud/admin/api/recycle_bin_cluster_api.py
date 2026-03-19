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


class RecyclebinclusterApi:
    """RecycleBinCluster API client.

    Provides methods for the recycleBinCluster endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._delete_recycle_bin_cluster_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/recycleBin/clusters/{clusterName}",
                "http_method": "DELETE",
                "operation_id": "delete_recycle_bin_cluster",
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
                "is_delete_backup": {
                    "required": True,
                    "location": "query",
                    "attribute": "isDeleteBackup",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_recycle_bin_cluster_endpoint = _Endpoint(
            settings={
                "response_type": RecycleBinCluster,
                "endpoint_path": "/admin/v1/organizations/{orgName}/recycleBin/clusters/{clusterName}",
                "http_method": "GET",
                "operation_id": "get_recycle_bin_cluster",
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
        self._list_recycle_bin_cluster_endpoint = _Endpoint(
            settings={
                "response_type": RecycleBinClusterList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/recycleBin/clusters",
                "http_method": "GET",
                "operation_id": "list_recycle_bin_cluster",
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
        self._list_recycle_bin_clusters_endpoint = _Endpoint(
            settings={
                "response_type": RecycleBinClusterList,
                "endpoint_path": "/admin/v1/recycleBin/clusters",
                "http_method": "GET",
                "operation_id": "list_recycle_bin_clusters",
                "deprecated": True,
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._restore_recycle_bin_cluster_endpoint = _Endpoint(
            settings={
                "response_type": Cluster,
                "endpoint_path": "/admin/v1/organizations/{orgName}/recycleBin/clusters/{clusterName}/restore",
                "http_method": "POST",
                "operation_id": "restore_recycle_bin_cluster",
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


    def delete_recycle_bin_cluster(
        self,
        org_name: str,
        cluster_name: str,
        is_delete_backup: bool,
    ) -> APIErrorResponse:
        """Delete cluster from the Recycle Bin of the Org.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param is_delete_backup: whether to delete the backup of the cluster
        :type is_delete_backup: bool
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["is_delete_backup"] = is_delete_backup
        return self._delete_recycle_bin_cluster_endpoint.call_with_http_info(**kwargs)

    def get_recycle_bin_cluster(
        self,
        org_name: str,
        cluster_name: str,
    ) -> RecycleBinCluster:
        """Get cluster in the Recycle Bin of the Org.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :rtype: RecycleBinCluster
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._get_recycle_bin_cluster_endpoint.call_with_http_info(**kwargs)

    def list_recycle_bin_cluster(
        self,
        org_name: str,
    ) -> RecycleBinClusterList:
        """List clusters in the Recycle Bin of the Org.
        :param org_name: name of the Org
        :type org_name: str
        :rtype: RecycleBinClusterList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._list_recycle_bin_cluster_endpoint.call_with_http_info(**kwargs)

    def list_recycle_bin_clusters(
        self,
    ) -> RecycleBinClusterList:
        """List all clusters in the Recycle Bin.
        :rtype: RecycleBinClusterList
        """
        warnings.warn("list_recycle_bin_clusters is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        return self._list_recycle_bin_clusters_endpoint.call_with_http_info(**kwargs)

    def restore_recycle_bin_cluster(
        self,
        org_name: str,
        cluster_name: str,
    ) -> Cluster:
        """Restore cluster from the Recycle Bin of the Org.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :rtype: Cluster
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._restore_recycle_bin_cluster_endpoint.call_with_http_info(**kwargs)
