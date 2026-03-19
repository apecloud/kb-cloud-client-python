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


class LoadbalancerApi:
    """LoadBalancer API client.

    Provides methods for the loadBalancer endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._check_load_balancer_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/environments/{environmentName}/loadbalancer/check",
                "http_method": "POST",
                "operation_id": "check_load_balancer",
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
        self._get_load_balancer_endpoint = _Endpoint(
            settings={
                "response_type": LoadBalancer,
                "endpoint_path": "/admin/v1/environments/{environmentName}/loadbalancer",
                "http_method": "GET",
                "operation_id": "get_load_balancer",
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


    def check_load_balancer(
        self,
        environment_name: str,
    ) -> APIErrorResponse:
        """Check if the load balancer is available.
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._check_load_balancer_endpoint.call_with_http_info(**kwargs)

    def get_load_balancer(
        self,
        environment_name: str,
    ) -> LoadBalancer:
        """Get the load balancer info in the environment.
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: LoadBalancer
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._get_load_balancer_endpoint.call_with_http_info(**kwargs)
