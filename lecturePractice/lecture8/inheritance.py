
##this is super class
class College:
    
    def __init__(self, name):
        if not name:
            raise ValueError("Name not present")
        self.name = name
        
        
        
## use the key super to access the functions of the super class
class Student(College):
    
    def __init__(self, name, house):
        #self.name = name ## now done in college class
        super().__init__(name) ## calls init of super class
        self.house = house


class Professor(College):
    
    def __init__(self, name, subject):
        #self.name = name ##now done in college class
        super().__init__(name)
        self.house = subject
        
        
    ...