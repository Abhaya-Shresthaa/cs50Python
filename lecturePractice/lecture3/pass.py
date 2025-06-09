#to not to print anything but catching the error and not doing anything with it
def main():
    x = get_init("What's x?")
    print(f"x is {x}")
    
def get_init(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()