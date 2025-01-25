import pandas as pd

def load_csv(file_path):
    try:
        # Load CSV into a DataFrame
        df = pd.read_csv(file_path)
        print("CSV loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def print_records(df):
    print("\nPrinting each record:")
    for index, row in df.iterrows():
        print(f"Record {index + 1}: {row.to_dict()}")

def count_records(df):
    count = len(df)
    print(f"\nNumber of records: {count}")
    return count

def reverse_and_save(df, output_file):
    # Reverse the order of the DataFrame
    reversed_df = df.iloc[::-1]
    reversed_df.to_csv(output_file, index=False)
    print(f"\nReversed records saved to '{output_file}'.")

def main():
    file_path = "data.csv"  # Replace with your CSV file path
    output_file = "reversed_data.csv"  # File to save reversed data

    df = load_csv(file_path)
    if df is not None:
        print_records(df)
        count_records(df)
        reverse_and_save(df, output_file)

if __name__ == "__main__":
    main()
