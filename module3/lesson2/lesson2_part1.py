# sudo pip install pycrypto
from Crypto.Cipher import DES

scheme = DES.new('87654321') # 8-byte
ciphertext = scheme.encrypt('andyrulz') # 8-byte
print(ciphertext)
print(scheme.decrypt(ciphertext))