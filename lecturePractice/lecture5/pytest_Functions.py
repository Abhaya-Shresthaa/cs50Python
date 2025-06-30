from calculator import square

def main():
    test_positive()
    
#pytest calls and check all the function even if not called in main()
def test_positive():
    assert square(2) == 4
    assert square(3) == 9 
    
def test_negative():
    assert square(-2) == 4 
    assert square(-3) == 9 
    
def test_zero():
    assert square(0) == 0 
    


if __name__ == "__main__":
    main()