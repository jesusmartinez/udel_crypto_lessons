# Test this out: Alter the code from the last part to take in a third parameter r
# which is the number of stretches we do. Hand compute the result for a specific
# password and salt when r=3 then make sure your function's output matches
# (even the screenshot I have above this task).

import bcrypt
import hashlib

psw = 'SuperSecure'
salt = 'something'
iterations = 3

def consume(p, s, r):
    x = '0'
    for n in range(r):
        enc = (x+p+s).encode('utf-8')
        x = hashlib.sha512(enc).hexdigest()
    return x

saltedPsw = consume(psw, salt, iterations)
print("Salted psw: " + str(saltedPsw))
# 7b9cd98b42f8c2c22767e9a74f6aeb34e2085c0d8dbae7edf9fe7ed19fcf67120497a23aee03d68c8b847241791b88c45737a153c59b88693778653ecce65d87
