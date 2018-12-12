from sage.all import *

def varWiener(e, n):
	q = 1			#beginning with q0 = 1
	m = 62415
	c = pow(m, e, n)
	
	cfList = continued_fraction(Integer(e)/Integer(n))
	convList = cfList.convergents()

	for i in convList:
		k = i.numerator()
		q1 = int(i.denominator())

		for a in range(15):
			for b in range(15):
				d = a*q + b*q1
				#print(d)
				check_message = pow(c, d, n)
				print(check_message)
				if check_message == m :
					print "FOUND d :P "
					print(d)
					break
		q = q1
	return None

e = 197 
n = 1363
varWiener(e, n)


