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
        self._get_resource_stats_endpoint = _Endpoint(
            settings={
                "response_type": EnvironmentResourceStats,
                "endpoint_path": "/admin/v1/environments/{environmentName}/resourceStats",
                "http_method": "GET",
                "operation_id": "get_resource_stats",
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
        self._list_instances_resource_stats_endpoint = _Endpoint(
            settings={
                "response_type": InstanceResourceStatsList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes/{nodeName}/instances/resourceStats",
                "http_method": "GET",
                "operation_id": "list_instances_resource_stats",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "node_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "nodeName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_nodes_resource_stats_endpoint = _Endpoint(
            settings={
                "response_type": NodeResourceStatsList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes/resourceStats",
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


    def get_resource_stats(
        self,
        environment_name: str,
    ) -> EnvironmentResourceStats:
        """Get resource statistics of environment.

        Returns aggregated resource statistics for the specified environment within an organization.
        :param environment_name: The name of the environment
        :type environment_name: str
        :rtype: EnvironmentResourceStats
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._get_resource_stats_endpoint.call_with_http_info(**kwargs)

    def list_instances_resource_stats(
        self,
        environment_name: str,
        node_name: str,
    ) -> InstanceResourceStatsList:
        """Get resource statistics of instances.

        Returns aggregated resource statistics for the specified node.
        :param environment_name: The name of the environment
        :type environment_name: str
        :param node_name: The name of the node
        :type node_name: str
        :rtype: InstanceResourceStatsList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["node_name"] = node_name
        return self._list_instances_resource_stats_endpoint.call_with_http_info(**kwargs)

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
