"""Example: Create a new cluster (user portal)."""

import os

from kb_cloud_client import ApiClient, Configuration
from kb_cloud_client.kbcloud import ClusterApi
from kb_cloud_client.kbcloud.model.cluster_create import ClusterCreate


def main():
    configuration = Configuration(
        api_key_name=os.environ.get("KB_CLOUD_API_KEY_NAME"),
        api_key_secret=os.environ.get("KB_CLOUD_API_KEY_SECRET"),
        host=os.environ.get("KB_CLOUD_SITE", "https://api.apecloud.com"),
    )

    org_name = os.environ.get("KB_CLOUD_ORG", "my-org")

    cluster_body = ClusterCreate(
        name="my-postgres-cluster",
        environment_name="default",
        engine="postgresql",
        version="14.0",
        termination_policy="Delete",
    )

    with ApiClient(configuration) as api_client:
        cluster_api = ClusterApi(api_client)

        print(f"Creating cluster in organization: {org_name}")
        cluster = cluster_api.create_cluster(org_name=org_name, body=cluster_body)
        print(f"Cluster created: {cluster}")


if __name__ == "__main__":
    main()
