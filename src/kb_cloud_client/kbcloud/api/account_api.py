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


class AccountApi:
    """Account API client.

    Provides methods for the account endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_account_endpoint = _Endpoint(
            settings={
                "response_type": Account,
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts",
                "http_method": "POST",
                "operation_id": "create_account",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
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
        self._create_account_old_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/accounts",
                "http_method": "POST",
                "operation_id": "create_account_old",
                "deprecated": True,
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
        self._create_mongo_db_account_endpoint = _Endpoint(
            settings={
                "response_type": Account,
                "endpoint_path": "/api/v1/data/mongodb/organizations/{orgName}/clusters/{clusterName}/accounts",
                "http_method": "POST",
                "operation_id": "create_mongo_db_account",
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
        self._delete_account_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}",
                "http_method": "DELETE",
                "operation_id": "delete_account",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_account_old_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}",
                "http_method": "DELETE",
                "operation_id": "delete_account_old",
                "deprecated": True,
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_mongo_db_account_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/data/mongodb/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}",
                "http_method": "DELETE",
                "operation_id": "delete_mongo_db_account",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_mssql_account_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/data/mssql/organizations/{orgName}/clusters/{clusterName}/accounts",
                "http_method": "DELETE",
                "operation_id": "delete_mssql_account",
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
                "account": {
                    "required": True,
                    "location": "query",
                    "attribute": "account",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_root_account_password_endpoint = _Endpoint(
            settings={
                "response_type": str,
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/root-password",
                "http_method": "GET",
                "operation_id": "get_root_account_password",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
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
                    "location": "query",
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
        self._list_accounts_endpoint = _Endpoint(
            settings={
                "response_type": List[AccountListItem],
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts",
                "http_method": "GET",
                "operation_id": "list_accounts",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
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
        self._list_accounts_old_endpoint = _Endpoint(
            settings={
                "response_type": List[AccountListItem],
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/accounts",
                "http_method": "GET",
                "operation_id": "list_accounts_old",
                "deprecated": True,
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
                "include_root": {
                    "location": "query",
                    "attribute": "includeRoot",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_mongo_db_accounts_endpoint = _Endpoint(
            settings={
                "response_type": List[AccountListItem],
                "endpoint_path": "/api/v1/data/mongodb/organizations/{orgName}/clusters/{clusterName}/accounts",
                "http_method": "GET",
                "operation_id": "list_mongo_db_accounts",
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
        self._update_account_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}",
                "http_method": "PATCH",
                "operation_id": "update_account",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
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
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_account_old_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}",
                "http_method": "PATCH",
                "operation_id": "update_account_old",
                "deprecated": True,
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
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_account_privileges_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}/privileges",
                "http_method": "PATCH",
                "operation_id": "update_account_privileges",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
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
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_account_privileges_old_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/accounts/privileges/{accountName}",
                "http_method": "PATCH",
                "operation_id": "update_account_privileges_old",
                "deprecated": True,
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
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_mssql_account_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/data/mssql/organizations/{orgName}/clusters/{clusterName}/accounts",
                "http_method": "PATCH",
                "operation_id": "update_mssql_account",
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


    def create_account(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        body: Account,
    ) -> Account:
        """Create cluster account.

        create an account in cluster
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :type body: Account
        :rtype: Account
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._create_account_endpoint.call_with_http_info(**kwargs)

    def create_account_old(
        self,
        org_name: str,
        cluster_name: str,
        body: Account,
    ) -> APIErrorResponse:
        """Create cluster account.

        create an account in cluster
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :type body: Account
        :rtype: APIErrorResponse
        """
        warnings.warn("create_account_old is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._create_account_old_endpoint.call_with_http_info(**kwargs)

    def create_mongo_db_account(
        self,
        org_name: str,
        cluster_name: str,
        body: Account,
    ) -> Account:
        """Create mongodb account.

        create an account in mongodb
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :type body: Account
        :rtype: Account
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._create_mongo_db_account_endpoint.call_with_http_info(**kwargs)

    def delete_account(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        account_name: str,
    ) -> APIErrorResponse:
        """Delete cluster account.

        delete an account in cluster
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param account_name: name of the Cluster
        :type account_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["account_name"] = account_name
        return self._delete_account_endpoint.call_with_http_info(**kwargs)

    def delete_account_old(
        self,
        org_name: str,
        cluster_name: str,
        account_name: str,
    ) -> APIErrorResponse:
        """Delete cluster account.

        delete an account in cluster
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param account_name: name of the Cluster
        :type account_name: str
        :rtype: APIErrorResponse
        """
        warnings.warn("delete_account_old is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["account_name"] = account_name
        return self._delete_account_old_endpoint.call_with_http_info(**kwargs)

    def delete_mongo_db_account(
        self,
        org_name: str,
        cluster_name: str,
        account_name: str,
    ) -> APIErrorResponse:
        """Delete mongodb account.

        delete an account in mongodb
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param account_name: name of the Cluster
        :type account_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["account_name"] = account_name
        return self._delete_mongo_db_account_endpoint.call_with_http_info(**kwargs)

    def delete_mssql_account(
        self,
        org_name: str,
        cluster_name: str,
        account: str,
    ) -> APIErrorResponse:
        """delete mssql account compatible with windows account.
        :param org_name: name of the organization
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param account: name of the account
        :type account: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["account"] = account
        return self._delete_mssql_account_endpoint.call_with_http_info(**kwargs)

    def get_root_account_password(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        account_name: str,
        *,
        component: Union[str, UnsetType] = unset,
    ) -> str:
        """get root account password.

        get root account password
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param account_name: name of the account
        :type account_name: str
        :param component: name of the component
        :type component: str, optional
        :rtype: str
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["account_name"] = account_name
        if component is not unset:
            kwargs["component"] = component
        return self._get_root_account_password_endpoint.call_with_http_info(**kwargs)

    def list_accounts(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
    ) -> List[AccountListItem]:
        """List cluster accounts.

        list accounts in cluster
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :rtype: List[AccountListItem]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._list_accounts_endpoint.call_with_http_info(**kwargs)

    def list_accounts_old(
        self,
        org_name: str,
        cluster_name: str,
        *,
        component: Union[str, UnsetType] = unset,
        include_root: Union[bool, UnsetType] = unset,
    ) -> List[AccountListItem]:
        """List cluster accounts.

        list accounts in cluster
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param component: component type
        :type component: str, optional
        :param include_root: include root account
        :type include_root: bool, optional
        :rtype: List[AccountListItem]
        """
        warnings.warn("list_accounts_old is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if component is not unset:
            kwargs["component"] = component
        if include_root is not unset:
            kwargs["include_root"] = include_root
        return self._list_accounts_old_endpoint.call_with_http_info(**kwargs)

    def list_mongo_db_accounts(
        self,
        org_name: str,
        cluster_name: str,
    ) -> List[AccountListItem]:
        """List mongodb accounts.

        list accounts in mongodb
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :rtype: List[AccountListItem]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._list_mongo_db_accounts_endpoint.call_with_http_info(**kwargs)

    def update_account(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        account_name: str,
        body: Account,
    ) -> APIErrorResponse:
        """update cluster account.

        update an account in cluster
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param account_name: name of the account
        :type account_name: str
        :type body: Account
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["account_name"] = account_name
        kwargs["body"] = body
        return self._update_account_endpoint.call_with_http_info(**kwargs)

    def update_account_old(
        self,
        org_name: str,
        cluster_name: str,
        account_name: str,
        body: Account,
    ) -> APIErrorResponse:
        """update cluster account.

        update an account in cluster
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param account_name: name of the account
        :type account_name: str
        :type body: Account
        :rtype: APIErrorResponse
        """
        warnings.warn("update_account_old is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["account_name"] = account_name
        kwargs["body"] = body
        return self._update_account_old_endpoint.call_with_http_info(**kwargs)

    def update_account_privileges(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        account_name: str,
        body: List[PrivilegeListItem],
    ) -> APIErrorResponse:
        """update account privileges.

        update account privileges for rdbms engine
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param account_name: name of the account
        :type account_name: str
        :type body: List[PrivilegeListItem]
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["account_name"] = account_name
        kwargs["body"] = body
        return self._update_account_privileges_endpoint.call_with_http_info(**kwargs)

    def update_account_privileges_old(
        self,
        org_name: str,
        cluster_name: str,
        account_name: str,
        body: List[PrivilegeListItem],
    ) -> APIErrorResponse:
        """update account privileges.

        update privileges of account
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param account_name: name of the account
        :type account_name: str
        :type body: List[PrivilegeListItem]
        :rtype: APIErrorResponse
        """
        warnings.warn("update_account_privileges_old is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["account_name"] = account_name
        kwargs["body"] = body
        return self._update_account_privileges_old_endpoint.call_with_http_info(**kwargs)

    def update_mssql_account(
        self,
        org_name: str,
        cluster_name: str,
        *,
        body: Union[Account, UnsetType] = unset,
    ) -> APIErrorResponse:
        """update mssql account compatible with windows account.
        :param org_name: name of the organization
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :type body: Account, optional
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if body is not unset:
            kwargs["body"] = body
        return self._update_mssql_account_endpoint.call_with_http_info(**kwargs)
