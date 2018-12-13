from Crypto.Util.number import *

m = "flag{Gr34t!_y0u_h4v3_d0n3_it!!}"
p = getPrime(512)
q = getPrime(512)
n = p*q
e = 65537
phin = (p-1)*(q-1)


def egcd(a,b):
	if b == 0:
		return a
	else:
		return egcd(b,a%b)

def mod_inv(a,b,x1,x2,y1,y2):
	gcd = egcd(p,q)
	if gcd == 1:	
		if b == 0:
			return x1
		else:
			x = (x1 - ((a/b)*x2))
			y = (y1 - ((a/b)*y2))
			return mod_inv(b,a%b,x2,x,y2,y)
	else:
		print "mod_inv_doesn't_exist"

m = bytes_to_long(m)
d = (mod_inv(e,phin,1,0,0,1))%phin
r = 13907
c = pow(m,e,n)
ct = c * pow(r,e,n)
ct = pow(ct,d,n)
pt = ct/r
print long_to_bytes(pt)

