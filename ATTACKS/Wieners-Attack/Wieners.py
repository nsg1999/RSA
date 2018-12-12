
from sage.all import *

def wiener(e, n):
    message = 98347651
    ciphertext = pow(message, e, n)
    cfList = continued_fraction(Integer(e)/Integer(n))
    convList = cfList.convergents()
   
    
    for i in convList:
        k = i.numerator()
        d = int(i.denominator())
        try:
            m1 = pow(c, d, n)
            if m1 == m:
                print "Found d: ", d
                return d
        except:
            continue
    return -1


print("THIS IS A TEST FOR Weiner's ATTACK")
print("**********************************")
test_d = wiener(70760135995620281241019, 205320043521075746592613 )
print(test_d)

