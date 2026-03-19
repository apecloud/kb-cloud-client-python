"""Example: List all available database engines and their versions (admin portal)."""

import os

from kb_cloud_client import ApiClient, Configuration
from kb_cloud_client.kbcloud.admin import EngineApi


def main():
    configuration = Configuration(
        api_key_name=os.environ.get("KB_CLOUD_API_KEY_NAME"),
        api_key_secret=os.environ.get("KB_CLOUD_API_KEY_SECRET"),
        host=os.environ.get("KB_CLOUD_SITE", "https://api.apecloud.com"),
    )

    engine_name = os.environ.get("KB_CLOUD_ENGINE")  # optional: filter by name

    with ApiClient(configuration) as api_client:
        engine_api = EngineApi(api_client)

        print(
            "Fetching all engines (admin view)"
            + (f" (filter: name={engine_name})" if engine_name else "")
            + "..."
        )

        result = engine_api.list_all_engines(name=engine_name)

        engines = result if isinstance(result, list) else getattr(result, "items", [])
        if not engines:
            print("  No engines found.")
            return

        print(f"  Total: {len(engines)} engine(s)")
        for engine in engines:
            name = getattr(engine, "name", "?")
            engine_type = getattr(engine, "type_", getattr(engine, "type", ""))
            versions = getattr(engine, "versions", []) or []
            ver_str = ", ".join(str(getattr(v, "version", v)) for v in versions[:5])
            if len(versions) > 5:
                ver_str += f" ... (+{len(versions) - 5} more)"
            print(
                f"  - {name}  type={engine_type}" + (f"  versions=[{ver_str}]" if ver_str else "")
            )


if __name__ == "__main__":
    main()
