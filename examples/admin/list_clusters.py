"""Example: List all clusters in an org with optional filters (admin portal)."""

import os

from kb_cloud_client import ApiClient, Configuration
from kb_cloud_client.kbcloud.admin import ClusterApi


def main():
    configuration = Configuration(
        api_key_name=os.environ.get("KB_CLOUD_API_KEY_NAME"),
        api_key_secret=os.environ.get("KB_CLOUD_API_KEY_SECRET"),
        host=os.environ.get("KB_CLOUD_SITE", "https://api.apecloud.com"),
    )

    org_name = os.environ.get("KB_CLOUD_ORG", "my-org")
    engine_filter = os.environ.get("KB_CLOUD_ENGINE")  # e.g. "postgresql"
    environment_name = os.environ.get("KB_CLOUD_ENV_NAME")  # e.g. "production"

    with ApiClient(configuration) as api_client:
        cluster_api = ClusterApi(api_client)

        print(
            f"Listing clusters in org '{org_name}' (admin view)"
            + (f", engine={engine_filter}" if engine_filter else "")
            + "..."
        )

        result = cluster_api.list_cluster(
            org_name=org_name,
            cluster_definition=engine_filter,
            environment_name=environment_name,
        )

        items = getattr(result, "items", None) or (result if isinstance(result, list) else [])
        if not items:
            print("  No clusters found.")
            return

        print(f"  Total: {len(items)} cluster(s)")
        for cluster in items:
            name = getattr(cluster, "name", "?")
            engine = getattr(cluster, "engine", "")
            status = getattr(cluster, "status", "")
            env = getattr(cluster, "environment_name", "")
            print(f"  - {name}  engine={engine}  env={env}  [{status}]")


if __name__ == "__main__":
    main()
