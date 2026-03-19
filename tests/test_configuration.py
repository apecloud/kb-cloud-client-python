"""Tests for Configuration."""

import os

import pytest

from kb_cloud_client import Configuration


def test_default_host():
    cfg = Configuration()
    assert cfg.host == "https://api.apecloud.com"


def test_host_from_env(monkeypatch):
    monkeypatch.setenv("KB_CLOUD_SITE", "https://api-dev.apecloud.cn")
    cfg = Configuration()
    assert cfg.host == "https://api-dev.apecloud.cn"


def test_explicit_host_takes_precedence(monkeypatch):
    monkeypatch.setenv("KB_CLOUD_SITE", "https://api-dev.apecloud.cn")
    cfg = Configuration(host="https://custom.example.com")
    assert cfg.host == "https://custom.example.com"


def test_host_trailing_slash_stripped():
    cfg = Configuration(host="https://api.apecloud.com/")
    assert cfg.host == "https://api.apecloud.com"


def test_api_key_from_env(monkeypatch):
    monkeypatch.setenv("KB_CLOUD_API_KEY_NAME", "my-key")
    monkeypatch.setenv("KB_CLOUD_API_KEY_SECRET", "my-secret")
    cfg = Configuration()
    assert cfg.api_key_name == "my-key"
    assert cfg.api_key_secret == "my-secret"


def test_explicit_api_key_takes_precedence(monkeypatch):
    monkeypatch.setenv("KB_CLOUD_API_KEY_NAME", "env-key")
    cfg = Configuration(api_key_name="explicit-key")
    assert cfg.api_key_name == "explicit-key"


def test_return_http_data_only_default():
    cfg = Configuration()
    assert cfg.return_http_data_only is True


def test_return_http_data_only_false():
    cfg = Configuration(return_http_data_only=False)
    assert cfg.return_http_data_only is False


def test_add_default_header():
    cfg = Configuration()
    cfg.add_default_header("X-Custom", "value")
    assert cfg.default_headers["X-Custom"] == "value"


def test_default_classmethod():
    cfg = Configuration.default()
    assert isinstance(cfg, Configuration)
