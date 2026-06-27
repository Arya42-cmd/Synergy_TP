import matplotlib.pyplot as plt
import pandas as pd

def load_cleaned_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def plot_domain_average_score(df: pd.DataFrame, output_path: str):
    average_scores = df.groupby("domain")["score"].mean()

    plt.figure(figsize=(8, 5))
    average_scores.plot(kind="bar")

    plt.title("Average Score by Domain")
    plt.xlabel("Domain")
    plt.ylabel("Average Score")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_attendance_vs_score(df: pd.DataFrame, output_path: str):
    plt.figure(figsize=(8, 5))
    plt.scatter(
        df["attendance_percent"],
        df["score"]
    )
    plt.title("Attendance vs Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_submission_status_count(df: pd.DataFrame, output_path: str):
    submission_count = df["submitted"].value_counts()

    plt.figure(figsize=(6, 5))
    submission_count.plot(kind="bar")

    plt.title("Submission Status Count")
    plt.xlabel("Submission Status")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def write_plot_summary(output_path: str) -> None:
    summary = """
# Plot Summary

## Domain Average Score
This bar chart compares the average score of students across different domains.

## Attendance vs Score
This scatter plot shows the relationship between attendance percentage and student scores.

## Submission Status Count
This bar chart shows the number of students who submitted and did not submit their work.
"""

    with open(output_path, "w") as file:
        file.write(summary)