def main():
    x = int (input("enter the number you want: "))
    
    print()
    print("Using normal")
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
    print()
    print("Using pythonic expression")
    if pythonic_is_even(x):
        print("Even")
    else:
        print("Odd")
        
    print()
    print("Using normal")
    if bool_is_even(x):
        print("Even")
    else:
        print("Odd")
        

    
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False  
    
#using pythonic expression  
def pythonic_is_even(n):
    return True if n % 2 == 0 else False


#smallest way as the expression itself is a boolean expression
def bool_is_even(n):
    return n % 2 == 0 
          
main()