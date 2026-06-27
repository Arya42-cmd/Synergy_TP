## Task 3: Manual CSV Parsing vs Pandas

## Objective

The objective of this task was to compare processing a CSV file manually using Python with processing the same file using the pandas library.

## Manual Parsing

- Read the CSV file line by line.
- Split each line using commas.
- Converted data types manually.
- Calculated statistics using loops and dictionaries.
- Wrote the summary to a JSON file.

## Pandas Parsing

- Loaded the CSV using `pd.read_csv()`.
- Used built-in DataFrame operations.
- Calculated statistics using pandas functions.
- Wrote the summary to a JSON file.

## Comparison

| Feature | Manual Parsing | Pandas |
|---------|----------------|---------|
| Code Length | Longer | Shorter |
| Ease of Implementation | More Complex | Simpler |
| Readability | Moderate | High |
| Performance | Slower | Faster |
| Scalability | Limited | Excellent |

## Conclusion

Both implementations produced identical results. Manual parsing provides a better understanding of file handling and data processing, while pandas offers a cleaner, faster, and more efficient solution for working with structured data.