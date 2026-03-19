"""Example: List all organizations (user portal)."""

import os

from kb_cloud_client import ApiClient, Configuration
from kb_cloud_client.kbcloud import OrganizationApi


def main():
    configuration = Configuration(
        api_key_name=os.environ.get("KB_CLOUD_API_KEY_NAME"),
        api_key_secret=os.environ.get("KB_CLOUD_API_KEY_SECRET"),
        host=os.environ.get("KB_CLOUD_SITE", "https://api.apecloud.com"),
    )

    with ApiClient(configuration) as api_client:
        org_api = OrganizationApi(api_client)

        print("Listing organizations...")
        result = org_api.list_org()

        items = result if isinstance(result, list) else getattr(result, "items", [result])
        for org in items:
            name = getattr(org, "name", org)
            display_name = getattr(org, "display_name", "")
            print(f"  - {name}" + (f" ({display_name})" if display_name else ""))


if __name__ == "__main__":
    main()
