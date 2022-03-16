from Crypto.Cipher import AES
import binascii

# 16 bytes = 128 bits
key = binascii.unhexlify(b'000102030405060708090a0b0c0d0e0f')
# AES.MODE_ECB is default encryption
scheme = AES.new(key)
cipher = binascii.unhexlify(b'00112233445566778899aabbccddeeff')

result = scheme.encrypt(cipher)
print(binascii.b2a_hex(result))
# output '69c4e0d86a7b0430d8cdb78070b4c55a'
