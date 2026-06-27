# Task 3: Manual CSV Parser vs Pandas

## Description

This project compares processing CSV data manually using core Python with processing the same data using the pandas library.

## Folder Structure

```
task_3/
│
├── data/
│   └── submissions.csv
│
├── output/
│   ├── manual_summary.json
│   └── pandas_summary.json
│
├── src/
│   ├── manual_parser.py
│   ├── pandas_parser.py
│   └── main.py
│
├── comparison_report.md
├── README.md
└── requirements.txt
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Run

```bash
python task_3/src/main.py task_3/data/submissions.csv task_3/output/manual_summary.json task_3/output/pandas_summary.json
```

## Output

- manual_summary.json
- pandas_summary.json

Both output files contain identical summaries generated using different approaches.