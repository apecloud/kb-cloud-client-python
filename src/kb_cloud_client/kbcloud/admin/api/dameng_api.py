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


class DamengApi:
    """Dameng API client.

    Provides methods for the dameng endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_tablespace_endpoint = _Endpoint(
            settings={
                "response_type": DmTablespace,
                "endpoint_path": "/admin/v1/data/damengdb/organizations/{orgName}/clusters/{clusterName}/tablespaces",
                "http_method": "POST",
                "operation_id": "create_tablespace",
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
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_tablespace_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/data/damengdb/organizations/{orgName}/clusters/{clusterName}/tablespaces/{tablespaceName}",
                "http_method": "DELETE",
                "operation_id": "delete_tablespace",
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
                "tablespace_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "tablespaceName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_tablespace_endpoint = _Endpoint(
            settings={
                "response_type": DmTablespace,
                "endpoint_path": "/admin/v1/data/damengdb/organizations/{orgName}/clusters/{clusterName}/tablespaces/{tablespaceName}",
                "http_method": "GET",
                "operation_id": "get_tablespace",
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
                "tablespace_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "tablespaceName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_tablespaces_endpoint = _Endpoint(
            settings={
                "response_type": List[DmTablespace],
                "endpoint_path": "/admin/v1/data/damengdb/organizations/{orgName}/clusters/{clusterName}/tablespaces",
                "http_method": "GET",
                "operation_id": "list_tablespaces",
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
        self._update_tablespace_endpoint = _Endpoint(
            settings={
                "response_type": DmTablespace,
                "endpoint_path": "/admin/v1/data/damengdb/organizations/{orgName}/clusters/{clusterName}/tablespaces/{tablespaceName}",
                "http_method": "PATCH",
                "operation_id": "update_tablespace",
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
                "tablespace_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "tablespaceName",
                },
                "body": {
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )


    def create_tablespace(
        self,
        org_name: str,
        cluster_name: str,
        *,
        body: Union[DmTablespace, UnsetType] = unset,
    ) -> DmTablespace:
        """Create damengdb tablespace.

        Create tablespace for a Dameng cluster.
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :type body: DmTablespace, optional
        :rtype: DmTablespace
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if body is not unset:
            kwargs["body"] = body
        return self._create_tablespace_endpoint.call_with_http_info(**kwargs)

    def delete_tablespace(
        self,
        org_name: str,
        cluster_name: str,
        tablespace_name: str,
    ) -> APIErrorResponse:
        """Delete damengdb tablespace.

        Delete tablespace for a Dameng cluster.
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :param tablespace_name: Tablespace name
        :type tablespace_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["tablespace_name"] = tablespace_name
        return self._delete_tablespace_endpoint.call_with_http_info(**kwargs)

    def get_tablespace(
        self,
        org_name: str,
        cluster_name: str,
        tablespace_name: str,
    ) -> DmTablespace:
        """Get Dameng tablespace info.
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :param tablespace_name: Tablespace name
        :type tablespace_name: str
        :rtype: DmTablespace
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["tablespace_name"] = tablespace_name
        return self._get_tablespace_endpoint.call_with_http_info(**kwargs)

    def list_tablespaces(
        self,
        org_name: str,
        cluster_name: str,
    ) -> List[DmTablespace]:
        """List damengdb tablespaces.

        List tablespaces for a Dameng cluster.
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :rtype: List[DmTablespace]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._list_tablespaces_endpoint.call_with_http_info(**kwargs)

    def update_tablespace(
        self,
        org_name: str,
        cluster_name: str,
        tablespace_name: str,
        *,
        body: Union[DmTablespace, UnsetType] = unset,
    ) -> DmTablespace:
        """Update damengdb tablespace.

        Update tablespace for a Dameng cluster.
        :param org_name: Organization name
        :type org_name: str
        :param cluster_name: Cluster name
        :type cluster_name: str
        :param tablespace_name: Tablespace name
        :type tablespace_name: str
        :type body: DmTablespace, optional
        :rtype: DmTablespace
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["tablespace_name"] = tablespace_name
        if body is not unset:
            kwargs["body"] = body
        return self._update_tablespace_endpoint.call_with_http_info(**kwargs)
