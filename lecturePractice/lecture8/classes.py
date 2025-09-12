
class Student:
    # ... #using ... is like using pass to do nothing to remove the syntax error
    def __init__(self, name, house): # it is like constructor
        #self defines that these values are to be stored in the current object
        
        if not name:
            raise ValueError("Name is empty")
        
        if house not in ['blue', 'green', 'red', 'yellow']:
            raise ValueError("Invalid House")
        
        self.name = name
        self.house = house
    
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    # student = Student()
    # student.name = input("enter name: ")
    # student.house = input("enter house: ")
    name = input("name: ")
    house = input("house: ")
    try:
        return Student(name, house)
    except ValueError:
        ...
        

main()