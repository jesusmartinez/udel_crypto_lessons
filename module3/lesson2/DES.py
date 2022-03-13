# pip install pycryptodome

from crypto.Cipher import DES


scheme = DES.new('87654321')
ciphertext = scheme.encrypt('andyrulz')
print(ciphertext)
print(scheme.decrypt(ciphertext))