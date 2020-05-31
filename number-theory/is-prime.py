import math

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True