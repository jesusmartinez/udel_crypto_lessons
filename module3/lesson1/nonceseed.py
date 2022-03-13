import os, hashlib, binascii

nonce = os.urandom(6)
hexnonce = binascii.hexlify(nonce)
oursecret = 54321
concatenated_hex = hexnonce.decode('utf-8') + format(oursecret, 'x')
even_length = concatenated_hex.rjust(len(concatenated_hex) + len(concatenated_hex) % 2, '0')
hexhash = hashlib.sha256(binascii.unhexlify(even_length)).hexdigest()
newseed = (int(hexhash, 16)) % 2**32
print(newseed)

# If I send a 6-byte NONCE of "cc4304c09aee" and our original seed was 54321
# then calculate the new seed using this method.
my_nonce = "cc4304c09aee"
concatenated_hex = my_nonce + format(oursecret, 'x')
even_length = concatenated_hex.rjust(len(concatenated_hex) + len(concatenated_hex) % 2, '0')
hexhash = hashlib.sha256(binascii.unhexlify(even_length)).hexdigest()
newseed = (int(hexhash, 16)) % 2**32
print(newseed)