from math import *

def is_square(n):
    
    x = n // 2
    y = set([x])
    
    while x * x != n:
        x = (x + (n // x)) // 2
        
        if x in y: 
        	return False
        y.add(x)
    return True



def FermatFactorisation(N):
	a = ceil(sqrt(N))
	b2 = (a*a) - N		#b*(2) = a*(2) - N   from the equation, N = (a*a) - (b*b)
	
	while not is_square(b2):
		a = a + 1
		b2 = (a*a) - N

	return (a - sqrt(b2), a + sqrt(b2))
	
print(FermatFactorisation(5959))

		
	
