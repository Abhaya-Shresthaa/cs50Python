
# use this to prevent NameError

try:
    x = int(input ("What's x? "))
except ValueError:
    print("x is not an integer")
#else part is only executed when there is no error in the try block 
else:
    print(f"x is {x}")