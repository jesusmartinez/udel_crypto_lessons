from Crypto.Util.number import long_to_bytes, bytes_to_long, inverse

e = 65537
prime1 = '0eca06b9fdfcc322789c135c9133'
p = int(prime1, 16)
prime2 = '0c8556bea0a3d7ac3d9347a9d165'
q = int(prime2, 16)
n = p * q
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

msg = b'Saturday night studying'
msg_as_int = bytes_to_long(msg)

encryption = pow(msg_as_int, e, n)
print('Encrypted msg: ', encryption)
print('d: ', d)
print('n: ', n)
decryption = pow(encryption, d, n)
print(long_to_bytes(decryption).decode('utf-8'))