from sage.all import *

def factor(n):
    a = 2
    b = 2
    while True:
        if b % 10000 == 0:
            print(b)
            
        a = pow(a, b, n)
            
        p = gcd(a - 1, n)
        if 1 < p < n:
            print("FOUND " + str(p))
            return p
            
        b += 1

	

f1 = factor(1403)
print(f1)
