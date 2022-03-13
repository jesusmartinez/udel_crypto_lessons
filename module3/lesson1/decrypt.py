import binascii
import encrypt

cipher_text = 'e5d8443c6ac32d3ee5c7398ecf7f9e03f619'

mygen = encrypt.crand(54321)
rands = [next(mygen) for i in range(6)] # Use length of seed
hexkey = "".join(map(lambda x: format(x, 'x')[-6:], rands))

cipher_as_int = int(cipher_text, 16) ^ int(hexkey, 16)
cipher_as_hex = format(cipher_as_int, 'x')

plain = binascii.unhexlify(cipher_as_hex)
print(plain)