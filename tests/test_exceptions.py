"""Tests for exception hierarchy."""

import pytest

from kb_cloud_client import (
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
from kb_cloud_client.exceptions import raise_from_response


class _FakeResponse:
    def __init__(self, status_code: int, reason: str = "Reason", text: str = "body"):
        self.status_code = status_code
        self.reason = reason
        self.text = text
        self.headers = {"Content-Type": "application/json"}


def test_hierarchy():
    assert issubclass(ApiException, OpenApiException)
    assert issubclass(NotFoundException, ApiException)
    assert issubclass(UnauthorizedException, ApiException)
    assert issubclass(ForbiddenException, ApiException)
    assert issubclass(ServiceException, ApiException)
    assert issubclass(ApiTypeError, OpenApiException)
    assert issubclass(ApiTypeError, TypeError)
    assert issubclass(ApiValueError, OpenApiException)
    assert issubclass(ApiValueError, ValueError)
    assert issubclass(ApiAttributeError, OpenApiException)
    assert issubclass(ApiAttributeError, AttributeError)
    assert issubclass(ApiKeyError, OpenApiException)
    assert issubclass(ApiKeyError, KeyError)


def test_raise_from_response_401():
    with pytest.raises(UnauthorizedException) as exc_info:
        raise_from_response(_FakeResponse(401))
    assert exc_info.value.status == 401


def test_raise_from_response_403():
    with pytest.raises(ForbiddenException):
        raise_from_response(_FakeResponse(403))


def test_raise_from_response_404():
    with pytest.raises(NotFoundException):
        raise_from_response(_FakeResponse(404))


def test_raise_from_response_500():
    with pytest.raises(ServiceException):
        raise_from_response(_FakeResponse(500))


def test_raise_from_response_400():
    with pytest.raises(ApiException):
        raise_from_response(_FakeResponse(400))


def test_api_exception_str():
    exc = ApiException(http_resp=_FakeResponse(422, "Unprocessable Entity", "bad input"))
    s = str(exc)
    assert "422" in s
    assert "Unprocessable Entity" in s
    assert "bad input" in s


def test_api_type_error_with_path():
    exc = ApiTypeError("wrong type", path_to_item=["items", 0, "name"])
    assert "items" in str(exc)
    assert "0" in str(exc)


def test_api_value_error():
    exc = ApiValueError("invalid value", path_to_item=["field"])
    assert "invalid value" in str(exc)
    assert "field" in str(exc)
