import hashlib, binascii
from lesson1_part2 import decrypt

cipher = '3e08816f1377f89f1c596fc197dd52946c92577bfd7c25c3'
# nonce = cipher[-12:]
# cipher_text = cipher[:-12]
nonce = cipher[:12]
cipher_text = cipher[12:len(cipher)]
key = 61983

concatenated_hex = nonce + format(key, 'x')
even_length = concatenated_hex.rjust(len(concatenated_hex) + len(concatenated_hex) % 2, '0')
hexhash = hashlib.sha256(binascii.unhexlify(even_length)).hexdigest()
seed = (int(hexhash, 16)) % 2**32
print(seed)

# INCOMPLETE, cause after
# "Assuming a secret key of 61983 and the first 6 bytes are NONCE bytes..."
# I get a seed of length 8,
# I'm supposed to decrypt 'f89f1c596fc197dd52946c92577bfd7c25c3',
# but I don't get a valid plain text back.
# I assume that rands = [next(mygen) for i in range(len(str(seed)))],
# where the for loops seed-length times.
plain = decrypt(cipher_text, seed)
print(plain)