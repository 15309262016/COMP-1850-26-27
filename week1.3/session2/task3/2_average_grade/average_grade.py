# Week 1.3, Session 2: Calculate Average Grade and Write to a File

import csv
from pathlib import Path

csv_file = Path(__file__).with_name("student_data.csv")
report_file = Path(__file__).with_name("report.txt")

with csv_file.open("r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    data = list(reader)

with report_file.open("w", encoding="utf-8") as report:
    for row in data[1:]:
        student_id, name, maths, science, history = row

        maths = int(maths)
        science = int(science)
        history = int(history)

        average = (maths + science + history) / 3
        report.write(f"{name}: {average:.2f}\n")

print(f"Report saved to {report_file.name}.")
