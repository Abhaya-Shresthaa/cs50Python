from random import randint

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

generate_number = randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess < 1:
        continue
    elif guess < generate_number:
        print("Too small!")
    elif guess > generate_number:
        print("Too large!")
    else:
        print("Just right!")
        break