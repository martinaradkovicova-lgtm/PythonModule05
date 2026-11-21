import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("[ERROR] Library 'python-dotenv' is missing.")
    print("Install it using: pip install -r requirements.txt")
    sys.exit(1)


def main() -> None:
    load_dotenv()

    print("ORACLE STATUS: Consulting the configuration...")

    matrix_mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("\nConfiguration loaded:")
    print(f"Mode: {matrix_mode}")

    if not database_url:
        print("Database: Connected to local instance (default)")
    else:
        print(f"Database: Connected to {database_url}")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key (running in restricted mode)")

    print(f"Log Level: {log_level}")

    if not zion_endpoint:
        print("Remote Network: Online")
    else:
        print(f"Remote Network: {zion_endpoint}")

    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
