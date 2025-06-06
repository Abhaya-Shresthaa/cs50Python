userInput = input ("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

userInput = userInput.strip().lower()

if userInput == "42" or userInput == 'forty-two' or userInput == 'forty two':
    print("Yes")
else:
    print("No")


