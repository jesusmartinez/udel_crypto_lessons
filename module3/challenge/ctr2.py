from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii

# https://www.programcreek.com/python/example/87998/Crypto.Cipher.AES.MODE_CTR
# https://stackoverflow.com/questions/3154998/pycrypto-problem-using-aesctr

key = "i have collies!!"
iv = b'\x90\x9c\xfa\xe3t\xfe5\xd7\x88\xf67{\xe3+)"'
counter = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
# crypto = AES.new(key, AES.MODE_CTR, counter=lambda: iv)
crypto = AES.new(key, AES.MODE_CTR, counter=counter)
encrypted = crypto.encrypt("aaaaaaaaaaaaaaaa")
print(encrypted)

# crypto2 = AES.new(key, AES.MODE_CTR, counter=lambda: iv)
counter = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
crypto2 = AES.new(key, AES.MODE_CTR, counter=counter)
dec = crypto2.decrypt(encrypted)
print(dec)
# print(binascii.hexlify(dec))