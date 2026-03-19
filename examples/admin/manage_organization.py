"""Example: Create, read, and delete an organization (admin portal)."""
import os
import sys

from kb_cloud_client import ApiClient, Configuration, ApiException
from kb_cloud_client.kbcloud.admin import OrganizationApi
from kb_cloud_client.kbcloud.admin.model.org_create import OrgCreate


def main():
    configuration = Configuration(
        api_key_name=os.environ.get("KB_CLOUD_API_KEY_NAME"),
        api_key_secret=os.environ.get("KB_CLOUD_API_KEY_SECRET"),
        host=os.environ.get("KB_CLOUD_SITE", "https://api.apecloud.com"),
    )

    org_name = os.environ.get("NEW_ORG_NAME", "example-org")

    with ApiClient(configuration) as api_client:
        org_api = OrganizationApi(api_client)

        # Create organization
        print(f"Creating organization '{org_name}'...")
        try:
            body = OrgCreate(
                name=org_name,
                display_name="Example Organization",
                description="Created via kb-cloud-client-python",
            )
            org = org_api.create_org(body=body)
            print(f"  Created: {getattr(org, 'name', org)}")
        except ApiException as e:
            print(f"  Failed to create org: {e}")
            sys.exit(1)

        # Read organization
        print(f"\nReading organization '{org_name}'...")
        try:
            org = org_api.read_org(org_name=org_name)
            print(f"  Name        : {getattr(org, 'name', '?')}")
            print(f"  DisplayName : {getattr(org, 'display_name', '?')}")
            print(f"  Description : {getattr(org, 'description', '?')}")
        except ApiException as e:
            print(f"  Failed to read org: {e}")

        # Delete organization
        print(f"\nDeleting organization '{org_name}'...")
        try:
            org_api.delete_org(org_name=org_name)
            print("  Deleted successfully.")
        except ApiException as e:
            print(f"  Failed to delete org: {e}")


if __name__ == "__main__":
    main()
