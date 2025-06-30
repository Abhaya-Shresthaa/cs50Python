from hello import hello

def test_default():
    assert hello() == 'hello, world'
    
def test_argument():
    assert hello("Abhaya") == 'hello, Abhaya'
    
def test_loop():
    for name in ['Abhaya', 'Shrestha']:
        assert hello(name) == f'hello, {name}'