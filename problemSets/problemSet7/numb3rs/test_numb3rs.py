from numb3rs import validate
import pytest

def test_allsame():
    assert validate('0.0.0.0') == True
    assert validate('1.2.3.4') == True
    assert validate('255.255.255.255') == True
    
def test_outRange():
    assert validate('266.1.4.5') == False
    assert validate('275.275.4.5') == False
    assert validate('266.1.4.5.6') == False
    assert validate('cat') == False
    assert validate('234.234.267.5') == False
    