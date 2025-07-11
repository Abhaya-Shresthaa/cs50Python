name = input("What's your name? ")

# file = open ("name.txt", "w") # w to write in file
# #write opens and recreate the file as new one
# file.write(name)
# file.close()

# so use append
file = open ("name.txt", "a")  # a for append
file.write(f"{name}\n") # f string and /n for changing the line
file.close()

#without using f.close directly closing the file later on
with open ("name.txt", "a") as file1: 
    file1.write(f"{name}\n") 
