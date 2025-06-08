while True: 
    try:
        userInput= input("Fraction: ")
        x, y = userInput.split('/')
        x = int(x)
        y = int(y)
        percentage = int((x/y)*100)
        if x > y:
            continue
    except (ValueError, ZeroDivisionError):
        pass
        
    else:
        break
    
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")

