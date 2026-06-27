import pandas as pd
import json

def read_csv_pandas(file_path: str):
    return pd.read_csv(file_path)

def calculate_summary_pandas(df) -> dict:
    submitted = df[df["submitted"].str.lower() == "yes"]
    total_students = len(df)
    submitted_students = len(submitted)
    missing_submissions = total_students - submitted_students
    average_score = round(submitted["score"].mean(), 2)
    highest_scorer = submitted.loc[submitted["score"].idxmax(), "name"]
    lowest_scorer = submitted.loc[submitted["score"].idxmin(), "name"]
    domain_average = submitted.groupby("domain")["score"].mean().round(2).to_dict()
    students_not_submitted = df[df["submitted"].str.lower() == "no"]["name"].tolist()
    students_below_5 = submitted[submitted["score"] < 5]["name"].tolist()

    return {
        "total_students": total_students,
        "submitted_students": submitted_students,
        "missing_submissions": missing_submissions,
        "average_score": average_score,
        "highest_scorer": highest_scorer,
        "lowest_scorer": lowest_scorer,
        "domain_wise_average": domain_average,
        "students_not_submitted": students_not_submitted,
        "students_below_5": students_below_5
    }

def write_json(data: dict, output_path: str):
    with open(output_path, "w") as file:
        json.dump(data, file, indent=4)