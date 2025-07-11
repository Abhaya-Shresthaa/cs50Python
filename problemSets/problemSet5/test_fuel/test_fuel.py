from fuel import convert, gauge
import pytest


def test_convert():
    assert convert('3/4') == 75
    assert convert('5/6') == 83

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(45) == "45%"
    
def test_convertError():
    with pytest.raises(ValueError):
        convert('4/3')
    with pytest.raises(ValueError):
        convert('6/3')
    with pytest.raises(ZeroDivisionError):
        convert('2/0')
    with pytest.raises(ZeroDivisionError):
        convert('3/0')
    with pytest.raises(ValueError):
        convert('-1/3')
        