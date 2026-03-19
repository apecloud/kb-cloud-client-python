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


class DisasterrecoveryApi:
    """DisasterRecovery API client.

    Provides methods for the disasterRecovery endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_disaster_recovery_endpoint = _Endpoint(
            settings={
                "response_type": DisasterRecoveryTask,
                "endpoint_path": "/api/v1/organizations/{orgName}/parent/{parentClusterID}/disasterRecovery",
                "http_method": "POST",
                "operation_id": "create_disaster_recovery",
                "deprecated": True,
            },
            params_map={
                "parent_cluster_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "parentClusterID",
                },
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
        self._delete_disaster_recovery_endpoint = _Endpoint(
            settings={
                "response_type": DisasterRecoveryTask,
                "endpoint_path": "/api/v1/organizations/{orgName}/disasterRecovery",
                "http_method": "DELETE",
                "operation_id": "delete_disaster_recovery",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "logical_instance_id": {
                    "location": "query",
                    "attribute": "logicalInstanceID",
                },
                "cluster_id": {
                    "location": "query",
                    "attribute": "clusterID",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_disaster_recovery_history_endpoint = _Endpoint(
            settings={
                "response_type": DisasterRecoveryHistory,
                "endpoint_path": "/api/v1/organizations/{orgName}/disasterRecovery/{clusterID}/switchHistory",
                "http_method": "GET",
                "operation_id": "get_disaster_recovery_history",
                "deprecated": True,
            },
            params_map={
                "cluster_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "clusterID",
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
        self._get_disaster_recovery_status_endpoint = _Endpoint(
            settings={
                "response_type": DisasterRecoveryStatusResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/disasterRecovery/{clusterID}/status",
                "http_method": "GET",
                "operation_id": "get_disaster_recovery_status",
                "deprecated": True,
            },
            params_map={
                "cluster_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "clusterID",
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
        self._list_disaster_recovery_endpoint = _Endpoint(
            settings={
                "response_type": DisasterRecoveryClusterList,
                "endpoint_path": "/api/v1/organizations/{orgName}/parent/{parentClusterID}/disasterRecovery",
                "http_method": "GET",
                "operation_id": "list_disaster_recovery",
                "deprecated": True,
            },
            params_map={
                "parent_cluster_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "parentClusterID",
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
        self._promote_disaster_recovery_endpoint = _Endpoint(
            settings={
                "response_type": DisasterRecoveryTask,
                "endpoint_path": "/api/v1/organizations/{orgName}/disasterRecovery/{clusterID}/promote",
                "http_method": "POST",
                "operation_id": "promote_disaster_recovery",
                "deprecated": True,
            },
            params_map={
                "cluster_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "clusterID",
                },
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


    def create_disaster_recovery(
        self,
        parent_cluster_id: str,
        org_name: str,
        body: DisasterRecoveryCreate,
    ) -> DisasterRecoveryTask:
        """Create a new disaster recovery instance.

        Create a new disaster recovery instance for a database cluster.
        :param parent_cluster_id: The ID of the parent database cluster
        :type parent_cluster_id: str
        :param org_name: name of the org
        :type org_name: str
        :type body: DisasterRecoveryCreate
        :rtype: DisasterRecoveryTask
        """
        warnings.warn("create_disaster_recovery is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["parent_cluster_id"] = parent_cluster_id
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_disaster_recovery_endpoint.call_with_http_info(**kwargs)

    def delete_disaster_recovery(
        self,
        org_name: str,
        *,
        logical_instance_id: Union[str, UnsetType] = unset,
        cluster_id: Union[str, UnsetType] = unset,
    ) -> DisasterRecoveryTask:
        """Delete a disaster recovery instance.

        Delete a specific disaster recovery instance
        :param org_name: name of the org
        :type org_name: str
        :param logical_instance_id: The ID of the disaster recovery logical instance
        :type logical_instance_id: str, optional
        :param cluster_id: The ID of the disaster recovery cluster
        :type cluster_id: str, optional
        :rtype: DisasterRecoveryTask
        """
        warnings.warn("delete_disaster_recovery is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        if logical_instance_id is not unset:
            kwargs["logical_instance_id"] = logical_instance_id
        if cluster_id is not unset:
            kwargs["cluster_id"] = cluster_id
        return self._delete_disaster_recovery_endpoint.call_with_http_info(**kwargs)

    def get_disaster_recovery_history(
        self,
        cluster_id: str,
        org_name: str,
    ) -> DisasterRecoveryHistory:
        """Get switch history of a disaster recovery instance.

        Retrieve the history of failover and failback operations for a specific disaster recovery instance.
        :param cluster_id: The ID of the disaster recovery instance
        :type cluster_id: str
        :param org_name: name of the org
        :type org_name: str
        :rtype: DisasterRecoveryHistory
        """
        warnings.warn("get_disaster_recovery_history is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["cluster_id"] = cluster_id
        kwargs["org_name"] = org_name
        return self._get_disaster_recovery_history_endpoint.call_with_http_info(**kwargs)

    def get_disaster_recovery_status(
        self,
        cluster_id: str,
        org_name: str,
    ) -> DisasterRecoveryStatusResponse:
        """Retrieve Disaster Recovery Instance Status.

        Get detailed information about the status of a specific disaster recovery instance, including delay and current replication point.
        :param cluster_id: Unique identifier of the disaster recovery instance
        :type cluster_id: str
        :param org_name: Name of the organization
        :type org_name: str
        :rtype: DisasterRecoveryStatusResponse
        """
        warnings.warn("get_disaster_recovery_status is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["cluster_id"] = cluster_id
        kwargs["org_name"] = org_name
        return self._get_disaster_recovery_status_endpoint.call_with_http_info(**kwargs)

    def list_disaster_recovery(
        self,
        parent_cluster_id: str,
        org_name: str,
    ) -> DisasterRecoveryClusterList:
        """List Disaster Recovery instances under the main cluster.

        Retrieve a list of disaster recovery instances for a specific database cluster.
        :param parent_cluster_id: The ID of the parent database cluster
        :type parent_cluster_id: str
        :param org_name: name of the org
        :type org_name: str
        :rtype: DisasterRecoveryClusterList
        """
        warnings.warn("list_disaster_recovery is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["parent_cluster_id"] = parent_cluster_id
        kwargs["org_name"] = org_name
        return self._list_disaster_recovery_endpoint.call_with_http_info(**kwargs)

    def promote_disaster_recovery(
        self,
        cluster_id: str,
        org_name: str,
        body: DisasterRecoveryPromote,
    ) -> DisasterRecoveryTask:
        """Promote a disaster recovery instance to the main instance.

        Promote the disaster recovery instance to the primary database instance.
        :param cluster_id: The ID of the disaster recovery instance
        :type cluster_id: str
        :param org_name: name of the org
        :type org_name: str
        :type body: DisasterRecoveryPromote
        :rtype: DisasterRecoveryTask
        """
        warnings.warn("promote_disaster_recovery is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["cluster_id"] = cluster_id
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._promote_disaster_recovery_endpoint.call_with_http_info(**kwargs)
