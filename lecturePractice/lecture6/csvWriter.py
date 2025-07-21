import csv

name = input("name: ")
home = input("home: ")

with open ("anoStudents.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames= ["name", "home"]) # this give how the inputs are kept
    writer.writerow({"name": name,"home": home}) 