from calculator import square

def main():
    test_square()
    
# gives assetion error
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9 

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 sqaure was not 4")
    try:
        assert square(3) == 9 
        
    except:
        print("3 sqaure was not 9")


if __name__ == "__main__":
    main()