def main():
    name = input("Enter name: ")
    print(hello(name))
    
def hello(to= "world"):
    return f"hello, {to}" #using return value to test our function