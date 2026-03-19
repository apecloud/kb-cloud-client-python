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


class ResourcestatsApi:
    """ResourceStats API client.

    Provides methods for the resourceStats endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._list_nodes_resource_stats_endpoint = _Endpoint(
            settings={
                "response_type": NodeResourceStatsList,
                "endpoint_path": "/api/v1/environments/{environmentName}/nodes/resourceStats",
                "http_method": "GET",
                "operation_id": "list_nodes_resource_stats",
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


    def list_nodes_resource_stats(
        self,
        environment_name: str,
    ) -> NodeResourceStatsList:
        """Get resource statistics of nodes.

        Returns aggregated resource statistics for the specified environment within an organization.
        :param environment_name: The name of the environment
        :type environment_name: str
        :rtype: NodeResourceStatsList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._list_nodes_resource_stats_endpoint.call_with_http_info(**kwargs)
