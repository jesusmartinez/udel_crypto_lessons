import random


def is_Prime(n):
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


modulus = '00b92c49180402208fd2730415ed8ef7baea7715997cfd0c35baec1f'
m = int(modulus, 16)
e = 65537
private_exponent = '459990abb72df981356fc7b45a38e3aaa3d4e13cacd2b3c67c9f49'
d = int(private_exponent, 16)
print('d: ', d)
prime1 = '0eca06b9fdfcc322789c135c9133'
p = int(prime1, 16)
print('p: ', p)
prime2 = '0c8556bea0a3d7ac3d9347a9d165'
q = int(prime2, 16)
print('q: ', q)

n = p * q
print('n: ', n)
phi_of_N = (p - 1) * (q - 1)
print('phi: ', phi_of_N)

x = e * d
res = x % phi_of_N
print('n = p . q')
print('e . q = 1 mod (p -1) . (q - 1) = ', res)
print('Is p prime?', is_Prime(p))
print('Is 1 prime?', is_Prime(q))
