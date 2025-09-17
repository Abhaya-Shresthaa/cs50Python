import pytest
from jar import Jar 

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar1 = Jar(-12)
    with pytest.raises(TypeError):
        jar2 = Jar('Hello')
    
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    
def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(13)
    
def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)
    jar.deposit(5)
    jar.withdraw(6)
    assert jar.size == 1
    