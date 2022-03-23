from param_reader import read_dsa
from Crypto.Util.number import inverse
import random
import hashlib


def is_prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n != int(n):
        return False
    n = int(n)
    # Miller-Rabin test for prime
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True


params = read_dsa()
# print(params)
p = params.get('P')
q = params.get('Q')
g = params.get('G')
d = params.get('priv')
pub = params.get('pub')

print('(p - 1) % q == 0', (p - 1) % q == 0)
# print(g**q, 1 % p)

print('Is p prime?', is_prime(p))
print('Is q prime?', is_prime(q))

res = pow(g, d, p)
print('G^d mod P', res == pub)

# Integers from signature file signature.bin
s = int('1287541617A98C1A7BCA8701032B28187258C7D0', 16)
r = int('7230C2657E41E367DB267CD3A8AA37161548E464', 16)

# shasum -a 256 thingtosign.txt
z = int('9d35c1353b5135d049f022de3f3a17665c361c6f34e020085ca6a0bdd86f2f16', 16)
# z = int(hashlib.sha256(b"andy is great\n").hexdigest()[:40], 16)
# 9d35c1353b5135d049f022de3f3a17665c361c6f34e020085ca6a0bdd86f2f16

# INCOMPLETE
k_of_e = ((s * ((z + (d * r)) ** -1)) ** -1) % q
s_1 = pow(g, int(k_of_e), p) % p
# result does not assert this below:
print(s == s_1)
