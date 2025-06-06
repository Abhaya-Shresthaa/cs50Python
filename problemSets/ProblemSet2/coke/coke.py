def main():
    # while True: 
    #     print("hello")
    n = int(input("Enter"))
    validate(n)
def validate(input):
    if input == 5 or input == 10 or input == 25:
        amount_due = amount_due - input
        print("Amount Due: ", amount_due)
    else:
        print("Amount Due: ", amount_due)

    
    
main()