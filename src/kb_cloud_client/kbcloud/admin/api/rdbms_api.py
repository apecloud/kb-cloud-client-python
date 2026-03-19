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


class RdbmsApi:
    """Rdbms API client.

    Provides methods for the rdbms endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._generate_demo_data_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/demo",
                "http_method": "POST",
                "operation_id": "generate_demo_data",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_database_options_endpoint = _Endpoint(
            settings={
                "response_type": List[str],
                "endpoint_path": "/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/dboptions",
                "http_method": "GET",
                "operation_id": "get_database_options",
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
                "type_": {
                    "required": True,
                    "location": "query",
                    "attribute": "type",
                },
                "charset": {
                    "location": "query",
                    "attribute": "charset",
                },
                "filter_": {
                    "location": "query",
                    "attribute": "filter",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def generate_demo_data(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        account_name: str,
    ) -> APIErrorResponse:
        """generate demo data.

        generate demo data
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param account_name: acccount name which owns the database to generate demo data
        :type account_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["account_name"] = account_name
        return self._generate_demo_data_endpoint.call_with_http_info(**kwargs)

    def get_database_options(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        type_: str,
        *,
        charset: Union[str, UnsetType] = unset,
        filter_: Union[str, UnsetType] = unset,
    ) -> List[str]:
        """get database options.

        get available options for creating database
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param type_: option type
        :type type_: str
        :param charset: specified charset
        :type charset: str, optional
        :param filter_: filter keyword
        :type filter_: str, optional
        :rtype: List[str]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["type_"] = type_
        if charset is not unset:
            kwargs["charset"] = charset
        if filter_ is not unset:
            kwargs["filter_"] = filter_
        return self._get_database_options_endpoint.call_with_http_info(**kwargs)
