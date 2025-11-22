import pandas as pd
import os
import sys


def get_data_path(filename: str) -> str:
    """
    Returns the full path to a data file (works both for .py and .exe).
    """
    # If running as a PyInstaller EXE
    if getattr(sys, "frozen", False):
        base_dir = os.path.dirname(sys.executable)
    else:
        # Running as a normal Python script
        base_dir = os.path.dirname(__file__)
    return os.path.join(base_dir, filename)


def main():
    print("Medical Claims Analyzer is ready.")

    # Find claims.csv next to the script / exe
    csv_path = get_data_path("claims.csv")
    print(f"\nLooking for file: {csv_path}")

    try:
        df = pd.read_csv(csv_path)

        print("\n--- FILE LOADED ---")
        print(df.head())          # show first 5 rows
        print("\nTotal rows:", len(df))
        print("Columns:", list(df.columns))

        # Small extra analysis (optional)
        if "claim_amount" in df.columns:
            print("\n--- Claim Amount Summary ---")
            print("Average claim amount:", df["claim_amount"].mean())
            print("Min claim amount:", df["claim_amount"].min())
            print("Max claim amount:", df["claim_amount"].max())

    except Exception as e:
        print("\nFile cannot be read:", e)

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
