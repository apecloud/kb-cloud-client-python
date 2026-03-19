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
        self._get_load_balancer_endpoint = _Endpoint(
            settings={
                "response_type": LoadBalancer,
                "endpoint_path": "/api/v1/organizations/{orgName}/environments/{environmentName}/loadbalancer",
                "http_method": "GET",
                "operation_id": "get_load_balancer",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
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


    def get_load_balancer(
        self,
        org_name: str,
        environment_name: str,
    ) -> LoadBalancer:
        """Get the load balancer info in the environment.
        :param org_name: name of the Organization
        :type org_name: str
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: LoadBalancer
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["environment_name"] = environment_name
        return self._get_load_balancer_endpoint.call_with_http_info(**kwargs)
