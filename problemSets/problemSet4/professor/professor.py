from random import randint

def main():
    score = 0
    level = get_level()
    
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for i in range(3):
            userAns = int(input(f"{x} + {y} = "))
            if(userAns == (x+y)):
                score = score +1
                break
            elif i == 2:
                print("EEE")
                print(f"{x} + {y} = {x+y}")
            else:
                print("EEE")
    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                break
        except ValueError:
            pass
    return level


def generate_integer(level):
    #return randint((10**(level-1)),((10**level)-1))
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10, 99)
    else:
        return randint(100, 999)

if __name__ == "__main__":
    main()
            