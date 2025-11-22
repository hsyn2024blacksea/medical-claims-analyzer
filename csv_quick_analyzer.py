import pandas as pd

def main():
    print("Medical Claims Analyzer is ready.")

    try:
        df = pd.read_csv("claims.csv")
        print("\n--- FILE LOADED ---")
        print(df.head())
        print("\nTotal rows:", len(df))
        print("Columns:", list(df.columns))

    except Exception as e:
        print("File cannot be read:", e)

if __name__ == "__main__":
    main()
