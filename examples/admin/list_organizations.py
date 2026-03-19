"""Example: List all organizations on the platform (admin portal)."""

import os

from kb_cloud_client import ApiClient, Configuration
from kb_cloud_client.kbcloud.admin import OrganizationApi


def main():
    configuration = Configuration(
        api_key_name=os.environ.get("KB_CLOUD_API_KEY_NAME"),
        api_key_secret=os.environ.get("KB_CLOUD_API_KEY_SECRET"),
        host=os.environ.get("KB_CLOUD_SITE", "https://api.apecloud.com"),
    )

    with ApiClient(configuration) as api_client:
        org_api = OrganizationApi(api_client)

        print("Fetching all organizations (admin view)...")
        result = org_api.list_organizations()

        items = getattr(result, "items", None) or (result if isinstance(result, list) else [])
        if not items:
            print("  No organizations found.")
            return

        print(f"  Total: {len(items)} organization(s)")
        for org in items:
            name = getattr(org, "name", "?")
            display_name = getattr(org, "display_name", "")
            status = getattr(org, "status", "")
            print(
                f"  - {name}"
                + (f" ({display_name})" if display_name else "")
                + (f"  [{status}]" if status else "")
            )


if __name__ == "__main__":
    main()
