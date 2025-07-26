import csv
import sys
import os

if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
    sys.exit(1)
else:
    try:
        students = []
        outStudents = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name":row['name'], 'house': row['house']})
               
            for student in students:
                lastName, firstName = (student['name']).rstrip().split(', ')
                outStudents.append({"first": firstName, "last": lastName, "house": student['house']})
        
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames= ['first', 'last', 'house'])
            writer.writerow({"first": 'first', 'last': 'last', 'house': 'house'})
            for outStudent in outStudents:
                writer.writerow({"first": outStudent['first'], 'last': outStudent['last'], 'house': outStudent['house']})
            
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

