"""Example: List all environments, optionally filtered by org or cloud provider (admin portal)."""
import os

from kb_cloud_client import ApiClient, Configuration
from kb_cloud_client.kbcloud.admin import EnvironmentApi


def main():
    configuration = Configuration(
        api_key_name=os.environ.get("KB_CLOUD_API_KEY_NAME"),
        api_key_secret=os.environ.get("KB_CLOUD_API_KEY_SECRET"),
        host=os.environ.get("KB_CLOUD_SITE", "https://api.apecloud.com"),
    )

    org_name = os.environ.get("KB_CLOUD_ORG")
    cloud_provider = os.environ.get("KB_CLOUD_PROVIDER")  # e.g. "aws", "aliyun"

    with ApiClient(configuration) as api_client:
        env_api = EnvironmentApi(api_client)

        print("Fetching environments" +
              (f" for org '{org_name}'" if org_name else "") +
              (f" on provider '{cloud_provider}'" if cloud_provider else "") + "...")

        result = env_api.list_environment(
            org_name=org_name,
            cloud_provider=cloud_provider,
        )

        items = getattr(result, "items", None) or (result if isinstance(result, list) else [])
        if not items:
            print("  No environments found.")
            return

        print(f"  Total: {len(items)} environment(s)")
        for env in items:
            name = getattr(env, "name", "?")
            env_type = getattr(env, "environment_type", "")
            provider = getattr(env, "cloud_provider", "")
            region = getattr(env, "cloud_region", "")
            status = getattr(env, "status", "")
            print(f"  - {name}  type={env_type}  {provider}/{region}  [{status}]")


if __name__ == "__main__":
    main()
