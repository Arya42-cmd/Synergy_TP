import json
import sys

from clean_data import (
    load_data,
    generate_summary,
    clean_data,
    validate_cleaned_data,
    save_cleaned_data,
    write_report
)

def main():
    if len(sys.argv) != 3:
        print("Usage: python task_4/src/main.py <input_csv> <output_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    df = load_data(input_file)

    summary_before = generate_summary(df)
    with open("task_4/output/summary_before.json", "w") as file:
        json.dump(summary_before, file, indent=4)

    df = clean_data(df)

    if not validate_cleaned_data(df):
        print("Validation failed.")
        sys.exit(1)

    summary_after = generate_summary(df)
    with open("task_4/output/summary_after.json", "w") as file:
        json.dump(summary_after, file, indent=4)

    save_cleaned_data(df, output_file)

    write_report("task_4/output/cleaning_report.md")

    print("Task 4 completed successfully.")

if __name__ == "__main__":
    main()