import binascii

def crand(seed):
    r=[]
    r.append(seed)
    for i in range(30):
        r.append((16807*r[-1]) % 2147483647)
        if r[-1] < 0:
            r[-1] += 2147483647
    for i in range(31, 34):
        r.append(r[len(r)-31])
    for i in range(34, 344):
        r.append((r[len(r)-31] + r[len(r)-3]) % 2**32)
    while True:
        next = r[len(r)-31]+r[len(r)-3] % 2**32
        r.append(next)
        yield (next >> 1 if next < 2**32 else (next % 2**32) >> 1)

mygen = crand(1983)
rands = [next(mygen) for i in range(4)]
plaintext = "andy rules!!"

# hexplain = binascii.hexlify(plaintext)
hexplain = binascii.hexlify(plaintext.encode('utf-8'))
hexkey = "".join(map(lambda x: format(x, 'x')[-6:], rands))

cipher_as_int = int(hexplain, 16) ^ int(hexkey, 16)
print("Cipher as int: " + str(cipher_as_int))
cipher_as_hex = format(cipher_as_int, 'x')
print("Cipher as hex: " + str(cipher_as_hex))