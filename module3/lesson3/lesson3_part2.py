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
print(ciphertext)


'''
INCOMPLETE
CBC by hand: 
Now recompute this number using the IV, XOR, 
and individual runs of the block cipher (one block at a time) 
with my secret key.
'''
hextext_1 = binascii.hexlify(b'abcdefghijklmnop')
hextext_2 = binascii.hexlify(b'qrstuvwxyzabcdef')
hexkey = binascii.hexlify(key)
hexiv = b'000102030405060708090a0b0c0d0e0f'

block_cipher_1 = int(hextext_1, 16) ^ int(hexiv, 16)
cipher_1 = block_cipher_1 ^ int(hexkey, 16)

block_cipher_2 = cipher_1 ^ int(hextext_2, 16)
cipher_2 = block_cipher_2 ^ int(hexkey, 16)

cipher_as_hex = format(int((str(cipher_1) + str(cipher_2))), 'x')
print("Cipher as hex: " + str(cipher_as_hex))
# print("Cipher as hex: " + binascii.unhexlify(cipher_as_hex))
