import sys
from manual_parser import read_csv_manual, convert_types, calculate_summary, write_json as write_manual_json
from pandas_parser import read_csv_pandas, calculate_summary_pandas, write_json as write_pandas_json

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <input_csv> <output_manual_json> <output_pandas_json>")
        return

    input_csv = sys.argv[1]
    output_manual = sys.argv[2]
    output_pandas = sys.argv[3]

    rows = read_csv_manual(input_csv)
    rows = convert_types(rows)
    manual_summary = calculate_summary(rows)
    write_manual_json(manual_summary, output_manual)

    df = read_csv_pandas(input_csv)
    pandas_summary = calculate_summary_pandas(df)
    write_pandas_json(pandas_summary, output_pandas)

    print("Manual summary written to:", output_manual)
    print("Pandas summary written to:", output_pandas)

if __name__ == "__main__":
    main()