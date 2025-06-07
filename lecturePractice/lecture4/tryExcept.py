try:
    x = int(input("Enter the value of x: "))
    print(f"x is {x}")
except ValueError: #value error means it has different value type
    print("x is not a integer")
except SyntaxError:
    print("Syntax error")
    
    
    
# this will return NameError which means that as 
# we provide alphabet to y and there is the error in converting it to int
# the y is not assigned with anything 
# as a result y is not initialized and the name y is used
try:
    y = int(input("Enter the value of y: "))

except ValueError:  
    print("y is not a integer")
    
print(f"y is {y}")