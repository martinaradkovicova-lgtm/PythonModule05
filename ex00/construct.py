import sys
import os


def main() -> None:
    is_virtual_env = (sys.prefix != sys.base_prefix
                      or "VIRTUAL_ENV" in os.environ)

    if not is_virtual_env:
        print("LABORATORY STATUS: You are working in the open")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")

        print()
        print("To seal the laboratory, run:")
        print("source lab_env/bin/activate  # On Unix")
        print(r"lab_env\Scripts\activate  # On Windows")
        print()
        print("Then run this program again.")
    else:
        print("LABORATORY STATUS: The laboratory is sealed")
        print()
        print(f"Current Python: {sys.executable}")
        venv_name = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print()
        print("Reagent installation path:")
        py_version = f"python{sys.version_info.major}.{sys.version_info.minor}"
        site_packages = f"{sys.prefix}/lib/{py_version}/site-packages"
        print(site_packages)


if __name__ == "__main__":
    main()
