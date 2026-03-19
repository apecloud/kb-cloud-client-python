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


class IpwhitelistApi:
    """IpWhitelist API client.

    Provides methods for the ipWhitelist endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_ip_whitelist_endpoint = _Endpoint(
            settings={
                "response_type": IpWhitelist,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/ipWhitelist",
                "http_method": "POST",
                "operation_id": "create_ip_whitelist",
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
        self._delete_ip_white_list_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/ipWhitelist/{ipWhitelistId}",
                "http_method": "DELETE",
                "operation_id": "delete_ip_white_list",
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
                "ip_whitelist_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "ipWhitelistId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_ip_whitelist_endpoint = _Endpoint(
            settings={
                "response_type": IpWhitelistList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/ipWhitelist",
                "http_method": "GET",
                "operation_id": "list_ip_whitelist",
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
        self._update_ip_whitelist_endpoint = _Endpoint(
            settings={
                "response_type": IpWhitelist,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/ipWhitelist/{ipWhitelistId}",
                "http_method": "PATCH",
                "operation_id": "update_ip_whitelist",
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
                "ip_whitelist_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "ipWhitelistId",
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


    def create_ip_whitelist(
        self,
        org_name: str,
        cluster_name: str,
        body: Dict[str, Any],
    ) -> IpWhitelist:
        """Create IP whitelist.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :type body: Dict[str, Any]
        :rtype: IpWhitelist
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._create_ip_whitelist_endpoint.call_with_http_info(**kwargs)

    def delete_ip_white_list(
        self,
        org_name: str,
        cluster_name: str,
        ip_whitelist_id: str,
    ) -> APIErrorResponse:
        """Delete IP whitelist.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param ip_whitelist_id: ID of the IP whitelist
        :type ip_whitelist_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["ip_whitelist_id"] = ip_whitelist_id
        return self._delete_ip_white_list_endpoint.call_with_http_info(**kwargs)

    def list_ip_whitelist(
        self,
        org_name: str,
        cluster_name: str,
    ) -> IpWhitelistList:
        """List IP whitelists.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :rtype: IpWhitelistList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._list_ip_whitelist_endpoint.call_with_http_info(**kwargs)

    def update_ip_whitelist(
        self,
        org_name: str,
        cluster_name: str,
        ip_whitelist_id: str,
        body: Dict[str, Any],
    ) -> IpWhitelist:
        """Update IP whitelist.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param ip_whitelist_id: ID of the IP whitelist
        :type ip_whitelist_id: str
        :type body: Dict[str, Any]
        :rtype: IpWhitelist
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["ip_whitelist_id"] = ip_whitelist_id
        kwargs["body"] = body
        return self._update_ip_whitelist_endpoint.call_with_http_info(**kwargs)
