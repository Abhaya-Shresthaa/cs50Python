while True:
    try:
        x = int(input("what's x?"))
    except:
        print("that's not an integer try again:)")
    else:
        print(f"your integer is {x}")
        break

#we can print here as well
print(f"Outside part your integer is {x}")



# 2
while True:
    try:
        x = int(input("what's x?"))
        print(f"your integer is {x}")
        break
    except:
        print("that's not an integer try again:)")