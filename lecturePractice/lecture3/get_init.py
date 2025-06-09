def main():
    x = get_init()
    print(f"x is {x}")
    
def get_init():
    while True:
        try:
            x = int(input("what's x?")) #we can also put the return value directly here
        except ValueError:
            print("that's not an integer try again:)")
        else:
            return x  # return directly breaks the loop  and enters 

main()