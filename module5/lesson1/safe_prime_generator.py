import random
from math import sqrt


def is_prime(num):
    prime = True
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if (num % i) == 0:
                prime = False
                break
    else:
        prime = False
    return prime


def safe_prime(bits):
    found_safe_prime = False
    ohshit = 0
    while not found_safe_prime and ohshit < 1000000:
        ohshit += 1
        q = 2 * random.randint(2**(bits - 1), 2**bits) - 1
        if pow(2, 2 * q, 2 * q + 1) != 1:
            continue
        if not is_prime(q):
            continue
        found_safe_prime = True
    if ohshit >= 1000000:
        return -1
    return 2 * q + 1

# Takes little time
# print(safe_prime(8))
# print(safe_prime(16))
# print(safe_prime(32))

# Takes too much time
# print(safe_prime(64))
#  1024 (the smallest "safe" prime size for DH). WARNING: be prepared to stop the process!
#print(safe_prime(1024))
