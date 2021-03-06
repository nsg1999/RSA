from sage.all import *

def pollard(n, B):
    a = 2
    for p in primes(B):
        pp = 1
        while pp*p <= B:
            pp *= p
        a = pow(a, pp, n)   # provided a>=b, gcd(a, b) = gcd(a%b, b)
        g = gcd(a-1, n)
        if 1 < g < n:
            return g
    return None


