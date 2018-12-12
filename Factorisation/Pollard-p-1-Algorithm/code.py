from sage.all import *

def Pollardp(n, B):
	a = 2

	for p in primes(B):
		s = 1
		while(s*p <= B):
			s = s * p
		g = gcd(pow(a, s, n)-1, n)
		if(1 < g < n):
			return g
	return None
	

f1 = Pollardp(1403, 6)
print(f1)
