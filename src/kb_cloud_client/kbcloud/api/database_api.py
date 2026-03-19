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


class DatabaseApi:
    """Database API client.

    Provides methods for the database endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_database_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/databases",
                "http_method": "POST",
                "operation_id": "create_database",
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
        self._create_database_old_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/databases",
                "http_method": "POST",
                "operation_id": "create_database_old",
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
        self._delete_database_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/databases/{databaseName}",
                "http_method": "DELETE",
                "operation_id": "delete_database",
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
                "database_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "databaseName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_database_old_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/databases/{databaseName}",
                "http_method": "DELETE",
                "operation_id": "delete_database_old",
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
                "database_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "databaseName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_database_endpoint = _Endpoint(
            settings={
                "response_type": Database,
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/databases/{databaseName}",
                "http_method": "GET",
                "operation_id": "get_database",
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
                "database_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "databaseName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_databases_endpoint = _Endpoint(
            settings={
                "response_type": DatabaseList,
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/databases",
                "http_method": "GET",
                "operation_id": "list_databases",
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
        self._list_databases_old_endpoint = _Endpoint(
            settings={
                "response_type": DatabaseList,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/databases",
                "http_method": "GET",
                "operation_id": "list_databases_old",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_database_config_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/databases/{databaseName}",
                "http_method": "PATCH",
                "operation_id": "update_database_config",
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
                "database_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "databaseName",
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


    def create_database(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        body: Database,
    ) -> APIErrorResponse:
        """Create cluster database.

        create a database in cluster
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :type body: Database
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._create_database_endpoint.call_with_http_info(**kwargs)

    def create_database_old(
        self,
        org_name: str,
        cluster_name: str,
        body: Database,
    ) -> APIErrorResponse:
        """Create cluster database.

        create a database in cluster
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :type body: Database
        :rtype: APIErrorResponse
        """
        warnings.warn("create_database_old is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._create_database_old_endpoint.call_with_http_info(**kwargs)

    def delete_database(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        database_name: str,
    ) -> APIErrorResponse:
        """Delete cluster database.

        delete a database in cluster
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param database_name: name of database
        :type database_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["database_name"] = database_name
        return self._delete_database_endpoint.call_with_http_info(**kwargs)

    def delete_database_old(
        self,
        org_name: str,
        cluster_name: str,
        database_name: str,
    ) -> APIErrorResponse:
        """Delete cluster database.

        delete a database in cluster
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param database_name: name of database
        :type database_name: str
        :rtype: APIErrorResponse
        """
        warnings.warn("delete_database_old is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["database_name"] = database_name
        return self._delete_database_old_endpoint.call_with_http_info(**kwargs)

    def get_database(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        database_name: str,
    ) -> Database:
        """getDatabase.

        get a database info in cluster
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param database_name: name of database
        :type database_name: str
        :rtype: Database
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["database_name"] = database_name
        return self._get_database_endpoint.call_with_http_info(**kwargs)

    def list_databases(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
    ) -> DatabaseList:
        """List cluster databases.

        list databases for rdbms engine cluster
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :rtype: DatabaseList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._list_databases_endpoint.call_with_http_info(**kwargs)

    def list_databases_old(
        self,
        org_name: str,
        cluster_name: str,
    ) -> DatabaseList:
        """List cluster databases.

        list databases in cluster
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :rtype: DatabaseList
        """
        warnings.warn("list_databases_old is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._list_databases_old_endpoint.call_with_http_info(**kwargs)

    def update_database_config(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        database_name: str,
        *,
        body: Union[Dict[str, str], UnsetType] = unset,
    ) -> APIErrorResponse:
        """update database config.

        update a database config in cluster
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param database_name: name of database
        :type database_name: str
        :type body: Dict[str, str], optional
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["database_name"] = database_name
        if body is not unset:
            kwargs["body"] = body
        return self._update_database_config_endpoint.call_with_http_info(**kwargs)
