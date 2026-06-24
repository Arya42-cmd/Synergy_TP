import csv
import json
import os
from typing import List, Dict


def read_submissions(file_path: str) -> List[Dict]:
    submissions = []

    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    row["score"] = int(row["score"])
                    submissions.append(row)
                except ValueError:
                    print(f"Invalid score for {row['name']}")

    except FileNotFoundError:
        print("Input file not found.")

    return submissions


def get_submitted_students(data: List[Dict]) -> List[Dict]:
    return [student for student in data if student["submitted"].lower() == "yes"]


def calculate_average_score(data: List[Dict]) -> float:
    submitted = get_submitted_students(data)

    if not submitted:
        return 0.0

    total = sum(student["score"] for student in submitted)
    return round(total / len(submitted), 2)


def get_domain_wise_average(data: List[Dict]) -> Dict:
    domain_scores = {}

    for student in get_submitted_students(data):
        domain = student["domain"]

        if domain not in domain_scores:
            domain_scores[domain] = []

        domain_scores[domain].append(student["score"])

    averages = {}

    for domain, scores in domain_scores.items():
        averages[domain] = round(sum(scores) / len(scores), 2)

    return averages


def get_missing_submissions(data: List[Dict]) -> List[str]:
    return [
        student["name"]
        for student in data
        if student["submitted"].lower() == "no"
    ]


def write_summary(summary: Dict, output_file: str) -> None:
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as file:
        json.dump(summary, file, indent=4)