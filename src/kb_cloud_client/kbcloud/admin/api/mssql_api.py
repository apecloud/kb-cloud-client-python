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


class MssqlApi:
    """Mssql API client.

    Provides methods for the mssql endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._manage_mssql_tde_database_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/data/mssql/organizations/{orgName}/clusters/{clusterName}/tde",
                "http_method": "PATCH",
                "operation_id": "manage_mssql_tde_database",
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


    def manage_mssql_tde_database(
        self,
        org_name: str,
        cluster_name: str,
        *,
        body: Union[DbTDERequest, UnsetType] = unset,
    ) -> APIErrorResponse:
        """batch modify database tde status.
        :param org_name: name of the organization
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :type body: DbTDERequest, optional
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if body is not unset:
            kwargs["body"] = body
        return self._manage_mssql_tde_database_endpoint.call_with_http_info(**kwargs)
