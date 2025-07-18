import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    # for row in reader:
    #     students.append({"name" : row[0], "caste": row[1]}) 
    for name, caste in reader:
        students.append({"name" : name, "caste": caste})
        
for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is {student['caste']}")
    