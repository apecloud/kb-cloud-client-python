"""Example: List all clusters in an organization (user portal)."""

import os

from kb_cloud_client import ApiClient, Configuration
from kb_cloud_client.kbcloud import ClusterApi


def main():
    configuration = Configuration(
        api_key_name=os.environ.get("KB_CLOUD_API_KEY_NAME"),
        api_key_secret=os.environ.get("KB_CLOUD_API_KEY_SECRET"),
        host=os.environ.get("KB_CLOUD_SITE", "https://api.apecloud.com"),
    )

    with ApiClient(configuration) as api_client:
        cluster_api = ClusterApi(api_client)

        org_name = os.environ.get("KB_CLOUD_ORG", "my-org")

        print(f"Listing clusters for organization: {org_name}")
        result = cluster_api.list_cluster(org_name=org_name)

        if result is None:
            print("No clusters found or response was empty.")
            return

        items = result if isinstance(result, list) else getattr(result, "items", [result])
        for cluster in items:
            if hasattr(cluster, "name"):
                print(f"  - {cluster.name} ({getattr(cluster, 'status', 'unknown')})")
            else:
                print(f"  - {cluster}")


if __name__ == "__main__":
    main()
