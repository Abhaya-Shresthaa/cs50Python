from twttr import shorten

def test_small():
    assert shorten("abhaya") == "bhy"
    assert shorten('hello') == "hll"
    
def test_cap():
    assert shorten("Abhaya") == "bhy"
    assert shorten("ABHAYA") == "BHY"
    assert shorten("HELLO") == "HLL"
    
def test_num():
    assert shorten("080BCT006") == "080BCT006"
    assert shorten("080BEI006") == "080B006"
    assert shorten("080BEL006") == "080BL006"
   
def test_puncuation():
    assert shorten("hello,man") == "hll,mn" 
    assert shorten("hey,how are you") == "hy,hw r y"  
    
    
    