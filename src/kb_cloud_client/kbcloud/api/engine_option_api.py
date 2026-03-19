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


class EngineoptionApi:
    """EngineOption API client.

    Provides methods for the engineOption endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_engine_option_endpoint = _Endpoint(
            settings={
                "response_type": EngineOption,
                "endpoint_path": "/api/v1/engineOptions/{engineName}",
                "http_method": "GET",
                "operation_id": "get_engine_option",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_engine_options_endpoint = _Endpoint(
            settings={
                "response_type": EngineOptionList,
                "endpoint_path": "/api/v1/engineOptions",
                "http_method": "GET",
                "operation_id": "list_engine_options",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def get_engine_option(
        self,
        engine_name: str,
    ) -> EngineOption:
        """Get engineOption.

        Get a engineOption detail
        :param engine_name: Name of the engineOption
        :type engine_name: str
        :rtype: EngineOption
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        return self._get_engine_option_endpoint.call_with_http_info(**kwargs)

    def list_engine_options(
        self,
    ) -> EngineOptionList:
        """List all engineOptions.

        list all engineOptions
        :rtype: EngineOptionList
        """
        kwargs: Dict[str, Any] = {}
        return self._list_engine_options_endpoint.call_with_http_info(**kwargs)
