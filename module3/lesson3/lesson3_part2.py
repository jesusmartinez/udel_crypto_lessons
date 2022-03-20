'''
CBC via Library:
Using the secret key "andy love simone" (16 characters/bytes) and
IV from the 16-byte hexdigest "000102030405060708090a0b0c0d0e0f"
then the encryption of "abcdefghijklmnopqrstuvwxyzabcdef" (32 bytes)
is "87dd2acb714db44393d8b4b71bdbad7720fbf40d2e34a03a93324cb9c4b97a08" (32 bytes).
Confirm this using PyCrypto.
'''
from Crypto.Cipher import AES
import binascii


# Secret Key of 16 bytes
key = b'andy love simone'
# IV of 16 bytes
iv = binascii.unhexlify(b'000102030405060708090a0b0c0d0e0f')
# text of 32 bytes
text = b'abcdefghijklmnopqrstuvwxyzabcdef'

scheme = AES.new(key, AES.MODE_CBC, iv)
result = scheme.encrypt(text)
ciphertext = binascii.b2a_hex(result)
print("First output: " + ciphertext.decode('utf-8'))


'''
CBC by hand: 
Now recompute this number using the IV, XOR, 
and individual runs of the block cipher (one block at a time) 
with my secret key.
'''
hextext_1 = binascii.hexlify(b'abcdefghijklmnop')
hexkey = binascii.hexlify(b'andy love simone')
hexiv = b'000102030405060708090a0b0c0d0e0f'

# First chunk
# Plaintext(first 16-bytes) _XOR_ IV
block_cipher_1 = int(hextext_1, 16) ^ int(hexiv, 16)
# Encrypt(Key, block_cipher_1)
scheme1 = AES.new(key)
block_cipher_1_hex = format(block_cipher_1, 'x')
# Encryption is performed in ascii
c1 = scheme1.encrypt(binascii.unhexlify(block_cipher_1_hex))
# Encrypted is transformed into HEX
cipher_1 = binascii.hexlify(c1)

# Second chunk
# c1_hex _XOR_ Plaintext(second 16-bytes)
hextext_2 = binascii.hexlify(b'qrstuvwxyzabcdef')
block_cipher_2 = int(cipher_1, 16) ^ int(hextext_2, 16)
# Encrypt(Key, block_cipher_1)
block_cipher_2_hex = format(block_cipher_2, 'x')
# Encryption is performed in ascii
c2 = scheme1.encrypt(binascii.unhexlify(block_cipher_2_hex))
# Encrypted is transformed into HEX
cipher_2 = binascii.hexlify(c2)

print("Must match  : " + cipher_1.decode('utf-8') + cipher_2.decode('utf-8'))

