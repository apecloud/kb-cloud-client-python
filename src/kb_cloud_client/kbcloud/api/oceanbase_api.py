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


class OceanbaseApi:
    """Oceanbase API client.

    Provides methods for the oceanbase endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_tenant_endpoint = _Endpoint(
            settings={
                "response_type": Tenant,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}",
                "http_method": "GET",
                "operation_id": "get_tenant",
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
                "tenant_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "tenantId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_tenants_endpoint = _Endpoint(
            settings={
                "response_type": List[Tenant],
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/tenants",
                "http_method": "GET",
                "operation_id": "list_tenants",
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


    def get_tenant(
        self,
        org_name: str,
        cluster_name: str,
        tenant_id: str,
    ) -> Tenant:
        """get tenants detail information of the oceanbase cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param tenant_id: id of the tenant
        :type tenant_id: str
        :rtype: Tenant
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["tenant_id"] = tenant_id
        return self._get_tenant_endpoint.call_with_http_info(**kwargs)

    def list_tenants(
        self,
        org_name: str,
        cluster_name: str,
    ) -> List[Tenant]:
        """list all tenants for the oceanbase cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :rtype: List[Tenant]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._list_tenants_endpoint.call_with_http_info(**kwargs)
