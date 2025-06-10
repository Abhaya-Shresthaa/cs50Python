import sys

from tempLibrary import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
    
    

    
# if __name__ == "__main__":
#     main()

#this is used to clal the main function only when the file is executed through command line
#checks if the file is imported or not and doesn't runs when the file is imported from other