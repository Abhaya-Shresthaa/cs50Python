from plates import is_valid

def test_notInRange():
    assert is_valid("a") == False
    assert is_valid("1") == False
    assert is_valid("ads234sd") == False
    assert is_valid("asdf1234rds") == False
    
def test_puncutation():
    assert is_valid("AB123,1") == False
    assert is_valid("HE@ E") == False
    assert is_valid("a sa") == False
    
def test_numers():
    assert is_valid("AB34") == True
    assert is_valid("BCD012") == False
    assert is_valid("AB34AB") == False
    
def test_allNum():
    assert is_valid("1234") == False
    assert is_valid("0134") == False
    
def test_allChar():
    assert is_valid("ABHC") == True
    assert is_valid("asdf") == True
    
    