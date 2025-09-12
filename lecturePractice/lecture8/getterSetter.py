

## in python we don't have actual private protected in class 
## we use naming convention by
## __ double underscore for private
## _  single underscore for protected

class Student:
    
    def __init__(self, name, house): # it is like constructor
        self.name = name
        ##here _house is not used because this calls the setter function and goes through checks
        self.house = house 

      
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    ## getter  call this function and get the value
    @property ## syntax for stating a getter
    def house(self):
        return self._house ##using _house for preventing naming collision
    
    ## setter  pass some value and set that value in this
    @house.setter ## syntax for stating a setter
    def house(self, house):
        if house not in ["yellow", "green", "red", "blue"]:
            raise ValueError("Invalid house")
        self._house = house
    
        
    
def main():
    student = get_student()
    try:
        student.house = "Hello" ## this gives the value error if not try
    except:
        pass
    
    student.house = "green"
    print(student)
    
def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)
    

main()