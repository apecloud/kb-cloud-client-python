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


class EventApi:
    """Event API client.

    Provides methods for the event endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_event_filter_endpoint = _Endpoint(
            settings={
                "response_type": EventFilterOptionList,
                "endpoint_path": "/api/v1/organizations/{orgName}/eventfilter/{filterType}",
                "http_method": "GET",
                "operation_id": "get_event_filter",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "filter_type": {
                    "required": True,
                    "location": "path",
                    "attribute": "filterType",
                },
                "start": {
                    "required": True,
                    "location": "query",
                    "attribute": "start",
                },
                "end": {
                    "required": True,
                    "location": "query",
                    "attribute": "end",
                },
                "resource_type": {
                    "location": "query",
                    "attribute": "resourceType",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_org_event_endpoint = _Endpoint(
            settings={
                "response_type": Event,
                "endpoint_path": "/api/v1/organizations/{orgName}/events/{eventID}",
                "http_method": "GET",
                "operation_id": "get_org_event",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "event_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "eventID",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_org_events_endpoint = _Endpoint(
            settings={
                "response_type": EventList,
                "endpoint_path": "/api/v1/organizations/{orgName}/events",
                "http_method": "GET",
                "operation_id": "list_org_events",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "start": {
                    "required": True,
                    "location": "query",
                    "attribute": "start",
                },
                "end": {
                    "required": True,
                    "location": "query",
                    "attribute": "end",
                },
                "custom_query": {
                    "location": "query",
                    "attribute": "customQuery",
                },
                "status": {
                    "location": "query",
                    "attribute": "status",
                },
                "page_number": {
                    "location": "query",
                    "attribute": "pageNumber",
                },
                "page_size": {
                    "location": "query",
                    "attribute": "pageSize",
                },
                "order_by": {
                    "location": "query",
                    "attribute": "orderBy",
                },
                "sort_desc": {
                    "location": "query",
                    "attribute": "sortDesc",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def get_event_filter(
        self,
        org_name: str,
        filter_type: EventFilterType,
        start: int,
        end: int,
        *,
        resource_type: Union[str, UnsetType] = unset,
    ) -> EventFilterOptionList:
        """Query available filters for event listing.

        Query available filters for event listing
        :param org_name: The orgName
        :type org_name: str
        :param filter_type: The event filter field you want to obtain. OpenAPI do not support orgName.
        :type filter_type: EventFilterType
        :param start: The start of the time range for the query, unit is seconds.
        :type start: int
        :param end: The end of the time range for the query, unit is seconds.
        :type end: int
        :param resource_type: The resource type you want to obtain.
        :type resource_type: str, optional
        :rtype: EventFilterOptionList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["filter_type"] = filter_type
        kwargs["start"] = start
        kwargs["end"] = end
        if resource_type is not unset:
            kwargs["resource_type"] = resource_type
        return self._get_event_filter_endpoint.call_with_http_info(**kwargs)

    def get_org_event(
        self,
        org_name: str,
        event_id: str,
    ) -> Event:
        """Query event detail by Event ID.

        Retrieves detailed information about an event based on the provided Event ID.
        :param org_name: Organization Name
        :type org_name: str
        :param event_id: Unique identifier for the event.
        :type event_id: str
        :rtype: Event
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["event_id"] = event_id
        return self._get_org_event_endpoint.call_with_http_info(**kwargs)

    def list_org_events(
        self,
        org_name: str,
        start: int,
        end: int,
        *,
        custom_query: Union[str, UnsetType] = unset,
        status: Union[EventResultStatus, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        order_by: Union[str, UnsetType] = unset,
        sort_desc: Union[bool, UnsetType] = unset,
    ) -> EventList:
        """List events.

        List events
        :param org_name: Organization Name
        :type org_name: str
        :param start: The start of the time range for the query, unit is seconds.
        :type start: int
        :param end: The end of the time range for the query, unit is seconds.
        :type end: int
        :param custom_query: Advanced query conditions, supporting all types of filterType. Such as "operatorID:333 operatorID:444"
        :type custom_query: str, optional
        :param status: the status of the event
        :type status: EventResultStatus, optional
        :param page_number: the pageNumber of the query
        :type page_number: int, optional
        :param page_size: the pageSize of the query
        :type page_size: int, optional
        :param order_by: A generic orderBy construct used to specify which field to sort by in the interface. (e.g., startTime or endTime). ...
        :type order_by: str, optional
        :param sort_desc: Specifies the sorting direction. `true` for descending, `false` for ascending.
        :type sort_desc: bool, optional
        :rtype: EventList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["start"] = start
        kwargs["end"] = end
        if custom_query is not unset:
            kwargs["custom_query"] = custom_query
        if status is not unset:
            kwargs["status"] = status
        if page_number is not unset:
            kwargs["page_number"] = page_number
        if page_size is not unset:
            kwargs["page_size"] = page_size
        if order_by is not unset:
            kwargs["order_by"] = order_by
        if sort_desc is not unset:
            kwargs["sort_desc"] = sort_desc
        return self._list_org_events_endpoint.call_with_http_info(**kwargs)
