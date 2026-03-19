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


class MonitordatasinkApi:
    """MonitorDataSink API client.

    Provides methods for the monitorDataSink endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_monitor_data_sink_endpoint = _Endpoint(
            settings={
                "response_type": MonitorDataSink,
                "endpoint_path": "/admin/v1/monitorDataSinks",
                "http_method": "POST",
                "operation_id": "create_monitor_data_sink",
            },
            params_map={
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
        self._delete_monitor_data_sink_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/monitorDataSinks/{monitorDataSinkID}",
                "http_method": "DELETE",
                "operation_id": "delete_monitor_data_sink",
            },
            params_map={
                "monitor_data_sink_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "monitorDataSinkID",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._list_monitor_data_sinks_endpoint = _Endpoint(
            settings={
                "response_type": MonitorDataSinkList,
                "endpoint_path": "/admin/v1/monitorDataSinks/environments/{environmentName}",
                "http_method": "GET",
                "operation_id": "list_monitor_data_sinks",
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
        self._patch_monitor_data_sink_endpoint = _Endpoint(
            settings={
                "response_type": MonitorDataSink,
                "endpoint_path": "/admin/v1/monitorDataSinks/{monitorDataSinkID}",
                "http_method": "PATCH",
                "operation_id": "patch_monitor_data_sink",
            },
            params_map={
                "monitor_data_sink_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "monitorDataSinkID",
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


    def create_monitor_data_sink(
        self,
        body: MonitorDataSinkCreate,
    ) -> MonitorDataSink:
        """Create monitor data sink.

        Create monitor data sink
        :type body: MonitorDataSinkCreate
        :rtype: MonitorDataSink
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_monitor_data_sink_endpoint.call_with_http_info(**kwargs)

    def delete_monitor_data_sink(
        self,
        monitor_data_sink_id: str,
    ) -> APIErrorResponse:
        """Delete monitor data sink.
        :param monitor_data_sink_id: monitor data sink id
        :type monitor_data_sink_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["monitor_data_sink_id"] = monitor_data_sink_id
        return self._delete_monitor_data_sink_endpoint.call_with_http_info(**kwargs)

    def list_monitor_data_sinks(
        self,
        environment_name: str,
    ) -> MonitorDataSinkList:
        """Get monitor data sink list.

        Get monitor data sink list
        :param environment_name: kubernetes environment name which monitor data sink deployed in.
        :type environment_name: str
        :rtype: MonitorDataSinkList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._list_monitor_data_sinks_endpoint.call_with_http_info(**kwargs)

    def patch_monitor_data_sink(
        self,
        monitor_data_sink_id: str,
        body: MonitorDataSinkUpdate,
    ) -> MonitorDataSink:
        """Update the specified monitor data sink.

        Update the specified monitor data sink
        :param monitor_data_sink_id: monitor data sink id
        :type monitor_data_sink_id: str
        :type body: MonitorDataSinkUpdate
        :rtype: MonitorDataSink
        """
        kwargs: Dict[str, Any] = {}
        kwargs["monitor_data_sink_id"] = monitor_data_sink_id
        kwargs["body"] = body
        return self._patch_monitor_data_sink_endpoint.call_with_http_info(**kwargs)
