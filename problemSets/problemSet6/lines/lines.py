import sys

def main():
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
        if len(sys.argv) > 2:
            print("Too many command-line arguments")
        sys.exit(1)
    else:
        if not sys.argv[1].endswith('.py'):
            print("Not a Python file ")
            sys.exit(1)
        else:
            try:
                with open(sys.argv[1], 'r') as file:
                    count = 0
                    for line in file:
                        if not line.lstrip().startswith('#') and line.lstrip() != '':
                            count += 1
                print(count)
                        
            except FileNotFoundError:
                print("File does not exist ")
                sys.exit(1)
    
if __name__ == '__main__':
    main()