# INCOMPLETE!
from Crypto.Cipher import AES
import binascii

key = b'andy love simone'
iv = b'\x00'*16
cipher = AES.new(key, AES.MODE_CBC, iv)
result = cipher.encrypt("andy love simoneandy love simone")
print(binascii.b2a_hex(result))


def XOR(raw1, raw2):
  return binascii.unhexlify(format(int(binascii.hexlify(raw1), 16) ^ int(binascii.hexlify(raw2), 16), 'x'))


scheme = AES.new(key, AES.MODE_CBC, iv)
result = scheme.encrypt(key)

cipher1 = binascii.b2a_hex(result)
# 16-bytes length
p1 = XOR(cipher1, key)
# print(p1)
result = scheme.encrypt(p1)
cipher2 = binascii.b2a_hex(result)
print(cipher2)
# tag = binascii.unhexlify(b'd6fdc5d5596e6ff6c3039cfbb5d9216f')