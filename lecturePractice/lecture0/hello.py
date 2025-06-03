# name = input("Hello What is your name? ")

name = "Abhaya"

# in print(*object ,  sep = '' , end = '\n')
#parameters already present bypass it

print(name)
print("hello" + name)
print("hello", name)
#put question mark in place of space 
print("hello", name, sep='??')
print("in the same line",  end = '' )
print(name)
#using a space in end
print("in the same line with space",  end = ' ' )
print(name)

#write other things
print("in the same line with other",  end = '???' )
print(name)
print()
print()
print()
#if we want to print actual quote
#use different quote in and out
print(" hello , 'friend' ")
print(' hello , "friend"')

print()

# f string in a easier way
print(f"hello {name}")

#remove white spaces in the front and last
spaceName = '   hello Man'
noSpace = spaceName.strip()
print(noSpace)

# capitalize first letter and small other letters
makeCapital = spaceName.capitalize()
print(makeCapital)

#capitalize first letter of every word
makeEachCapital = spaceName.title()
print(makeEachCapital)

#do on the same line
managed = spaceName.strip().title()
print(managed)

#use on the same line of the input as well
# name = input("Hello What is your name? ").strip().title()

# splitting the name
myName = 'Abhaya Shrestha'
firstName , lastName = myName.split(" ")
print(firstName)
print(lastName)