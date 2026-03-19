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


class TlsApi:
    """Tls API client.

    Provides methods for the tls endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_tls_certificate_endpoint = _Endpoint(
            settings={
                "response_type": List[TlsCert],
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/tls",
                "http_method": "GET",
                "operation_id": "get_tls_certificate",
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
        self._tls_switcher_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/tls",
                "http_method": "POST",
                "operation_id": "tls_switcher",
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


    def get_tls_certificate(
        self,
        org_name: str,
        cluster_name: str,
    ) -> List[TlsCert]:
        """Get cluster TLS certificate.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :rtype: List[TlsCert]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._get_tls_certificate_endpoint.call_with_http_info(**kwargs)

    def tls_switcher(
        self,
        org_name: str,
        cluster_name: str,
        body: TlsRequest,
    ) -> APIErrorResponse:
        """Enable or disable cluster TLS.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param body: Enable TLS or not
        :type body: TlsRequest
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._tls_switcher_endpoint.call_with_http_info(**kwargs)
