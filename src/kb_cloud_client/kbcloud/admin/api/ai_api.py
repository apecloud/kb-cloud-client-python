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


class AiApi:
    """AI API client.

    Provides methods for the AI endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._chat_biv2_sse_endpoint = _Endpoint(
            settings={
                "response_type": ChatResponse,
                "endpoint_path": "/admin/v1/ai/chatbi/v2",
                "http_method": "POST",
                "operation_id": "chat_biv2_sse",
            },
            params_map={
                "body": {
                    "required": True,
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["text/event-stream", "application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._chat_v2_sse_endpoint = _Endpoint(
            settings={
                "response_type": ChatResponse,
                "endpoint_path": "/admin/v1/ai/chatops/v2",
                "http_method": "POST",
                "operation_id": "chat_v2_sse",
            },
            params_map={
                "body": {
                    "required": True,
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["text/event-stream", "application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_conversation_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/ai/conversations/{conversationId}",
                "http_method": "DELETE",
                "operation_id": "delete_conversation",
            },
            params_map={
                "conversation_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "conversationId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_conversation_messages_endpoint = _Endpoint(
            settings={
                "response_type": AiMessageListResponse,
                "endpoint_path": "/admin/v1/ai/conversations/{conversationId}/messages",
                "http_method": "GET",
                "operation_id": "get_conversation_messages",
            },
            params_map={
                "conversation_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "conversationId",
                },
                "pre": {
                    "location": "query",
                    "attribute": "pre",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_conversations_endpoint = _Endpoint(
            settings={
                "response_type": AiConversationListResponse,
                "endpoint_path": "/admin/v1/ai/conversations",
                "http_method": "GET",
                "operation_id": "list_conversations",
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
                "type_": {
                    "location": "query",
                    "attribute": "type",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._new_ai_conversation_endpoint = _Endpoint(
            settings={
                "response_type": AiConversation,
                "endpoint_path": "/admin/v1/ai/conversations",
                "http_method": "POST",
                "operation_id": "new_ai_conversation",
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


    def chat_biv2_sse(
        self,
        body: ChatRequest,
    ) -> ChatResponse:
        """SSE endpoint for Chat BI V2.

        Establishes an SSE connection for AI BI conversation.
        :type body: ChatRequest
        :rtype: ChatResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._chat_biv2_sse_endpoint.call_with_http_info(**kwargs)

    def chat_v2_sse(
        self,
        body: ChatRequest,
    ) -> ChatResponse:
        """SSE endpoint for Chat V2.

        Establishes an SSE connection for AI conversation.
        :type body: ChatRequest
        :rtype: ChatResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._chat_v2_sse_endpoint.call_with_http_info(**kwargs)

    def delete_conversation(
        self,
        conversation_id: str,
    ) -> APIErrorResponse:
        """Delete a conversation.

        Deletes a specific conversation and all its associated messages.
        :param conversation_id: ID of the conversation to delete
        :type conversation_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["conversation_id"] = conversation_id
        return self._delete_conversation_endpoint.call_with_http_info(**kwargs)

    def get_conversation_messages(
        self,
        conversation_id: str,
        *,
        pre: Union[str, UnsetType] = unset,
    ) -> AiMessageListResponse:
        """Get AI conversation messages.

        Retrieves ai messages for a specific conversation. If pre is not provided, returns the last 10 turn messages. If pre is provided, returns 10 turn messages after the pre message.
        :param conversation_id: ID of the conversation
        :type conversation_id: str
        :param pre: Previous message ID
        :type pre: str, optional
        :rtype: AiMessageListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["conversation_id"] = conversation_id
        if pre is not unset:
            kwargs["pre"] = pre
        return self._get_conversation_messages_endpoint.call_with_http_info(**kwargs)

    def list_conversations(
        self,
        *,
        page: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        type_: Union[str, UnsetType] = unset,
    ) -> AiConversationListResponse:
        """List conversations by user.

        Retrieves a list of conversations filtered by user.
        :param page: Page number for pagination
        :type page: int, optional
        :param page_size: Number of items per page
        :type page_size: int, optional
        :param type_: Type of conversations to filter, can be bi or analysis.
        :type type_: str, optional
        :rtype: AiConversationListResponse
        """
        kwargs: Dict[str, Any] = {}
        if page is not unset:
            kwargs["page"] = page
        if page_size is not unset:
            kwargs["page_size"] = page_size
        if type_ is not unset:
            kwargs["type_"] = type_
        return self._list_conversations_endpoint.call_with_http_info(**kwargs)

    def new_ai_conversation(
        self,
        body: AIConversationRequest,
    ) -> AiConversation:
        """Create a new conversation.

        Creates a new conversation.
        :type body: AIConversationRequest
        :rtype: AiConversation
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._new_ai_conversation_endpoint.call_with_http_info(**kwargs)
