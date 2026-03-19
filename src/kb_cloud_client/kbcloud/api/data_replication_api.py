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


class DatareplicationApi:
    """DataReplication API client.

    Provides methods for the dataReplication endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_data_channel_endpoint = _Endpoint(
            settings={
                "response_type": DataChannelResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel",
                "http_method": "POST",
                "operation_id": "create_data_channel",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
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
        self._create_data_channel_ops_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel/{channelID}/ops/{opsType}",
                "http_method": "POST",
                "operation_id": "create_data_channel_ops",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "channel_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "channelID",
                },
                "ops_type": {
                    "required": True,
                    "location": "path",
                    "attribute": "opsType",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._create_pre_check_endpoint = _Endpoint(
            settings={
                "response_type": PreCheckTaskResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel/precheck",
                "http_method": "POST",
                "operation_id": "create_pre_check",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
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
        self._delete_data_channel_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel/{channelID}",
                "http_method": "DELETE",
                "operation_id": "delete_data_channel",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "channel_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "channelID",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_pre_check_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel/precheck/{preCheckID}",
                "http_method": "DELETE",
                "operation_id": "delete_pre_check",
                "deprecated": True,
            },
            params_map={
                "pre_check_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "preCheckID",
                },
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_data_channel_endpoint = _Endpoint(
            settings={
                "response_type": DataChannelDetail,
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel/{channelID}",
                "http_method": "GET",
                "operation_id": "get_data_channel",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "channel_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "channelID",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_pre_check_endpoint = _Endpoint(
            settings={
                "response_type": PreCheckTaskDetail,
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel/precheck/{preCheckID}",
                "http_method": "GET",
                "operation_id": "get_pre_check",
                "deprecated": True,
            },
            params_map={
                "pre_check_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "preCheckID",
                },
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_data_channel_events_endpoint = _Endpoint(
            settings={
                "response_type": List[EventItem],
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel/{channelID}/events",
                "http_method": "GET",
                "operation_id": "list_data_channel_events",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "channel_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "channelID",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_data_channel_parameters_endpoint = _Endpoint(
            settings={
                "response_type": DataReplicationParametersResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel/parameters",
                "http_method": "GET",
                "operation_id": "list_data_channel_parameters",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "standard_name": {
                    "location": "query",
                    "attribute": "standardName",
                },
                "channel_id": {
                    "location": "query",
                    "attribute": "channelID",
                },
                "module_name": {
                    "location": "query",
                    "attribute": "moduleName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_data_channels_endpoint = _Endpoint(
            settings={
                "response_type": List[DataChannelItem],
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel",
                "http_method": "GET",
                "operation_id": "list_data_channels",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "name": {
                    "location": "query",
                    "attribute": "name",
                },
                "status": {
                    "location": "query",
                    "attribute": "status",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._query_data_channel_logs_endpoint = _Endpoint(
            settings={
                "response_type": str,
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel/{channelID}/logs",
                "http_method": "GET",
                "operation_id": "query_data_channel_logs",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "channel_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "channelID",
                },
                "module_name": {
                    "location": "query",
                    "attribute": "moduleName",
                },
                "limit": {
                    "location": "query",
                    "attribute": "limit",
                },
            },
            headers_map={
                "accept": ["text/plain", "application/json"],
            },
            api_client=api_client,
        )
        self._query_replication_object_endpoint = _Endpoint(
            settings={
                "response_type": ReplicationObjectTree,
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel/objects",
                "http_method": "POST",
                "operation_id": "query_replication_object",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
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
        self._update_data_channel_endpoint = _Endpoint(
            settings={
                "response_type": DataChannelResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/replication/channel/{channelID}",
                "http_method": "PATCH",
                "operation_id": "update_data_channel",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "channel_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "channelID",
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


    def create_data_channel(
        self,
        org_name: str,
        body: DataReplicationCreate,
    ) -> DataChannelResponse:
        """Create a new data channel.

        Create a new data channel.
        :param org_name: The Name of the organization
        :type org_name: str
        :type body: DataReplicationCreate
        :rtype: DataChannelResponse
        """
        warnings.warn("create_data_channel is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_data_channel_endpoint.call_with_http_info(**kwargs)

    def create_data_channel_ops(
        self,
        org_name: str,
        channel_id: str,
        ops_type: DataReplication_opsType,
    ) -> APIErrorResponse:
        """Create a new data channel ops.

        Create a new data channel ops.
        :param org_name: The Name of the organization
        :type org_name: str
        :param channel_id: The ID of the data channel
        :type channel_id: str
        :param ops_type: The operation type
        :type ops_type: DataReplication_opsType
        :rtype: APIErrorResponse
        """
        warnings.warn("create_data_channel_ops is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["channel_id"] = channel_id
        kwargs["ops_type"] = ops_type
        return self._create_data_channel_ops_endpoint.call_with_http_info(**kwargs)

    def create_pre_check(
        self,
        org_name: str,
        body: PreCheckCreate,
    ) -> PreCheckTaskResponse:
        """create pre check.

        create pre check.
        :param org_name: The Name of the organization
        :type org_name: str
        :type body: PreCheckCreate
        :rtype: PreCheckTaskResponse
        """
        warnings.warn("create_pre_check is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_pre_check_endpoint.call_with_http_info(**kwargs)

    def delete_data_channel(
        self,
        org_name: str,
        channel_id: str,
    ) -> APIErrorResponse:
        """Delete a data channel.

        Delete a data channel.
        :param org_name: The Name of the organization
        :type org_name: str
        :param channel_id: The ID of the data channel
        :type channel_id: str
        :rtype: APIErrorResponse
        """
        warnings.warn("delete_data_channel is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["channel_id"] = channel_id
        return self._delete_data_channel_endpoint.call_with_http_info(**kwargs)

    def delete_pre_check(
        self,
        pre_check_id: str,
        org_name: str,
    ) -> APIErrorResponse:
        """delete preCheck.

        delete preCheck.
        :param pre_check_id: The ID of the preCheck task
        :type pre_check_id: str
        :param org_name: The Name of the organization
        :type org_name: str
        :rtype: APIErrorResponse
        """
        warnings.warn("delete_pre_check is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["pre_check_id"] = pre_check_id
        kwargs["org_name"] = org_name
        return self._delete_pre_check_endpoint.call_with_http_info(**kwargs)

    def get_data_channel(
        self,
        org_name: str,
        channel_id: str,
    ) -> DataChannelDetail:
        """Get Data Channel Details.

        Retrieve a data channel detail.
        :param org_name: The Name of the organization
        :type org_name: str
        :param channel_id: The ID of the data channel
        :type channel_id: str
        :rtype: DataChannelDetail
        """
        warnings.warn("get_data_channel is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["channel_id"] = channel_id
        return self._get_data_channel_endpoint.call_with_http_info(**kwargs)

    def get_pre_check(
        self,
        pre_check_id: str,
        org_name: str,
    ) -> PreCheckTaskDetail:
        """get preCheck.

        get preCheck.
        :param pre_check_id: The ID of the preCheck task
        :type pre_check_id: str
        :param org_name: The Name of the organization
        :type org_name: str
        :rtype: PreCheckTaskDetail
        """
        warnings.warn("get_pre_check is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["pre_check_id"] = pre_check_id
        kwargs["org_name"] = org_name
        return self._get_pre_check_endpoint.call_with_http_info(**kwargs)

    def list_data_channel_events(
        self,
        org_name: str,
        channel_id: str,
    ) -> List[EventItem]:
        """List Data Channel Events.

        Retrieve a list of data channel events.
        :param org_name: The Name of the organization
        :type org_name: str
        :param channel_id: The ID of the data channel
        :type channel_id: str
        :rtype: List[EventItem]
        """
        warnings.warn("list_data_channel_events is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["channel_id"] = channel_id
        return self._list_data_channel_events_endpoint.call_with_http_info(**kwargs)

    def list_data_channel_parameters(
        self,
        org_name: str,
        *,
        standard_name: Union[str, UnsetType] = unset,
        channel_id: Union[str, UnsetType] = unset,
        module_name: Union[str, UnsetType] = unset,
    ) -> DataReplicationParametersResponse:
        """List Data Channel Parameters.

        Retrieve a list of data channel parameters.
        :param org_name: The Name of the organization
        :type org_name: str
        :param standard_name: The name of the standard definition
        :type standard_name: str, optional
        :param channel_id: The ID of the data channel
        :type channel_id: str, optional
        :param module_name: The module name
        :type module_name: str, optional
        :rtype: DataReplicationParametersResponse
        """
        warnings.warn("list_data_channel_parameters is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        if standard_name is not unset:
            kwargs["standard_name"] = standard_name
        if channel_id is not unset:
            kwargs["channel_id"] = channel_id
        if module_name is not unset:
            kwargs["module_name"] = module_name
        return self._list_data_channel_parameters_endpoint.call_with_http_info(**kwargs)

    def list_data_channels(
        self,
        org_name: str,
        *,
        name: Union[str, UnsetType] = unset,
        status: Union[List[str], UnsetType] = unset,
    ) -> List[DataChannelItem]:
        """List Data Channels.

        Retrieve a list of data channels.
        :param org_name: The Name of the organization
        :type org_name: str
        :param name: The name of the data channel
        :type name: str, optional
        :param status: The status of the data channel
        :type status: List[str], optional
        :rtype: List[DataChannelItem]
        """
        warnings.warn("list_data_channels is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        if name is not unset:
            kwargs["name"] = name
        if status is not unset:
            kwargs["status"] = status
        return self._list_data_channels_endpoint.call_with_http_info(**kwargs)

    def query_data_channel_logs(
        self,
        org_name: str,
        channel_id: str,
        *,
        module_name: Union[str, UnsetType] = unset,
        limit: Union[str, UnsetType] = unset,
    ) -> str:
        """Query data channel logs.

        Query logs of a data channel
        :param org_name: The Name of the organization
        :type org_name: str
        :type channel_id: str
        :type module_name: str, optional
        :type limit: str, optional
        :rtype: str
        """
        warnings.warn("query_data_channel_logs is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["channel_id"] = channel_id
        if module_name is not unset:
            kwargs["module_name"] = module_name
        if limit is not unset:
            kwargs["limit"] = limit
        return self._query_data_channel_logs_endpoint.call_with_http_info(**kwargs)

    def query_replication_object(
        self,
        org_name: str,
        body: ReplicationObjectQuery,
    ) -> ReplicationObjectTree:
        """query replication object.

        query replication object.
        :param org_name: The Name of the organization
        :type org_name: str
        :type body: ReplicationObjectQuery
        :rtype: ReplicationObjectTree
        """
        warnings.warn("query_replication_object is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._query_replication_object_endpoint.call_with_http_info(**kwargs)

    def update_data_channel(
        self,
        org_name: str,
        channel_id: str,
        body: DataReplicationUpdate,
    ) -> DataChannelResponse:
        """Update a data channel.

        Update a new data channel.
        :param org_name: The Name of the organization
        :type org_name: str
        :param channel_id: The ID of the data channel
        :type channel_id: str
        :type body: DataReplicationUpdate
        :rtype: DataChannelResponse
        """
        warnings.warn("update_data_channel is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["channel_id"] = channel_id
        kwargs["body"] = body
        return self._update_data_channel_endpoint.call_with_http_info(**kwargs)
