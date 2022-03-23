from Crypto.Util.number import getStrongPrime, bytes_to_long, inverse, long_to_bytes

# msg = b'andy rules'
msg = b'Saturday night studying instead of partying'
msg_as_int = bytes_to_long(msg)
p = getStrongPrime(512)
q = getStrongPrime(512)
N = p * q
# print(N)

encryption = pow(msg_as_int, 65537, N)
print(encryption)

phi_of_N = (p - 1) * (q - 1)
d = inverse(65537, phi_of_N)
decryption = pow(encryption, d, N)
print(long_to_bytes(decryption))
