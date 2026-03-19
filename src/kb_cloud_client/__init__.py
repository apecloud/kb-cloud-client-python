# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
"""KubeBlocks Cloud Python client.

Packages:
  kbcloud        – user-portal API
  kbcloud.admin  – admin-portal API
"""

from . import kbcloud
from ._version import __version__
from .api_client import ApiClient, UnsetType, unset
from .configuration import Configuration
from .exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    ForbiddenException,
    NotFoundException,
    OpenApiException,
    ServiceException,
    UnauthorizedException,
)

__all__ = [
    "__version__",
    "ApiClient",
    "Configuration",
    "unset",
    "UnsetType",
    "OpenApiException",
    "ApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiAttributeError",
    "ApiKeyError",
    "NotFoundException",
    "UnauthorizedException",
    "ForbiddenException",
    "ServiceException",
    "kbcloud",
]
