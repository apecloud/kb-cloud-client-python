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


class InstanceApi:
    """Instance API client.

    Provides methods for the instance endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._list_instances_endpoint = _Endpoint(
            settings={
                "response_type": InstanceList,
                "endpoint_path": "/admin/v1/instances",
                "http_method": "GET",
                "operation_id": "list_instances",
                "deprecated": True,
            },
            params_map={
                "env_name": {
                    "location": "query",
                    "attribute": "envName",
                },
                "node_name": {
                    "location": "query",
                    "attribute": "nodeName",
                },
                "org_name": {
                    "location": "query",
                    "attribute": "orgName",
                },
                "cluster_name": {
                    "location": "query",
                    "attribute": "clusterName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def list_instances(
        self,
        *,
        env_name: Union[str, UnsetType] = unset,
        node_name: Union[str, UnsetType] = unset,
        org_name: Union[str, UnsetType] = unset,
        cluster_name: Union[str, UnsetType] = unset,
    ) -> InstanceList:
        """List cluster instances.

        List instances based on query parameters with constraints.
        :param env_name: Name of the environment (optional, required when querying by nodeName).
        :type env_name: str, optional
        :param node_name: Name of the node (optional, required when querying by envName).
        :type node_name: str, optional
        :param org_name: Name of the organization (optional, required when querying by clusterName).
        :type org_name: str, optional
        :param cluster_name: Name of the cluster (optional).
        :type cluster_name: str, optional
        :rtype: InstanceList
        """
        warnings.warn("list_instances is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        if env_name is not unset:
            kwargs["env_name"] = env_name
        if node_name is not unset:
            kwargs["node_name"] = node_name
        if org_name is not unset:
            kwargs["org_name"] = org_name
        if cluster_name is not unset:
            kwargs["cluster_name"] = cluster_name
        return self._list_instances_endpoint.call_with_http_info(**kwargs)
