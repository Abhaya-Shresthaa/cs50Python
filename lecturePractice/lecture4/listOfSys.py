import sys

if len(sys.argv) < 2:
    sys.exit("very less arguments")

# in this list the syss.argv[0] has the name of the argumnet which will produce error
for arg in sys.argv:
    print("My name is", arg)
    
#slicing the element i.e removing the part 

for arg in sys.argv[1:]:  # [:-1] for removing from last
    print("My name is ", arg)
    
#PyPi python package index to see the external packages
# pip is the package manager of the python that installs packages in python