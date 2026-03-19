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


class MarkclusterApi:
    """MarkCluster API client.

    Provides methods for the markCluster endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._mark_cluster_restore_completed_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/markClusterRestoreCompleted",
                "http_method": "POST",
                "operation_id": "mark_cluster_restore_completed",
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


    def mark_cluster_restore_completed(
        self,
        org_name: str,
        cluster_name: str,
    ) -> APIErrorResponse:
        """mark cluster to restore completed, usually used when manually repairing or recovering issues.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._mark_cluster_restore_completed_endpoint.call_with_http_info(**kwargs)
