from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii


def assertEqual(a, b):
    if a == b:
        print('OK', a, b)
    else:
        print('ERR!', a, b)


plaintext = b'martinez'
ciphertext = b'\xff|\xf3\x9c"\xe4C\xe4'
key = '2b7e151628aed2a6abf7158809cf4f3c'
iv = b'\x90\x9c\xfa\xe3t\xfe5\xd7\x88\xf67{\xe3+)"'

key = binascii.unhexlify(key)
cipher = AES.new(key, AES.MODE_CTR, counter=lambda: iv)
assertEqual(cipher.encrypt(plaintext), ciphertext)

cipher = AES.new(key, AES.MODE_CTR, counter=lambda: iv)
assertEqual(cipher.decrypt(ciphertext), plaintext)