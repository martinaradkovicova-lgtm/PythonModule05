import sys
import importlib


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")

    reagents = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready"
    }

    missing = False

    for reagent, description in reagents.items():
        try:
            mod = importlib.import_module(reagent)
            try:
                version = mod.__version__
            except AttributeError:
                version = "unknown"
            print(f"[OK] {reagent} ({version}) - {description}")
        except ImportError:
            print(f"[ERROR] {reagent} is missing.")
            missing = True

    if missing:
        print("\nSome reagents are missing!")
        print("To install them, you can use one of the following methods:")
        print("  - Using pip:   pip install -r ex0/requirements.txt")
        print("  - Using Poetry: poetry install (or poetry add numpy pandas)")
        sys.exit(1)

    print("\npip vs Poetry:")
    print("\trequirements.txt declares what to install; "
          "pip resolves it at install time.")
    print("\tpyproject.toml declares the same constraints, and Poetry "
          "pins the resolved\n\tversions"
          " in poetry.lock so every install is identical.")
    print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
