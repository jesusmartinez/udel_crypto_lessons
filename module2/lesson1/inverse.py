def modInverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return -1


print(modInverse(3, 10))
print(modInverse(16, 19))