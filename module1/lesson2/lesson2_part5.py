# Test this out: Alter the code from the last part to take in a third parameter r
# which is the number of stretches we do. Hand compute the result for a specific
# password and salt when r=3 then make sure your function's output matches
#
# Time it Use the time module or some timing mechanism (example follows)
# find an r which causes your hash function to take 1 second.
# Solution: around 730,000

import binascii

import bcrypt
import hashlib
import time

# Step 1: Calculate
psw = b'SuperSecure'
def consume(p):
    s = bcrypt.gensalt()
    starttime = time.perf_counter()
    x = b'0'
    r = 0
    while time.perf_counter() - starttime < 1:
        enc = x+p+s
        x = hashlib.sha512(enc).digest()
        r += 1
    print(time.perf_counter() - starttime)

    return [s, r, x]

[salt, iterations, theHash] = consume(psw)

print("Salt: " + str(salt))
print("r: " + str(iterations))
print("theHash in ASCII: " + str(theHash))
print("theHash in HEX: " + str(binascii.b2a_hex(theHash)))

# Step 2: Prove
def prove(p, s, i):
    x = b'0'
    r = 0
    while r < i:
        enc = x + p + s
        x = hashlib.sha512(enc).digest()
        r += 1
    return x

result = prove(psw, salt, iterations)
print("Prove the result: " + str(binascii.b2a_hex(result)))
