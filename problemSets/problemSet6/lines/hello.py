import sys

def main():
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            #sys.exit()