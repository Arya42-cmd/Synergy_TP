import json
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    "Load the CSV file into a pandas DataFrame."
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found.")
        raise
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

def generate_summary(df: pd.DataFrame) -> dict:
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "data_types": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "unique_domains": sorted(df["domain"].astype(str).unique().tolist())
    }

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=True)

def standardize_domains(df: pd.DataFrame) -> pd.DataFrame:
    domain_map = {
        "ml": "ML",
        "machine learning": "ML",
        "web": "Web",
        "web dev": "Web",
        "web development": "Web",
        "electronics": "Electronics",
        "mechanical": "Mechanical"
    }

    df["domain"] = (
        df["domain"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(domain_map)
        .fillna(df["domain"])
    )

    return df

def clean_attendance(df: pd.DataFrame) -> pd.DataFrame:
    df["attendance_percent"] = (
        df["attendance_percent"]
        .astype(str)
        .str.replace("%", "", regex=False)
    )

    df["attendance_percent"] = pd.to_numeric(
        df["attendance_percent"],
        errors="coerce"
    )

    df["attendance_percent"] = df["attendance_percent"].clip(0, 100)

    return df

def clean_scores(df: pd.DataFrame) -> pd.DataFrame:
    score_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
    }

    df["score"] = (
        df["score"]
        .astype(str)
        .str.strip()
        .str.lower()
        .replace(score_map)
    )

    df["score"] = pd.to_numeric(
        df["score"],
        errors="coerce"
    )

    return df

def clean_study_hours(df: pd.DataFrame) -> pd.DataFrame:
    hours_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
    }

    df["study_hours"] = (
        df["study_hours"]
        .astype(str)
        .str.strip()
        .str.lower()
        .replace(hours_map)
    )

    df["study_hours"] = pd.to_numeric(
        df["study_hours"],
        errors="coerce"
    )

    return df

def clean_height(df: pd.DataFrame) -> pd.DataFrame:
    df["height"] = (
        df["height"]
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "", regex=False)
    )

    def convert_height(value):
        if value.endswith("cm"):
            return float(value.replace("cm", ""))
        elif value.endswith("m"):
            return float(value.replace("m", "")) * 100
        return pd.NA

    df["height_cm"] = df["height"].apply(convert_height)
    df = df.drop(columns=["height"])

    return df

def clean_weight(df: pd.DataFrame) -> pd.DataFrame:
    df["weight"] = (
        df["weight"]
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "", regex=False)
        .str.replace("kg", "", regex=False)
    )

    df["weight_kg"] = pd.to_numeric(
        df["weight"],
        errors="coerce"
    )

    df = df.drop(columns=["weight"])

    return df

def clean_submitted(df: pd.DataFrame) -> pd.DataFrame:
    submitted_map = {
        "yes": "yes",
        "y": "yes",
        "no": "no",
        "n": "no"
    }

    df["submitted"] = (
        df["submitted"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(submitted_map)
    )

    return df

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df["attendance_percent"] = df["attendance_percent"].fillna(
        df["attendance_percent"].median()
    )

    df["score"] = df["score"].fillna(
        df["score"].median()
    )

    df["study_hours"] = df["study_hours"].fillna(
        df["study_hours"].median()
    )

    df["height_cm"] = df["height_cm"].fillna(
        df["height_cm"].median()
    )

    df["weight_kg"] = df["weight_kg"].fillna(
        df["weight_kg"].median()
    )

    return df

def validate_cleaned_data(df: pd.DataFrame) -> bool:
    valid_domains = ["ML", "Web", "Electronics", "Mechanical"]
    valid_submitted = ["yes", "no"]
    if df["student_id"].duplicated().any():
        return False
    if not df["attendance_percent"].between(0, 100).all():
        return False
    if not pd.api.types.is_numeric_dtype(df["score"]):
        return False
    if not pd.api.types.is_numeric_dtype(df["study_hours"]):
        return False
    if not pd.api.types.is_numeric_dtype(df["height_cm"]):
        return False
    if not pd.api.types.is_numeric_dtype(df["weight_kg"]):
        return False
    if not df["domain"].isin(valid_domains).all():
        return False
    if not df["submitted"].isin(valid_submitted).all():
        return False
    critical_columns = [
        "student_id",
        "name",
        "domain",
        "attendance_percent",
        "score",
        "study_hours",
        "height_cm",
        "weight_kg",
        "submitted"
        ]
    if df[critical_columns].isnull().any().any():
        return False
    return True

def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    df.to_csv(output_path, index=False)

def write_report(report_path: str) -> None:
    report = """
# Data Cleaning Report

Cleaning Steps Performed

1. Removed duplicate rows.
2. Standardized domain names.
3. Converted attendance_percent to numeric values.
4. Converted score values to numeric.
5. Converted study_hours values to numeric.
6. Converted height to centimeters.
7. Converted weight to kilograms.
8. Standardized submitted values to yes/no.
9. Filled missing numeric values using the median.
10. Validated the cleaned dataset.
"""

    with open(report_path, "w") as file:
        file.write(report)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = remove_duplicates(df)
    df = standardize_domains(df)
    df = clean_attendance(df)
    df = clean_scores(df)
    df = clean_study_hours(df)
    df = clean_height(df)
    df = clean_weight(df)
    df = clean_submitted(df)
    df = handle_missing_values(df)
    return df
