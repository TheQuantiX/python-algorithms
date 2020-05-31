def gcd(a, b):
    if a * b == 0:
        return a + b
    if a >= b:
        return gcd(a % b, b)
    return gcd(b % a, a)
    
def lcm(a, b):
    return a // gcd(a, b) * b