# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd

from __future__ import annotations

from typing import Any, List, Optional


class OpenApiException(Exception):
    """Base class for all exceptions raised by this client."""


class ApiTypeError(OpenApiException, TypeError):
    """Raised when a value has the wrong type."""

    def __init__(
        self,
        msg: str,
        path_to_item: Optional[List[Any]] = None,
        valid_classes: Optional[tuple] = None,
        key_type: Optional[bool] = None,
    ):
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = f"{msg} at {_render_path(path_to_item)}"
        super().__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    """Raised when a value is invalid."""

    def __init__(self, msg: str, path_to_item: Optional[List[Any]] = None):
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = f"{msg} at {_render_path(path_to_item)}"
        super().__init__(full_msg)


class ApiAttributeError(OpenApiException, AttributeError):
    """Raised when an attribute reference or assignment fails."""

    def __init__(self, msg: str, path_to_item: Optional[List[Any]] = None):
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = f"{msg} at {_render_path(path_to_item)}"
        super().__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    """Raised when a key is not found."""

    def __init__(self, msg: str, path_to_item: Optional[List[Any]] = None):
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = f"{msg} at {_render_path(path_to_item)}"
        super().__init__(full_msg)


class ApiException(OpenApiException):
    """Raised when an API call returns an error HTTP status code."""

    def __init__(
        self,
        status: Optional[int] = None,
        reason: Optional[str] = None,
        http_resp: Any = None,
    ):
        if http_resp is not None:
            self.status = http_resp.status_code
            self.reason = http_resp.reason
            self.body = http_resp.text
            self.headers = dict(http_resp.headers)
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self) -> str:
        msg = f"({self.status})\nReason: {self.reason}\n"
        if self.headers:
            msg += f"HTTP response headers: {self.headers}\n"
        if self.body:
            msg += f"HTTP response body: {self.body}\n"
        return msg


class NotFoundException(ApiException):
    """Raised when a resource is not found (HTTP 404)."""


class UnauthorizedException(ApiException):
    """Raised when authentication fails (HTTP 401)."""


class ForbiddenException(ApiException):
    """Raised when access is forbidden (HTTP 403)."""


class ServiceException(ApiException):
    """Raised when a server error occurs (HTTP 5xx)."""


def raise_from_response(resp: Any) -> None:
    """Raise the appropriate exception based on HTTP status code."""
    status = resp.status_code
    if status == 401:
        raise UnauthorizedException(http_resp=resp)
    elif status == 403:
        raise ForbiddenException(http_resp=resp)
    elif status == 404:
        raise NotFoundException(http_resp=resp)
    elif status >= 500:
        raise ServiceException(http_resp=resp)
    else:
        raise ApiException(http_resp=resp)


def _render_path(path_to_item: List[Any]) -> str:
    result = ""
    for part in path_to_item:
        if isinstance(part, int):
            result += f"[{part}]"
        else:
            result += f"['{part}']"
    return result
