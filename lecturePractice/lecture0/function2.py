

# #in the previous way we couldn't write the function below the function call so

# #if main function is defined then we should call the main function

# def main():
#     name = input("what is your name man?? ")
#     hello()
#     hello(name)    
    
# def hello(arguName = "World"):
#     print("Hello ", arguName)
   
   
# #if main function is made then we should always call the main function  
# main()

#for returning a value

def main():
    n = int(input("enter the value for input: "))
    print("squared value is: ", squaredValue(n))
    
def squaredValue(x):
    #return x * x
    #return x ** 3
    return pow(x,2)
   
main()