import sys

from visualize import (
    load_cleaned_data,
    plot_domain_average_score,
    plot_attendance_vs_score,
    plot_submission_status_count,
    write_plot_summary
)

def main():
    if len(sys.argv) != 3:
        print("Usage: python task_5/src/main.py <input_csv> <output_folder>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_folder = sys.argv[2]

    df = load_cleaned_data(input_file)

    plot_domain_average_score(
        df,
        f"{output_folder}/domain_average_score.png"
    )

    plot_attendance_vs_score(
        df,
        f"{output_folder}/attendance_vs_score.png"
    )

    plot_submission_status_count(
        df,
        f"{output_folder}/submission_status_count.png"
    )

    write_plot_summary(
        f"{output_folder}/plot_summary.md"
    )

    print("Task 5 completed successfully.")

if __name__ == "__main__":
    main()