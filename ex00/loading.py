import sys
import importlib

def main() -> None:
    reagents = ["numpy", "pandas"]
    
    for reagent in reagents:
        try:
            importlib.import_module(reagent)
            print(f"SUCCESS: {reagent} loaded successfully.")
        except ImportError as ERROR:
            print(f"ERROR: Failed to load {reagent}: {ERROR}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
