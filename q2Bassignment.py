import csv

grade_to_points = {'AP': 10, 'AA': 10, 'AB': 9, 'BB': 8, 'BC': 7, 'CC': 6}

file_path = "C:\\Users\\dircr\\Downloads\\student_records.csv"
students = {}

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        roll_number = row['roll_number']
        credit = int(row['credit'])
        grade = row['grade']


        grade_points = grade_to_points.get(grade, 0)

        if roll_number not in students:
            students[roll_number] = {'total_credits': 0, 'weighted_sum': 0}


        students[roll_number]['total_credits'] += credit
        students[roll_number]['weighted_sum'] += grade_points * credit

results = []
for roll_number, data in students.items():
    total_credits = data['total_credits']
    weighted_sum = data['weighted_sum']
    cpi = weighted_sum / total_credits if total_credits > 0 else 0
    results.append({'roll_number': roll_number, 'total_credits': total_credits, 'CPI': round(cpi, 2)})

for result in results:
    print(f"Roll Number: {result['roll_number']}, Total Credits: {result['total_credits']}, CPI: {result['CPI']}")





