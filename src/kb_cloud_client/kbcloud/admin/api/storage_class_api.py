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


class StorageclassApi:
    """StorageClass API client.

    Provides methods for the storageClass endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_storage_class_endpoint = _Endpoint(
            settings={
                "response_type": StorageClassInfo,
                "endpoint_path": "/admin/v1/environments/{environmentName}/storageClasses",
                "http_method": "POST",
                "operation_id": "create_storage_class",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "body": {
                    "required": True,
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_storage_class_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}",
                "http_method": "DELETE",
                "operation_id": "delete_storage_class",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "storage_class_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "storageClassName",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._get_storage_class_endpoint = _Endpoint(
            settings={
                "response_type": StorageClassInfo,
                "endpoint_path": "/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}",
                "http_method": "GET",
                "operation_id": "get_storage_class",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "storage_class_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "storageClassName",
                },
                "with_stats_by_node": {
                    "location": "query",
                    "attribute": "withStatsByNode",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._list_storage_class_node_stats_endpoint = _Endpoint(
            settings={
                "response_type": StorageClassNodeStatsList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}/nodeStats",
                "http_method": "GET",
                "operation_id": "list_storage_class_node_stats",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "storage_class_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "storageClassName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_storage_class_pvcs_endpoint = _Endpoint(
            settings={
                "response_type": PersistentVolumeClaimList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}/pvcs",
                "http_method": "GET",
                "operation_id": "list_storage_class_pvcs",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "storage_class_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "storageClassName",
                },
                "page_id": {
                    "required": True,
                    "location": "query",
                    "attribute": "pageId",
                },
                "page_size": {
                    "required": True,
                    "location": "query",
                    "attribute": "pageSize",
                },
                "node": {
                    "location": "query",
                    "attribute": "node",
                },
                "org_name": {
                    "location": "query",
                    "attribute": "orgName",
                },
                "cluster_name": {
                    "location": "query",
                    "attribute": "clusterName",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._list_storage_classes_endpoint = _Endpoint(
            settings={
                "response_type": StorageClassList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/storageClasses",
                "http_method": "GET",
                "operation_id": "list_storage_classes",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._list_storage_provisioners_endpoint = _Endpoint(
            settings={
                "response_type": StorageProvisionerList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/storageProvisioners",
                "http_method": "GET",
                "operation_id": "list_storage_provisioners",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._update_storage_class_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}",
                "http_method": "PATCH",
                "operation_id": "update_storage_class",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "storage_class_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "storageClassName",
                },
                "body": {
                    "required": True,
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )


    def create_storage_class(
        self,
        environment_name: str,
        body: StorageClassCreate,
    ) -> StorageClassInfo:
        """create storage class.

        Create storage class for the specified environment.
        :param environment_name: Name of the Environment
        :type environment_name: str
        :param body: Fields used to create the storage class
        :type body: StorageClassCreate
        :rtype: StorageClassInfo
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["body"] = body
        return self._create_storage_class_endpoint.call_with_http_info(**kwargs)

    def delete_storage_class(
        self,
        environment_name: str,
        storage_class_name: str,
    ) -> Dict[str, Any]:
        """Delete storage class.

        Delete the storage class for the specified environment.
        :param environment_name: Name of the Environment
        :type environment_name: str
        :param storage_class_name: Name of the Storage Class to be deleted
        :type storage_class_name: str
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["storage_class_name"] = storage_class_name
        return self._delete_storage_class_endpoint.call_with_http_info(**kwargs)

    def get_storage_class(
        self,
        environment_name: str,
        storage_class_name: str,
        *,
        with_stats_by_node: Union[bool, UnsetType] = unset,
    ) -> StorageClassInfo:
        """get storage class.

        get the storage class for the specified environment.
        :param environment_name: Name of the Environment
        :type environment_name: str
        :param storage_class_name: Name of the Storage Class to be updated
        :type storage_class_name: str
        :param with_stats_by_node: defined whether to search for volume statistics by node. If not set, returns without the stats.
        :type with_stats_by_node: bool, optional
        :rtype: StorageClassInfo
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["storage_class_name"] = storage_class_name
        if with_stats_by_node is not unset:
            kwargs["with_stats_by_node"] = with_stats_by_node
        return self._get_storage_class_endpoint.call_with_http_info(**kwargs)

    def list_storage_class_node_stats(
        self,
        environment_name: str,
        storage_class_name: str,
    ) -> StorageClassNodeStatsList:
        """get node stats of the storage class.

        get the node stats related to the specified storage class for the specified environment.
        :param environment_name: Name of the Environment
        :type environment_name: str
        :param storage_class_name: Name of the Storage Class to be specified
        :type storage_class_name: str
        :rtype: StorageClassNodeStatsList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["storage_class_name"] = storage_class_name
        return self._list_storage_class_node_stats_endpoint.call_with_http_info(**kwargs)

    def list_storage_class_pvcs(
        self,
        environment_name: str,
        storage_class_name: str,
        page_id: int,
        page_size: int,
        *,
        node: Union[str, UnsetType] = unset,
        org_name: Union[str, UnsetType] = unset,
        cluster_name: Union[str, UnsetType] = unset,
    ) -> PersistentVolumeClaimList:
        """get persistentvolumeclaim list of the storage class.

        get the persistentvolumeclaim list related to the specified storage class for the specified environment.
        :param environment_name: Name of the Environment
        :type environment_name: str
        :param storage_class_name: Name of the Storage Class to be specified
        :type storage_class_name: str
        :param page_id: defined page id.
        :type page_id: int
        :param page_size: defined page size.
        :type page_size: int
        :param node: Name of the Node to be specified
        :type node: str, optional
        :param org_name: Name of the Org to be specified
        :type org_name: str, optional
        :param cluster_name: Name of the Cluster to be specified
        :type cluster_name: str, optional
        :rtype: PersistentVolumeClaimList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["storage_class_name"] = storage_class_name
        kwargs["page_id"] = page_id
        kwargs["page_size"] = page_size
        if node is not unset:
            kwargs["node"] = node
        if org_name is not unset:
            kwargs["org_name"] = org_name
        if cluster_name is not unset:
            kwargs["cluster_name"] = cluster_name
        return self._list_storage_class_pvcs_endpoint.call_with_http_info(**kwargs)

    def list_storage_classes(
        self,
        environment_name: str,
    ) -> StorageClassList:
        """List storage classes of a environment.

        Provides a summary of storage class statistics.
        :param environment_name: name of the Environment
        :type environment_name: str
        :rtype: StorageClassList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._list_storage_classes_endpoint.call_with_http_info(**kwargs)

    def list_storage_provisioners(
        self,
        environment_name: str,
    ) -> StorageProvisionerList:
        """List the provisioners that can be used by storage class of a environment.

        Provides a summary of storage provisioners statistics.
        :param environment_name: name of the Environment
        :type environment_name: str
        :rtype: StorageProvisionerList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._list_storage_provisioners_endpoint.call_with_http_info(**kwargs)

    def update_storage_class(
        self,
        environment_name: str,
        storage_class_name: str,
        body: StorageClassUpdate,
    ) -> Dict[str, Any]:
        """Update storage class.

        Updates the  storage class for the specified environment.
        :param environment_name: Name of the Environment
        :type environment_name: str
        :param storage_class_name: Name of the Storage Class to be updated
        :type storage_class_name: str
        :param body: Fields to update for the storage class
        :type body: StorageClassUpdate
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["storage_class_name"] = storage_class_name
        kwargs["body"] = body
        return self._update_storage_class_endpoint.call_with_http_info(**kwargs)
