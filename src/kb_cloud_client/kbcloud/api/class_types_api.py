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


class ClasstypesApi:
    """ClassTypes API client.

    Provides methods for the classTypes endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_class_type_endpoint = _Endpoint(
            settings={
                "response_type": ClassType,
                "endpoint_path": "/api/v1/classTypes/{id}",
                "http_method": "GET",
                "operation_id": "get_class_type",
            },
            params_map={
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_class_types_endpoint = _Endpoint(
            settings={
                "response_type": List[ClassType],
                "endpoint_path": "/api/v1/classTypes",
                "http_method": "GET",
                "operation_id": "get_class_types",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def get_class_type(
        self,
        id_: str,
    ) -> ClassType:
        """Get a class type by ID.
        :type id_: str
        :rtype: ClassType
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id_"] = id_
        return self._get_class_type_endpoint.call_with_http_info(**kwargs)

    def get_class_types(
        self,
    ) -> List[ClassType]:
        """Get all class types.
        :rtype: List[ClassType]
        """
        kwargs: Dict[str, Any] = {}
        return self._get_class_types_endpoint.call_with_http_info(**kwargs)
