import math

def check_prime(n1: int) -> bool:
    assert(n1 > 0)
    
    if(n1 in [1,2]):
        return True
    
    for i in range(2, int(math.sqrt(n1))+2):
        if n1%i == 0: return False
        
    return True

def backwardsPrime(n1: int, n2: int) -> list:
    assert(0 < n1 < n2)
    
    backwards_primes = []
    
    for i in range(n1, n2+1):
        
        i_reversed = int(str(i)[::-1])
        
        if(i!=i_reversed and check_prime(i) and check_prime(i_reversed)):
            backwards_primes.append(i)
    
    return backwards_primes
    