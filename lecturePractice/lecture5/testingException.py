import pytest
from calculator import square

def main():
    test_positive()
    
def test_positive():
    assert square(2) == 4
    assert square(3) == 9 
    
def test_string():
    with pytest.raises(TypeError):
        square("hello")
    


if __name__ == "__main__":
    main()