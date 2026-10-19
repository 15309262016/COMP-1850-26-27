# Worksheet 1.3: Task 3

import csv

input_file_name = input()

with open(input_file_name, newline="", encoding="utf-8") as input_file:
	reader = csv.reader(input_file)
	next(reader, None)

	results = []
	for row in reader:
		if not row:
			continue

		student_id = row[0]
		grades = [int(grade) for grade in row[1:] if grade.strip()]
		average_grade = sum(grades) / len(grades)

		if average_grade >= 70:
			classification = "1"
		elif average_grade >= 60:
			classification = "2:1"
		elif average_grade >= 50:
			classification = "2:2"
		elif average_grade >= 40:
			classification = "3"
		else:
			classification = "F"

		results.append((student_id, f"{average_grade:.2f}", classification))

output_file_name = input_file_name + "_out.csv"
with open(output_file_name, "w", newline="", encoding="utf-8") as output_file:
	writer = csv.writer(output_file, lineterminator="\n")
	writer.writerows(results)