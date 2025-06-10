
lst = []

while True:
    try:
        userInput = input()
        lst.append(userInput)
    except EOFError:
        break

      
if len(lst) == 1:
    print(f"Adieu, adieu, to ", end= "")
    print(f"{lst[0]}")
elif len(lst) == 2:
    print(f"Adieu, adieu, to {lst[0]} and {lst[1]}")
    
else:
    print(f"Adieu, adieu, to ", end= "")
    for i in range(len(lst)):
        if i == len(lst) - 2:
            print(f"{lst[i]}", end=", and ")
        elif i == len(lst) - 1:
            print(f"{lst[i]}")
        else:
            print(f"{lst[i]}", end=", ")