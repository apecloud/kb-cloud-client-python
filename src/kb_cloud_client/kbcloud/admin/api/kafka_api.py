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


class KafkaApi:
    """Kafka API client.

    Provides methods for the kafka endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_kafka_topic_endpoint = _Endpoint(
            settings={
                "response_type": Topic,
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topics",
                "http_method": "POST",
                "operation_id": "create_kafka_topic",
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
        self._delete_kafka_consumer_group_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/consumer-groups/{groupId}",
                "http_method": "DELETE",
                "operation_id": "delete_kafka_consumer_group",
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
                "group_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "groupId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_kafka_topic_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}",
                "http_method": "DELETE",
                "operation_id": "delete_kafka_topic",
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
                "topic": {
                    "required": True,
                    "location": "path",
                    "attribute": "topic",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._expand_kafka_topic_partitions_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/partitions",
                "http_method": "POST",
                "operation_id": "expand_kafka_topic_partitions",
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
                "topic": {
                    "required": True,
                    "location": "path",
                    "attribute": "topic",
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
        self._get_kafka_broker_configs_endpoint = _Endpoint(
            settings={
                "response_type": List[ConfigEntry],
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/brokers/{brokerId}/configs",
                "http_method": "GET",
                "operation_id": "get_kafka_broker_configs",
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
                "broker_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "brokerId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_kafka_brokers_endpoint = _Endpoint(
            settings={
                "response_type": List[Broker],
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/brokers",
                "http_method": "GET",
                "operation_id": "get_kafka_brokers",
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
        self._get_kafka_consumer_group_describe_endpoint = _Endpoint(
            settings={
                "response_type": List[ConsumerGroupDescribe],
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/consumer-groups/{groupId}",
                "http_method": "GET",
                "operation_id": "get_kafka_consumer_group_describe",
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
                "group_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "groupId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_kafka_topic_brokers_endpoint = _Endpoint(
            settings={
                "response_type": List[Broker],
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/brokers",
                "http_method": "GET",
                "operation_id": "get_kafka_topic_brokers",
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
                "topic": {
                    "required": True,
                    "location": "path",
                    "attribute": "topic",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_kafka_topic_config_endpoint = _Endpoint(
            settings={
                "response_type": List[ConfigEntry],
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/configs",
                "http_method": "GET",
                "operation_id": "get_kafka_topic_config",
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
                "topic": {
                    "required": True,
                    "location": "path",
                    "attribute": "topic",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_kafka_topic_infos_endpoint = _Endpoint(
            settings={
                "response_type": TopicDetails,
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}",
                "http_method": "GET",
                "operation_id": "get_kafka_topic_infos",
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
                "topic": {
                    "required": True,
                    "location": "path",
                    "attribute": "topic",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_kafka_topic_partitions_endpoint = _Endpoint(
            settings={
                "response_type": List[Partition],
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/partitions",
                "http_method": "GET",
                "operation_id": "get_kafka_topic_partitions",
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
                "topic": {
                    "required": True,
                    "location": "path",
                    "attribute": "topic",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_kafka_topics_endpoint = _Endpoint(
            settings={
                "response_type": List[Topic],
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topics",
                "http_method": "GET",
                "operation_id": "get_kafka_topics",
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
                "name_filter": {
                    "location": "query",
                    "attribute": "nameFilter",
                },
                "only_names": {
                    "location": "query",
                    "attribute": "onlyNames",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_kafka_consumer_groups_endpoint = _Endpoint(
            settings={
                "response_type": List[ConsumerGroup],
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/consumer-groups",
                "http_method": "GET",
                "operation_id": "list_kafka_consumer_groups",
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
                "group_id": {
                    "location": "query",
                    "attribute": "groupId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_kafka_topic_consumer_groups_endpoint = _Endpoint(
            settings={
                "response_type": List[ConsumerGroup],
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/consumer-groups",
                "http_method": "GET",
                "operation_id": "list_kafka_topic_consumer_groups",
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
                "topic": {
                    "required": True,
                    "location": "path",
                    "attribute": "topic",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_kafka_topic_consumer_offsets_endpoint = _Endpoint(
            settings={
                "response_type": List[TopicOffset],
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/consumer-groups/{groupId}/offsets",
                "http_method": "GET",
                "operation_id": "list_kafka_topic_consumer_offsets",
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
                "topic": {
                    "required": True,
                    "location": "path",
                    "attribute": "topic",
                },
                "group_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "groupId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_kafka_topic_messages_endpoint = _Endpoint(
            settings={
                "response_type": List[TopicMessage],
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/messages",
                "http_method": "GET",
                "operation_id": "list_kafka_topic_messages",
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
                "topic": {
                    "required": True,
                    "location": "path",
                    "attribute": "topic",
                },
                "partition": {
                    "required": True,
                    "location": "query",
                    "attribute": "partition",
                },
                "offset": {
                    "required": True,
                    "location": "query",
                    "attribute": "offset",
                },
                "count": {
                    "location": "query",
                    "attribute": "count",
                },
                "key_filter": {
                    "location": "query",
                    "attribute": "keyFilter",
                },
                "value_filter": {
                    "location": "query",
                    "attribute": "valueFilter",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._produce_kafka_topic_message_endpoint = _Endpoint(
            settings={
                "response_type": int,
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/messages",
                "http_method": "POST",
                "operation_id": "produce_kafka_topic_message",
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
                "topic": {
                    "required": True,
                    "location": "path",
                    "attribute": "topic",
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
        self._reset_kafka_topic_consumer_offset_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/consumer-groups/{groupId}/offsets",
                "http_method": "PUT",
                "operation_id": "reset_kafka_topic_consumer_offset",
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
                "topic": {
                    "required": True,
                    "location": "path",
                    "attribute": "topic",
                },
                "group_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "groupId",
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
        self._set_kafka_topic_config_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/configs",
                "http_method": "PUT",
                "operation_id": "set_kafka_topic_config",
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
                "topic": {
                    "required": True,
                    "location": "path",
                    "attribute": "topic",
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
        self._update_kafka_broker_config_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/brokers/{brokerId}/configs",
                "http_method": "PUT",
                "operation_id": "update_kafka_broker_config",
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
                "broker_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "brokerId",
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


    def create_kafka_topic(
        self,
        org_name: str,
        cluster_name: str,
        body: CreateTopicRequest,
    ) -> Topic:
        """Create new topic.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :type body: CreateTopicRequest
        :rtype: Topic
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._create_kafka_topic_endpoint.call_with_http_info(**kwargs)

    def delete_kafka_consumer_group(
        self,
        org_name: str,
        cluster_name: str,
        group_id: str,
    ) -> APIErrorResponse:
        """Delete consumer group.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :param group_id: The id of consumer group
        :type group_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["group_id"] = group_id
        return self._delete_kafka_consumer_group_endpoint.call_with_http_info(**kwargs)

    def delete_kafka_topic(
        self,
        org_name: str,
        cluster_name: str,
        topic: str,
    ) -> APIErrorResponse:
        """Delete topic.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :type topic: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["topic"] = topic
        return self._delete_kafka_topic_endpoint.call_with_http_info(**kwargs)

    def expand_kafka_topic_partitions(
        self,
        org_name: str,
        cluster_name: str,
        topic: str,
        body: ExpandPartitionRequest,
    ) -> APIErrorResponse:
        """expand topic partition.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :type topic: str
        :type body: ExpandPartitionRequest
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["topic"] = topic
        kwargs["body"] = body
        return self._expand_kafka_topic_partitions_endpoint.call_with_http_info(**kwargs)

    def get_kafka_broker_configs(
        self,
        org_name: str,
        cluster_name: str,
        broker_id: int,
    ) -> List[ConfigEntry]:
        """Get all configs of a broker.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :param broker_id: The id of broker
        :type broker_id: int
        :rtype: List[ConfigEntry]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["broker_id"] = broker_id
        return self._get_kafka_broker_configs_endpoint.call_with_http_info(**kwargs)

    def get_kafka_brokers(
        self,
        org_name: str,
        cluster_name: str,
    ) -> List[Broker]:
        """Get all brokers in cluster.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :rtype: List[Broker]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._get_kafka_brokers_endpoint.call_with_http_info(**kwargs)

    def get_kafka_consumer_group_describe(
        self,
        org_name: str,
        cluster_name: str,
        group_id: str,
    ) -> List[ConsumerGroupDescribe]:
        """Get consumer group describe.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :param group_id: The id of consumer group
        :type group_id: str
        :rtype: List[ConsumerGroupDescribe]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["group_id"] = group_id
        return self._get_kafka_consumer_group_describe_endpoint.call_with_http_info(**kwargs)

    def get_kafka_topic_brokers(
        self,
        org_name: str,
        cluster_name: str,
        topic: str,
    ) -> List[Broker]:
        """Get broker distributions of topic.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :type topic: str
        :rtype: List[Broker]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["topic"] = topic
        return self._get_kafka_topic_brokers_endpoint.call_with_http_info(**kwargs)

    def get_kafka_topic_config(
        self,
        org_name: str,
        cluster_name: str,
        topic: str,
    ) -> List[ConfigEntry]:
        """Get topic configuration.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :type topic: str
        :rtype: List[ConfigEntry]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["topic"] = topic
        return self._get_kafka_topic_config_endpoint.call_with_http_info(**kwargs)

    def get_kafka_topic_infos(
        self,
        org_name: str,
        cluster_name: str,
        topic: str,
    ) -> TopicDetails:
        """Get topic Infos.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :type topic: str
        :rtype: TopicDetails
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["topic"] = topic
        return self._get_kafka_topic_infos_endpoint.call_with_http_info(**kwargs)

    def get_kafka_topic_partitions(
        self,
        org_name: str,
        cluster_name: str,
        topic: str,
    ) -> List[Partition]:
        """Get partition list of topic.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :type topic: str
        :rtype: List[Partition]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["topic"] = topic
        return self._get_kafka_topic_partitions_endpoint.call_with_http_info(**kwargs)

    def get_kafka_topics(
        self,
        org_name: str,
        cluster_name: str,
        *,
        name_filter: Union[str, UnsetType] = unset,
        only_names: Union[bool, UnsetType] = unset,
    ) -> List[Topic]:
        """Get all topics in cluster.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :param name_filter: search pattern, support prefix search
        :type name_filter: str, optional
        :param only_names: if true, only return topic names
        :type only_names: bool, optional
        :rtype: List[Topic]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if name_filter is not unset:
            kwargs["name_filter"] = name_filter
        if only_names is not unset:
            kwargs["only_names"] = only_names
        return self._get_kafka_topics_endpoint.call_with_http_info(**kwargs)

    def list_kafka_consumer_groups(
        self,
        org_name: str,
        cluster_name: str,
        *,
        group_id: Union[str, UnsetType] = unset,
    ) -> List[ConsumerGroup]:
        """List all consumer groups.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :param group_id: the id of consumer group
        :type group_id: str, optional
        :rtype: List[ConsumerGroup]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if group_id is not unset:
            kwargs["group_id"] = group_id
        return self._list_kafka_consumer_groups_endpoint.call_with_http_info(**kwargs)

    def list_kafka_topic_consumer_groups(
        self,
        org_name: str,
        cluster_name: str,
        topic: str,
    ) -> List[ConsumerGroup]:
        """List consumer groups of topic.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :param topic: The name of topic
        :type topic: str
        :rtype: List[ConsumerGroup]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["topic"] = topic
        return self._list_kafka_topic_consumer_groups_endpoint.call_with_http_info(**kwargs)

    def list_kafka_topic_consumer_offsets(
        self,
        org_name: str,
        cluster_name: str,
        topic: str,
        group_id: str,
    ) -> List[TopicOffset]:
        """List consumer offsets of topic.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :param topic: The name of topic
        :type topic: str
        :param group_id: The id of consumer group
        :type group_id: str
        :rtype: List[TopicOffset]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["topic"] = topic
        kwargs["group_id"] = group_id
        return self._list_kafka_topic_consumer_offsets_endpoint.call_with_http_info(**kwargs)

    def list_kafka_topic_messages(
        self,
        org_name: str,
        cluster_name: str,
        topic: str,
        partition: int,
        offset: int,
        *,
        count: Union[int, UnsetType] = unset,
        key_filter: Union[str, UnsetType] = unset,
        value_filter: Union[str, UnsetType] = unset,
    ) -> List[TopicMessage]:
        """List messages from topic.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :type topic: str
        :type partition: int
        :type offset: int
        :param count: 获取消息的数量
        :type count: int, optional
        :param key_filter: 消息 key 的过滤条件（大小写不敏感）
        :type key_filter: str, optional
        :param value_filter: 消息内容的过滤条件（大小写不敏感）
        :type value_filter: str, optional
        :rtype: List[TopicMessage]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["topic"] = topic
        kwargs["partition"] = partition
        kwargs["offset"] = offset
        if count is not unset:
            kwargs["count"] = count
        if key_filter is not unset:
            kwargs["key_filter"] = key_filter
        if value_filter is not unset:
            kwargs["value_filter"] = value_filter
        return self._list_kafka_topic_messages_endpoint.call_with_http_info(**kwargs)

    def produce_kafka_topic_message(
        self,
        org_name: str,
        cluster_name: str,
        topic: str,
        body: TopicMessageRequest,
    ) -> int:
        """Produce message to topic.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :type topic: str
        :type body: TopicMessageRequest
        :rtype: int
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["topic"] = topic
        kwargs["body"] = body
        return self._produce_kafka_topic_message_endpoint.call_with_http_info(**kwargs)

    def reset_kafka_topic_consumer_offset(
        self,
        org_name: str,
        cluster_name: str,
        topic: str,
        group_id: str,
        body: ResetOffsetRequest,
    ) -> APIErrorResponse:
        """Reset consumer offset of topic.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :param topic: The name of topic
        :type topic: str
        :param group_id: The id of consumer group
        :type group_id: str
        :type body: ResetOffsetRequest
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["topic"] = topic
        kwargs["group_id"] = group_id
        kwargs["body"] = body
        return self._reset_kafka_topic_consumer_offset_endpoint.call_with_http_info(**kwargs)

    def set_kafka_topic_config(
        self,
        org_name: str,
        cluster_name: str,
        topic: str,
        body: UpdateTopicConfigRequest,
    ) -> APIErrorResponse:
        """Update topic configuration.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :type topic: str
        :type body: UpdateTopicConfigRequest
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["topic"] = topic
        kwargs["body"] = body
        return self._set_kafka_topic_config_endpoint.call_with_http_info(**kwargs)

    def update_kafka_broker_config(
        self,
        org_name: str,
        cluster_name: str,
        broker_id: int,
        body: UpdateBrokerConfigRequest,
    ) -> APIErrorResponse:
        """Update broker config.
        :param org_name: The name of organization
        :type org_name: str
        :param cluster_name: The name of cluster
        :type cluster_name: str
        :param broker_id: The id of broker
        :type broker_id: int
        :type body: UpdateBrokerConfigRequest
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["broker_id"] = broker_id
        kwargs["body"] = body
        return self._update_kafka_broker_config_endpoint.call_with_http_info(**kwargs)
