from working import convert
import pytest

def test_correct():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10 AM to 8:50 PM') == '10:00 to 20:50'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_firsPM():
    assert convert('10:30 PM to 8 AM') == '22:30 to 08:00'
    assert convert('5:30 PM to 10 AM') == '17:30 to 10:00'
    assert convert('10:30 PM to 8 PM') == '22:30 to 20:00'
    
    
def test_valueError():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    