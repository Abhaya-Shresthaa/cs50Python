

class Student:
    
    def __init__(self, name, house): # it is like constructor
        self.name = name
        self.house = house
    
    ##########
    #just directly print the class it will make it the way we want to
      
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    ## our made function
    def charm(self):
        return "Inside Charm"
    
    def i_made(self):
        return "I_MADE"
        
    
def main():
    student = get_student()
    print(student)
    print(student.charm())
    print(student.i_made())
    


def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)
    

main()