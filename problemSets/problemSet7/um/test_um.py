from um import count
import pytest 

def test_initialUm():
    assert count('um') == 1
    assert count('um, hello') == 1
    assert count('um! hi') == 1
    
def test_inMiddle():
    assert count('hello, um, world') == 1
    assert count('hi, um! thats great') == 1

def test_inWords():
    assert count('yummy') == 0
    assert count('um thats yummy') == 1

def test_moreThanOne():
    assert count('um thats great um') == 2

def test_case():
    assert count('Um thats great UM') == 2
    