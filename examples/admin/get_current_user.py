"""Example: Get the currently authenticated user's information (admin portal)."""
import os

from kb_cloud_client import ApiClient, Configuration
from kb_cloud_client.kbcloud.admin import UserApi


def main():
    configuration = Configuration(
        api_key_name=os.environ.get("KB_CLOUD_API_KEY_NAME"),
        api_key_secret=os.environ.get("KB_CLOUD_API_KEY_SECRET"),
        host=os.environ.get("KB_CLOUD_SITE", "https://api.apecloud.com"),
    )

    with ApiClient(configuration) as api_client:
        user_api = UserApi(api_client)

        print("Fetching current authenticated user...")
        user = user_api.get_authenticated_user()

        if user is None:
            print("  Could not retrieve user info.")
            return

        print(f"  Username     : {getattr(user, 'user_name', '?')}")
        print(f"  Display Name : {getattr(user, 'display_name', '?')}")
        print(f"  Email        : {getattr(user, 'email', '?')}")
        print(f"  Phone        : {getattr(user, 'phone_number', '?')}")
        print(f"  Created At   : {getattr(user, 'created_at', '?')}")


if __name__ == "__main__":
    main()
