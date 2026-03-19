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


class RelationApi:
    """Relation API client.

    Provides methods for the relation endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_relation_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/relations",
                "http_method": "POST",
                "operation_id": "create_relation",
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
                "target": {
                    "required": True,
                    "location": "query",
                    "attribute": "target",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._delete_relation_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/relation/{target}",
                "http_method": "DELETE",
                "operation_id": "delete_relation",
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
                "target": {
                    "required": True,
                    "location": "path",
                    "attribute": "target",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._list_available_clusters_for_relation_endpoint = _Endpoint(
            settings={
                "response_type": List[Dict[str, Any]],
                "endpoint_path": "/api/v1/organizations/{orgName}/cluster/{clusterName}/available-relations",
                "http_method": "GET",
                "operation_id": "list_available_clusters_for_relation",
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
                "target_type": {
                    "required": True,
                    "location": "query",
                    "attribute": "targetType",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_related_clusters_endpoint = _Endpoint(
            settings={
                "response_type": List[RelatedClusterListItem],
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/relations",
                "http_method": "GET",
                "operation_id": "list_related_clusters",
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


    def create_relation(
        self,
        org_name: str,
        cluster_name: str,
        target: str,
    ) -> APIErrorResponse:
        """create a relation between the clusters in the organization.
        :type org_name: str
        :type cluster_name: str
        :type target: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["target"] = target
        return self._create_relation_endpoint.call_with_http_info(**kwargs)

    def delete_relation(
        self,
        org_name: str,
        cluster_name: str,
        target: str,
    ) -> APIErrorResponse:
        """delete a existed relation between the clusters in the organization.
        :type org_name: str
        :type cluster_name: str
        :type target: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["target"] = target
        return self._delete_relation_endpoint.call_with_http_info(**kwargs)

    def list_available_clusters_for_relation(
        self,
        org_name: str,
        cluster_name: str,
        target_type: str,
    ) -> List[Dict[str, Any]]:
        """list the available clusters for the organization to create the a relation.
        :type org_name: str
        :type cluster_name: str
        :type target_type: str
        :rtype: List[Dict[str, Any]]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["target_type"] = target_type
        return self._list_available_clusters_for_relation_endpoint.call_with_http_info(**kwargs)

    def list_related_clusters(
        self,
        org_name: str,
        cluster_name: str,
    ) -> List[RelatedClusterListItem]:
        """list the clusters that have built a relation to the specified cluster.
        :type org_name: str
        :type cluster_name: str
        :rtype: List[RelatedClusterListItem]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._list_related_clusters_endpoint.call_with_http_info(**kwargs)
