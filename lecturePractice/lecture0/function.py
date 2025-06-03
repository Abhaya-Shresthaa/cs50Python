def hello():
    print("Hello ")
    
#using a parameterized function
def paraHello(arguName):
    print("Hello ", arguName)
    
#default argument
def defaultHello(arguName = "World"):
    print("Hello ", arguName)
    
name = input("what is your name man?? ")
hello()
print(name)

print()
paraHello(name)

print()
defaultHello()
defaultHello(name)




