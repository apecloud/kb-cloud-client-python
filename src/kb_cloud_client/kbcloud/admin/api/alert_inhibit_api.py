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


class AlertinhibitApi:
    """AlertInhibit API client.

    Provides methods for the alertInhibit endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_alert_inhibit_endpoint = _Endpoint(
            settings={
                "response_type": AlertInhibit,
                "endpoint_path": "/admin/v1/alerts/inhibits",
                "http_method": "POST",
                "operation_id": "create_alert_inhibit",
            },
            params_map={
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
        self._delete_alert_inhibit_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/admin/v1/alerts/inhibits/{inhibitId}",
                "http_method": "DELETE",
                "operation_id": "delete_alert_inhibit",
            },
            params_map={
                "inhibit_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "inhibitId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_alert_inhibit_endpoint = _Endpoint(
            settings={
                "response_type": AlertInhibit,
                "endpoint_path": "/admin/v1/alerts/inhibits/{inhibitId}",
                "http_method": "GET",
                "operation_id": "get_alert_inhibit",
            },
            params_map={
                "inhibit_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "inhibitId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_alert_inhibits_endpoint = _Endpoint(
            settings={
                "response_type": AlertInhibitList,
                "endpoint_path": "/admin/v1/alerts/inhibits",
                "http_method": "GET",
                "operation_id": "list_alert_inhibits",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._patch_alert_inhibit_endpoint = _Endpoint(
            settings={
                "response_type": AlertInhibit,
                "endpoint_path": "/admin/v1/alerts/inhibits",
                "http_method": "PATCH",
                "operation_id": "patch_alert_inhibit",
            },
            params_map={
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


    def create_alert_inhibit(
        self,
        *,
        body: Union[AlertInhibit, UnsetType] = unset,
    ) -> AlertInhibit:
        """Create alert inhibit.
        :type body: AlertInhibit, optional
        :rtype: AlertInhibit
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._create_alert_inhibit_endpoint.call_with_http_info(**kwargs)

    def delete_alert_inhibit(
        self,
        inhibit_id: str,
    ) -> Dict[str, Any]:
        """Delete alert inhibit.
        :param inhibit_id: inhibit id
        :type inhibit_id: str
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["inhibit_id"] = inhibit_id
        return self._delete_alert_inhibit_endpoint.call_with_http_info(**kwargs)

    def get_alert_inhibit(
        self,
        inhibit_id: str,
    ) -> AlertInhibit:
        """Get alert inhibit.
        :param inhibit_id: inhibit id
        :type inhibit_id: str
        :rtype: AlertInhibit
        """
        kwargs: Dict[str, Any] = {}
        kwargs["inhibit_id"] = inhibit_id
        return self._get_alert_inhibit_endpoint.call_with_http_info(**kwargs)

    def list_alert_inhibits(
        self,
    ) -> AlertInhibitList:
        """List alert inhibits.
        :rtype: AlertInhibitList
        """
        kwargs: Dict[str, Any] = {}
        return self._list_alert_inhibits_endpoint.call_with_http_info(**kwargs)

    def patch_alert_inhibit(
        self,
        *,
        body: Union[AlertInhibit, UnsetType] = unset,
    ) -> AlertInhibit:
        """Patch alert inhibit.
        :type body: AlertInhibit, optional
        :rtype: AlertInhibit
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._patch_alert_inhibit_endpoint.call_with_http_info(**kwargs)
