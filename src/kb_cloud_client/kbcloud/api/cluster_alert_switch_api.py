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


class ClusteralertswitchApi:
    """ClusterAlertSwitch API client.

    Provides methods for the clusterAlertSwitch endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_cluster_alert_disabled_endpoint = _Endpoint(
            settings={
                "response_type": AlertCluster,
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/cluster/{clusterName}",
                "http_method": "GET",
                "operation_id": "get_cluster_alert_disabled",
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
        self._set_cluster_alert_disabled_endpoint = _Endpoint(
            settings={
                "response_type": AlertCluster,
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/cluster/{clusterName}",
                "http_method": "PATCH",
                "operation_id": "set_cluster_alert_disabled",
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


    def get_cluster_alert_disabled(
        self,
        org_name: str,
        cluster_name: str,
    ) -> AlertCluster:
        """Check if cluster alert is disabled.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: clusterName
        :type cluster_name: str
        :rtype: AlertCluster
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._get_cluster_alert_disabled_endpoint.call_with_http_info(**kwargs)

    def set_cluster_alert_disabled(
        self,
        org_name: str,
        cluster_name: str,
        *,
        body: Union[AlertCluster, UnsetType] = unset,
    ) -> AlertCluster:
        """Set cluster alert disabled or enabled.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: clusterName
        :type cluster_name: str
        :type body: AlertCluster, optional
        :rtype: AlertCluster
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if body is not unset:
            kwargs["body"] = body
        return self._set_cluster_alert_disabled_endpoint.call_with_http_info(**kwargs)
