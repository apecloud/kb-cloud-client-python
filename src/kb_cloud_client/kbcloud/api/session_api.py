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


class SessionApi:
    """Session API client.

    Provides methods for the session endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._kill_session_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/sessions/{session}",
                "http_method": "DELETE",
                "operation_id": "kill_session",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
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
                "session": {
                    "required": True,
                    "location": "path",
                    "attribute": "session",
                },
                "keep": {
                    "location": "query",
                    "attribute": "keep",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_sessions_endpoint = _Endpoint(
            settings={
                "response_type": List[DmsSession],
                "endpoint_path": "/api/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/sessions",
                "http_method": "GET",
                "operation_id": "list_sessions",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
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
                "all": {
                    "location": "query",
                    "attribute": "all",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def kill_session(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        session: str,
        *,
        keep: Union[bool, UnsetType] = unset,
    ) -> APIErrorResponse:
        """Kill cluster session.

        kill a session in cluster
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param session: session id
        :type session: str
        :param keep: if keep is true, the session will not be killed but only closed
        :type keep: bool, optional
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["session"] = session
        if keep is not unset:
            kwargs["keep"] = keep
        return self._kill_session_endpoint.call_with_http_info(**kwargs)

    def list_sessions(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        *,
        all: Union[bool, UnsetType] = unset,
    ) -> List[DmsSession]:
        """List cluster sessions.

        list sessions in cluster
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param all: whether list all session includes sleep
        :type all: bool, optional
        :rtype: List[DmsSession]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if all is not unset:
            kwargs["all"] = all
        return self._list_sessions_endpoint.call_with_http_info(**kwargs)
