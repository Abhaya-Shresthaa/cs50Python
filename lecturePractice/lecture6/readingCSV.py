# with open("student.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is {row[1]}")
        # firstPart, secondPart = line.rstrip().split(",")
        # print(f"{firstPart} is {secondPart}")
        
# # sorting
# students = []
# with open("student.csv") as file:
#     for line in file:
#         firstN, secondN = line.rstrip().split(",")
#         students.append(f"{firstN} and {secondN}")
        
# for student in sorted(students):
#     print(student)

# sorting using dictionary keys

students = []
with open("student.csv") as file:
    for line in file:
        name, caste = line.rstrip().split(",")
        # student = {}
        # student["name"] = name
        # student["caste"] = caste
        # in single line
        student = {"name" : name , "caste" : caste}
        students.append(student)
        
for student in students:
    print(f"{student['name']} is {student['caste']}")
        