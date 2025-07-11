from bank import value

def test_hStarting():
    assert value("hey") == 20
    assert value("hiii") == 20
    
def test_helloStarting():
    assert value("hello!") == 0
    assert value("hello! man how are you") == 0
    assert value("hello dude") == 0

def test_caseSensitivity():
    assert value("Hey") == 20
    assert value("HELlo,man") == 0
    
def test_puncuations():
    assert value("hello,man") == 0
    assert value("hey,how are you") == 20
    assert value("man, how are you") == 100 
     
def test_other():
    assert value("mann") == 100
    assert value("00 98") == 100
    assert value ("whats up") ==100
    
     