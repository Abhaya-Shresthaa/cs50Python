from seasons import splitDateBorn,validateDate,removeAnd, calculateMin
import pytest
from datetime import date


def test_splitDateBorn():
    assert splitDateBorn('2005-05-21') == date(2005,5,21)
    assert splitDateBorn('2021-09-11') == date(2021,9,11)

def test_validateDate_exit():
    # Invalid input should trigger sys.exit
    with pytest.raises(SystemExit):
        validateDate("invalid-date")
    with pytest.raises(SystemExit):
        validateDate("2005/08/21")

def test_removeAnd():
    assert removeAnd('ten and twelve') == 'Ten twelve'
    assert removeAnd('one hundred, and twelve') == 'One hundred, twelve'


def test_calMin():
    assert calculateMin(date(2025,9,14),date(2024,9,14)) == 525600
    assert calculateMin(date(2025,9,14),date(2023,9,14)) == 1052640
    
