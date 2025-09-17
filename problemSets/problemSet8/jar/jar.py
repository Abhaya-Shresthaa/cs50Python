

class Jar:
    
    def __init__(self, capacity = 12):
        if not capacity >= 0:
            raise ValueError 
        self._capacity = capacity
        self._numPresent = 0
        
    def __str__(self):
        return "🍪" * self._numPresent
    
    def deposit(self, n):
        if (self._numPresent + n) > self._capacity:
            raise ValueError
        else:
            self._numPresent += n
            
    def withdraw(self, n):
        if (self._numPresent - n )< 0:
            raise ValueError
        else:
            self._numPresent -= n
            
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._numPresent
    
def main():
    jar = Jar(14)
    print(jar.capacity)
    jar.deposit(3)
    print(jar.size)
    print(jar)
    
    
    
if __name__ == "__main__":
    main()