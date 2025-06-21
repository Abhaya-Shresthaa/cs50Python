from calculator import square

def main():
    testing_sqaure()

def testing_sqaure():
    if square(2) != 4:
        print("2 sqaure is not 4")
    if square(3) != 9:
        print("3 sqaure is not 9")
        
if __name__ == "__main__":
    main()