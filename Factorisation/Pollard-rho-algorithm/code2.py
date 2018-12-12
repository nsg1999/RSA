from Crypto.Util.number import *

number = 10403
y = 2
cycle = 2
x = 2
fac = 1

while fac == 1:
    count = 1
    while count <= cycle and fac <= 1:
        print(count, cycle, x, y,fac)
        x = (pow(x, 2) + 1) % number
        #print(x)
        fac = GCD(x - y, number)
        print(fac)
        count += 1
    cycle *= 2
    #print(cycle)
    y = x

print("--------------------")
print(count, cycle, x, y)
