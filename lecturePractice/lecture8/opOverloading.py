

class People:
    
    def __init__(self, cash, bank):
        self.cash = cash
        self.bank = bank
        
    def __str__(self):
        return f"Rs.{self.cash} in hand cash and Rs.{self.bank} as bank balance"
    
    ###### overlaoding of operator
    def __add__(self,other):
        cash = self.cash + other.cash
        bank = self.bank + other.bank
        return People(cash, bank)
    
abhaya = People(1000, 2000)
print(abhaya)
shrestha = People(500, 700)
print(shrestha)
print()
## so it is overloaded
print(abhaya + shrestha)
    

