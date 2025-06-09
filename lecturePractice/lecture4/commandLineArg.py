
# in this the arguments given before running the program are stored in the in list
# sys.argv is the list that stores all the values

# in sys.argv[0] the name of the file is placed which is used by python to execute

#if we use " " and write name inside that inside part is taken in one list index
import sys

print("hello, i am", sys.argv[1])

if len(sys.argv) < 2:
    print("Too few arguments") 
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

print()
# sys.exit to again exit to the command line 
if len(sys.argv) < 2:
    sys.exit("Too few arguments") 
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])