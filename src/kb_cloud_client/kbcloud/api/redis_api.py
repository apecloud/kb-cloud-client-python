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


class RedisApi:
    """Redis API client.

    Provides methods for the redis endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_redis_account_endpoint = _Endpoint(
            settings={
                "response_type": ClusterTask,
                "endpoint_path": "/api/v1/data/redis/organizations/{orgName}/clusters/{clusterName}/accounts",
                "http_method": "POST",
                "operation_id": "create_redis_account",
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
        self._delete_redis_account_endpoint = _Endpoint(
            settings={
                "response_type": ClusterTask,
                "endpoint_path": "/api/v1/data/redis/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}",
                "http_method": "DELETE",
                "operation_id": "delete_redis_account",
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
                "account_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "accountName",
                },
                "component": {
                    "location": "query",
                    "attribute": "component",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_redis_accounts_endpoint = _Endpoint(
            settings={
                "response_type": ACLUserResponse,
                "endpoint_path": "/api/v1/data/redis/organizations/{orgName}/clusters/{clusterName}/accounts",
                "http_method": "GET",
                "operation_id": "list_redis_accounts",
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
                "component": {
                    "location": "query",
                    "attribute": "component",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_redis_account_endpoint = _Endpoint(
            settings={
                "response_type": ClusterTask,
                "endpoint_path": "/api/v1/data/redis/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}",
                "http_method": "PATCH",
                "operation_id": "update_redis_account",
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
                "account_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "accountName",
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


    def create_redis_account(
        self,
        org_name: str,
        cluster_name: str,
        body: ACLUser,
        *,
        component: Union[str, UnsetType] = unset,
    ) -> ClusterTask:
        """create redis account.
        :param org_name: the name of organization
        :type org_name: str
        :param cluster_name: the name of cluster
        :type cluster_name: str
        :type body: ACLUser
        :param component: the component type to create account
        :type component: str, optional
        :rtype: ClusterTask
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        if component is not unset:
            kwargs["component"] = component
        return self._create_redis_account_endpoint.call_with_http_info(**kwargs)

    def delete_redis_account(
        self,
        org_name: str,
        cluster_name: str,
        account_name: str,
        *,
        component: Union[str, UnsetType] = unset,
    ) -> ClusterTask:
        """delete redis account.
        :param org_name: the name of organization
        :type org_name: str
        :param cluster_name: the name of cluster
        :type cluster_name: str
        :param account_name: the name of account
        :type account_name: str
        :param component: in which component type to delete account
        :type component: str, optional
        :rtype: ClusterTask
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["account_name"] = account_name
        if component is not unset:
            kwargs["component"] = component
        return self._delete_redis_account_endpoint.call_with_http_info(**kwargs)

    def list_redis_accounts(
        self,
        org_name: str,
        cluster_name: str,
        *,
        component: Union[str, UnsetType] = unset,
    ) -> ACLUserResponse:
        """list redis accounts.
        :param org_name: the name of organization
        :type org_name: str
        :param cluster_name: the name of cluster
        :type cluster_name: str
        :param component: the component type to list accounts
        :type component: str, optional
        :rtype: ACLUserResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if component is not unset:
            kwargs["component"] = component
        return self._list_redis_accounts_endpoint.call_with_http_info(**kwargs)

    def update_redis_account(
        self,
        org_name: str,
        cluster_name: str,
        account_name: str,
        body: ACLUser,
        *,
        component: Union[str, UnsetType] = unset,
    ) -> ClusterTask:
        """update redis account.
        :param org_name: the name of organization
        :type org_name: str
        :param cluster_name: the name of cluster
        :type cluster_name: str
        :param account_name: the name of account
        :type account_name: str
        :type body: ACLUser
        :param component: in which component type to update account
        :type component: str, optional
        :rtype: ClusterTask
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["account_name"] = account_name
        kwargs["body"] = body
        if component is not unset:
            kwargs["component"] = component
        return self._update_redis_account_endpoint.call_with_http_info(**kwargs)
