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


class SlaApi:
    """SLA API client.

    Provides methods for the SLA endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._calculate_sla_in_org_endpoint = _Endpoint(
            settings={
                "response_type": List[SLA],
                "endpoint_path": "/api/v1/organizations/{orgName}/sla",
                "http_method": "GET",
                "operation_id": "calculate_sla_in_org",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "environment_name": {
                    "location": "query",
                    "attribute": "environmentName",
                    "collection_format": "multi",
                },
                "cluster_id": {
                    "location": "query",
                    "attribute": "clusterID",
                    "collection_format": "multi",
                },
                "engine": {
                    "location": "query",
                    "attribute": "engine",
                    "collection_format": "multi",
                },
                "start_time": {
                    "location": "query",
                    "attribute": "startTime",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def calculate_sla_in_org(
        self,
        org_name: str,
        *,
        environment_name: Union[List[str], UnsetType] = unset,
        cluster_id: Union[List[str], UnsetType] = unset,
        engine: Union[List[str], UnsetType] = unset,
        start_time: Union[int, UnsetType] = unset,
    ) -> List[SLA]:
        """Calculate SLA for a organization.

        Calculate SLA for a organization
        :param org_name: name of the organization
        :type org_name: str
        :param environment_name: name of the environment
        :type environment_name: List[str], optional
        :param cluster_id: id of the cluster
        :type cluster_id: List[str], optional
        :param engine: database engine type
        :type engine: List[str], optional
        :param start_time: UTC timestamp of the start time to calculate SLA, unit is second
        :type start_time: int, optional
        :rtype: List[SLA]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        if environment_name is not unset:
            kwargs["environment_name"] = environment_name
        if cluster_id is not unset:
            kwargs["cluster_id"] = cluster_id
        if engine is not unset:
            kwargs["engine"] = engine
        if start_time is not unset:
            kwargs["start_time"] = start_time
        return self._calculate_sla_in_org_endpoint.call_with_http_info(**kwargs)
