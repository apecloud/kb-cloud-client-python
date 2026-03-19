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


class VippoolApi:
    """VipPool API client.

    Provides methods for the vipPool endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_vip_pool_endpoint = _Endpoint(
            settings={
                "response_type": VipPool,
                "endpoint_path": "/admin/v1/environments/{environmentName}/loadbalancer/vipPool",
                "http_method": "POST",
                "operation_id": "create_vip_pool",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
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
        self._delete_vip_pool_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/environments/{environmentName}/loadbalancer/vipPool/{poolID}",
                "http_method": "DELETE",
                "operation_id": "delete_vip_pool",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "pool_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "poolID",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_vip_pool_endpoint = _Endpoint(
            settings={
                "response_type": VipPoolList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/loadbalancer/vipPool",
                "http_method": "GET",
                "operation_id": "list_vip_pool",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def create_vip_pool(
        self,
        environment_name: str,
        body: VipPoolCreate,
    ) -> VipPool:
        """Create environment VIP Pool.
        :param environment_name: name of the environment
        :type environment_name: str
        :type body: VipPoolCreate
        :rtype: VipPool
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["body"] = body
        return self._create_vip_pool_endpoint.call_with_http_info(**kwargs)

    def delete_vip_pool(
        self,
        environment_name: str,
        pool_id: str,
    ) -> APIErrorResponse:
        """Delete environment VIP Pool.
        :param environment_name: name of the environment
        :type environment_name: str
        :param pool_id: id of the VIP Pool
        :type pool_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["pool_id"] = pool_id
        return self._delete_vip_pool_endpoint.call_with_http_info(**kwargs)

    def list_vip_pool(
        self,
        environment_name: str,
    ) -> VipPoolList:
        """List environment VIP Pools.
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: VipPoolList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._list_vip_pool_endpoint.call_with_http_info(**kwargs)
