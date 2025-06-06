def main():
    # while True: 
    #     print("hello")
    totalAmount = 50
    while True: 
        print("Amount Due:", totalAmount)
        n = int(input("Insert Coin: "))
        totalAmount = validate(totalAmount, n)
        if totalAmount <= 0:
            print("Change Owed:", abs(totalAmount))
            break
        else:
            continue
        
def validate(amount_due, input):
    if input == 5 or input == 10 or input == 25:
        amount_due = amount_due - input
        return amount_due
    else:
        return amount_due
main()