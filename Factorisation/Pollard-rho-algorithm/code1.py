from random import randint
from fractions import gcd
from math import *

def PollardRho(n):
    i = 0
    xi = randint(0, n-1)
    k = 2       #cycles
    y = xi

    while i<n:
        i+=1
        xi = ((xi**2) - 1) % n
        d = gcd(y-xi, n)
        if d!=1 and d!=n:
            print("found d")
            return d

        if i == k:
            y = xi
            k = 2*k
            #print(k)


p = PollardRho(10403)
q = 10403/p
print(p)
print(q)
