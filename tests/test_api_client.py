"""Tests for ApiClient internals (no network required)."""
import json
import pytest
from unittest.mock import MagicMock, patch
from kb_cloud_client import ApiClient, Configuration
from kb_cloud_client.api_client import (
    Endpoint,
    _deserialize_value,
    _parse_datetime,
    unset,
    UnsetType,
)
from kb_cloud_client.exceptions import NotFoundException, UnauthorizedException


# ── unset sentinel ────────────────────────────────────────────────────────────

def test_unset_is_singleton():
    from kb_cloud_client.api_client import _Unset
    assert _Unset() is unset


def test_unset_is_falsy():
    assert not unset


def test_unset_repr():
    assert repr(unset) == "unset"


def test_unset_type():
    assert isinstance(unset, UnsetType)


# ── _parse_datetime ───────────────────────────────────────────────────────────

def test_parse_datetime_z_suffix():
    from datetime import timezone
    dt = _parse_datetime("2026-03-11T07:15:02.582Z")
    assert dt.tzinfo == timezone.utc
    assert dt.year == 2026
    assert dt.month == 3


def test_parse_datetime_passthrough_non_string():
    assert _parse_datetime(None) is None
    assert _parse_datetime(42) == 42


def test_parse_datetime_invalid_string():
    assert _parse_datetime("not-a-date") == "not-a-date"


# ── _deserialize_value ────────────────────────────────────────────────────────

def test_deserialize_none():
    assert _deserialize_value(None, str) is None


def test_deserialize_list():
    from typing import List
    result = _deserialize_value([1, 2, 3], List[int])
    assert result == [1, 2, 3]


def test_deserialize_dict():
    from typing import Dict
    result = _deserialize_value({"a": 1}, Dict[str, int])
    assert result == {"a": 1}


def test_deserialize_optional_present():
    from typing import Optional
    result = _deserialize_value("hello", Optional[str])
    assert result == "hello"


def test_deserialize_optional_none():
    from typing import Optional
    result = _deserialize_value(None, Optional[str])
    assert result is None


def test_deserialize_model_via_from_dict():
    class FakeModel:
        @classmethod
        def from_dict(cls, data):
            obj = cls()
            obj.name = data["name"]
            return obj

    result = _deserialize_value({"name": "test"}, FakeModel)
    assert result.name == "test"


# ── ApiClient._sanitize_params ────────────────────────────────────────────────

def test_sanitize_params_skips_none():
    cfg = Configuration()
    client = ApiClient(cfg)
    result = client._sanitize_params({"a": 1, "b": None, "c": "x"}, {})
    assert "b" not in result
    assert result["a"] == 1


def test_sanitize_params_csv():
    cfg = Configuration()
    client = ApiClient(cfg)
    result = client._sanitize_params({"ids": [1, 2, 3]}, {"ids": "csv"})
    assert result["ids"] == "1,2,3"


def test_sanitize_params_multi():
    cfg = Configuration()
    client = ApiClient(cfg)
    result = client._sanitize_params({"tags": ["a", "b"]}, {"tags": "multi"})
    assert result["tags"] == ["a", "b"]


# ── ApiClient._serialize ──────────────────────────────────────────────────────

def test_serialize_none():
    client = ApiClient(Configuration())
    assert client._serialize(None) is None


def test_serialize_dict():
    client = ApiClient(Configuration())
    result = client._serialize({"key": "value"})
    assert json.loads(result) == {"key": "value"}


def test_serialize_model_with_to_dict():
    class FakeModel:
        def to_dict(self):
            return {"field": "val"}

    client = ApiClient(Configuration())
    result = client._serialize(FakeModel())
    assert json.loads(result) == {"field": "val"}


# ── ApiClient._build_url ──────────────────────────────────────────────────────

def test_build_url_no_params():
    client = ApiClient(Configuration(host="https://api.example.com"))
    assert client._build_url("/v1/orgs") == "https://api.example.com/v1/orgs"


def test_build_url_with_path_params():
    client = ApiClient(Configuration(host="https://api.example.com"))
    url = client._build_url("/v1/orgs/{orgName}/clusters", {"orgName": "my org"})
    assert url == "https://api.example.com/v1/orgs/my%20org/clusters"


# ── Endpoint.call_with_http_info ──────────────────────────────────────────────

def _make_endpoint(api_client, path="/test", method="GET", response_type=None):
    return Endpoint(
        settings={
            "response_type": response_type,
            "endpoint_path": path,
            "http_method": method,
            "operation_id": "test_op",
        },
        params_map={
            "org_name": {"location": "path", "attribute": "orgName"},
            "page": {"location": "query", "attribute": "page"},
            "body": {"location": "body"},
        },
        headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
        api_client=api_client,
    )


def test_endpoint_routes_path_param():
    client = ApiClient(Configuration())
    captured = {}

    def fake_call_api(**kwargs):
        captured.update(kwargs)
        return None

    client.call_api = fake_call_api
    ep = _make_endpoint(client, path="/orgs/{orgName}")
    ep.call_with_http_info(org_name="acme")
    assert captured["path_params"] == {"orgName": "acme"}


def test_endpoint_routes_query_param():
    client = ApiClient(Configuration())
    captured = {}

    def fake_call_api(**kwargs):
        captured.update(kwargs)
        return None

    client.call_api = fake_call_api
    ep = _make_endpoint(client)
    ep.call_with_http_info(page=2)
    assert captured["query_params"] == {"page": 2}


def test_endpoint_routes_body():
    client = ApiClient(Configuration())
    captured = {}

    def fake_call_api(**kwargs):
        captured.update(kwargs)
        return None

    client.call_api = fake_call_api
    ep = _make_endpoint(client, method="POST")
    ep.call_with_http_info(body={"name": "test"})
    assert captured["body"] == {"name": "test"}
