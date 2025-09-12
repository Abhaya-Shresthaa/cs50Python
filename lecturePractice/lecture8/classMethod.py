

class Name:
    
    def __init__(self, name, house):
        self.name = name  
        self.house = house  
    
    def __str__(self):
        return f"{self.name} is in {self.house}"
        
        
    ## directly access the function without making its instance i.e object
    ## give reference to the class itself
    @classmethod
    def sort(cls, name):
        ...
      
    ##by using this we can call the get_student without making the oblject of the Name class initially  
    @classmethod
    def get_student(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
        
        
#Name.sort("Shrestha")
student = Name.get_student()
print (student)