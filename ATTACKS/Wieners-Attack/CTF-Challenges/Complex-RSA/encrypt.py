from Crypto.PublicKey import RSA
f1 = open("pubkey1.txt", "r")
key = RSA.importKey(f1.read())
print "n1 =", key.n
print "e1 =", key.e

f2 = open("pubkey1.txt", "r")
key = RSA.importKey(f1.read())
print "n1 =", key.n
print "e1 =", key.e

f3 = open("flag.enc", "r")
print f3.read().encode('hex')
