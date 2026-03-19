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


class AlertobjectApi:
    """AlertObject API client.

    Provides methods for the alertObject endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._list_alert_objects_endpoint = _Endpoint(
            settings={
                "response_type": AlertObjectList,
                "endpoint_path": "/admin/v1/alerts/objects",
                "http_method": "GET",
                "operation_id": "list_alert_objects",
            },
            params_map={
                "page": {
                    "location": "query",
                    "attribute": "page",
                },
                "page_size": {
                    "location": "query",
                    "attribute": "pageSize",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._set_alert_object_status_endpoint = _Endpoint(
            settings={
                "response_type": AlertObject,
                "endpoint_path": "/admin/v1/alerts/objects/{alertId}",
                "http_method": "PATCH",
                "operation_id": "set_alert_object_status",
            },
            params_map={
                "alert_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "alertId",
                },
                "status": {
                    "required": True,
                    "location": "query",
                    "attribute": "status",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._set_alert_objects_status_endpoint = _Endpoint(
            settings={
                "response_type": AlertObjectList,
                "endpoint_path": "/admin/v1/alerts/objects",
                "http_method": "PATCH",
                "operation_id": "set_alert_objects_status",
            },
            params_map={
                "status": {
                    "required": True,
                    "location": "query",
                    "attribute": "status",
                },
                "body": {
                    "location": "body",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )


    def list_alert_objects(
        self,
        *,
        page: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
    ) -> AlertObjectList:
        """List alert objects.
        :param page: page number
        :type page: int, optional
        :param page_size: page size
        :type page_size: int, optional
        :rtype: AlertObjectList
        """
        kwargs: Dict[str, Any] = {}
        if page is not unset:
            kwargs["page"] = page
        if page_size is not unset:
            kwargs["page_size"] = page_size
        return self._list_alert_objects_endpoint.call_with_http_info(**kwargs)

    def set_alert_object_status(
        self,
        alert_id: str,
        status: str,
    ) -> AlertObject:
        """Set alert object status.
        :param alert_id: alert id
        :type alert_id: str
        :type status: str
        :rtype: AlertObject
        """
        kwargs: Dict[str, Any] = {}
        kwargs["alert_id"] = alert_id
        kwargs["status"] = status
        return self._set_alert_object_status_endpoint.call_with_http_info(**kwargs)

    def set_alert_objects_status(
        self,
        status: str,
        *,
        body: Union[List[AlertObject], UnsetType] = unset,
    ) -> AlertObjectList:
        """Set alert objects status.
        :type status: str
        :type body: List[AlertObject], optional
        :rtype: AlertObjectList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["status"] = status
        if body is not unset:
            kwargs["body"] = body
        return self._set_alert_objects_status_endpoint.call_with_http_info(**kwargs)
