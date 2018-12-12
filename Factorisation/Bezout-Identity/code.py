def e(a,b):
    r = b
    x = a    # becomes gcd(a,b)
    s = 0
    y = 1    # the coefficient of a
    t = 1
    z = 0    # the coefficient of b
    while r:
        q = x / r
        x, r = r, x%r
        y, s = s, y-q*s
        z, t = t, z-q*t
    return y%(b/x), z%(-a/x)

print(e(31,71))  



