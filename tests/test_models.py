"""Tests for generated model deserialization / serialization."""
import sys
import os
import pytest

# Ensure the src package is on the path when running tests directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from kb_cloud_client.kbcloud.admin.model.organization_item import OrganizationItem
from kb_cloud_client.kbcloud.admin.model.organization_list import OrganizationList


RAW_ORG_ITEM = {
    "name": "acme",
    "displayName": "ACME Corp",
    "creator": "alice",
    "creatorID": "12345",
    "clusterTotal": 3,
    "createdAt": "2025-06-01T10:00:00.000Z",
}

RAW_ORG_LIST = {
    "items": [RAW_ORG_ITEM, {**RAW_ORG_ITEM, "name": "beta"}],
}


def test_organization_item_from_dict():
    item = OrganizationItem.from_dict(RAW_ORG_ITEM)
    assert item.name == "acme"
    assert item.display_name == "ACME Corp"
    assert item.creator == "alice"
    assert item.creator_id == "12345"
    assert item.cluster_total == 3


def test_organization_item_datetime_parsed():
    from datetime import timezone
    item = OrganizationItem.from_dict(RAW_ORG_ITEM)
    assert item.created_at is not None
    assert item.created_at.tzinfo == timezone.utc
    assert item.created_at.year == 2025


def test_organization_item_from_dict_none():
    assert OrganizationItem.from_dict(None) is None


def test_organization_list_from_dict_nested():
    lst = OrganizationList.from_dict(RAW_ORG_LIST)
    assert lst.items is not None
    assert len(lst.items) == 2
    # Items should be OrganizationItem instances, not raw dicts
    assert isinstance(lst.items[0], OrganizationItem)
    assert lst.items[0].name == "acme"
    assert lst.items[1].name == "beta"


def test_organization_item_to_dict():
    item = OrganizationItem.from_dict(RAW_ORG_ITEM)
    d = item.to_dict()
    assert d["name"] == "acme"
    assert d["displayName"] == "ACME Corp"
    assert d["clusterTotal"] == 3
