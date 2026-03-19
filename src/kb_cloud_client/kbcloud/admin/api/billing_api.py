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


class BillingApi:
    """Billing API client.

    Provides methods for the billing endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._list_bills_endpoint = _Endpoint(
            settings={
                "response_type": BillList,
                "endpoint_path": "/admin/v1/bills",
                "http_method": "GET",
                "operation_id": "list_bills",
            },
            params_map={
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
                "bill_id": {
                    "location": "query",
                    "attribute": "billID",
                },
                "cluster_id": {
                    "location": "query",
                    "attribute": "clusterID",
                },
                "org_name": {
                    "location": "query",
                    "attribute": "orgName",
                },
                "project_name": {
                    "location": "query",
                    "attribute": "projectName",
                },
                "aggregation_time": {
                    "location": "query",
                    "attribute": "aggregationTime",
                },
                "aggregation_group": {
                    "location": "query",
                    "attribute": "aggregationGroup",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._refresh_bills_endpoint = _Endpoint(
            settings={
                "response_type": BasicTask,
                "endpoint_path": "/admin/v1/bills/refresh",
                "http_method": "POST",
                "operation_id": "refresh_bills",
            },
            params_map={
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def list_bills(
        self,
        start: int,
        end: int,
        *,
        bill_id: Union[str, UnsetType] = unset,
        cluster_id: Union[str, UnsetType] = unset,
        org_name: Union[str, UnsetType] = unset,
        project_name: Union[str, UnsetType] = unset,
        aggregation_time: Union[AggregationTimeType, UnsetType] = unset,
        aggregation_group: Union[AggregationGroupType, UnsetType] = unset,
    ) -> BillList:
        """List bills.
        :param start: The start of the time range for the query, unit is seconds.
        :type start: int
        :param end: The end of the time range for the query, unit is seconds.
        :type end: int
        :param bill_id: The ID of the bill
        :type bill_id: str, optional
        :param cluster_id: The ID of the cluster
        :type cluster_id: str, optional
        :param org_name: name of the organization
        :type org_name: str, optional
        :param project_name: name of the project
        :type project_name: str, optional
        :param aggregation_time: The type of aggregation time
        :type aggregation_time: AggregationTimeType, optional
        :param aggregation_group: The type of aggregation group
        :type aggregation_group: AggregationGroupType, optional
        :rtype: BillList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["start"] = start
        kwargs["end"] = end
        if bill_id is not unset:
            kwargs["bill_id"] = bill_id
        if cluster_id is not unset:
            kwargs["cluster_id"] = cluster_id
        if org_name is not unset:
            kwargs["org_name"] = org_name
        if project_name is not unset:
            kwargs["project_name"] = project_name
        if aggregation_time is not unset:
            kwargs["aggregation_time"] = aggregation_time
        if aggregation_group is not unset:
            kwargs["aggregation_group"] = aggregation_group
        return self._list_bills_endpoint.call_with_http_info(**kwargs)

    def refresh_bills(
        self,
        start: int,
        end: int,
    ) -> BasicTask:
        """Refresh bill.
        :param start: The start of the time range for the query, unit is seconds.
        :type start: int
        :param end: The end of the time range for the query, unit is seconds.
        :type end: int
        :rtype: BasicTask
        """
        kwargs: Dict[str, Any] = {}
        kwargs["start"] = start
        kwargs["end"] = end
        return self._refresh_bills_endpoint.call_with_http_info(**kwargs)
