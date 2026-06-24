import sys
from analyzer import (
    read_submissions,
    get_submitted_students,
    calculate_average_score,
    get_domain_wise_average,
    get_missing_submissions,
    write_summary,
)


def main():
    if len(sys.argv) != 3:
        print("Usage:")
        print(
            "python task_2/src/main.py input.csv output.json"
        )
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = read_submissions(input_file)

    if not data:
        print("No data found.")
        return

    submitted_students = get_submitted_students(data)

    total_students = len(data)
    submitted_count = len(submitted_students)
    missing_count = total_students - submitted_count

    average_score = calculate_average_score(data)

    highest_scorer = max(
        submitted_students,
        key=lambda x: x["score"]
    )["name"]

    lowest_scorer = min(
        submitted_students,
        key=lambda x: x["score"]
    )["name"]

    missing_submissions = get_missing_submissions(data)

    below_five = [
        student["name"]
        for student in submitted_students
        if student["score"] < 5
    ]

    summary = {
        "total_students": total_students,
        "submitted_students": submitted_count,
        "missing_submissions": missing_count,
        "average_score": average_score,
        "highest_scorer": highest_scorer,
        "lowest_scorer": lowest_scorer,
        "domain_wise_average":
            get_domain_wise_average(data),
        "students_not_submitted":
            missing_submissions,
        "students_below_5":
            below_five,
    }

    write_summary(summary, output_file)

    print(f"Total Students: {total_students}")
    print(f"Submitted: {submitted_count}")
    print(f"Missing: {missing_count}")
    print(f"Average Score: {average_score}")
    print(f"Highest Scorer: {highest_scorer}")
    print(f"Missing Submissions: {missing_submissions}")
    print(
        f"Summary written to {output_file}"
    )


if __name__ == "__main__":
    main()