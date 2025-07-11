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
        
  #using key      
# def get_name(student):
#     return student["name"]

# for student in sorted(students, key   = get_name):
#     print(f"{student['name']} is {student['caste']}")

#using lambda 
#using lambda is like the above but it is like a anonymous function 
# thats name is student and return the student name
for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is {student['caste']}")
