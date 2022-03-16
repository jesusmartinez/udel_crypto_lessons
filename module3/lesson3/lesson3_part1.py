from PIL import Image
from Crypto.Cipher import AES
import hashlib
import os
from Crypto.Util import Counter

im = Image.open('heckert_gnu.png', mode='r', formats=['PNG'])

# Key
m = hashlib.sha256()
m.update(b'password')
key = m.digest()
# IV
iv = os.urandom(32)
print('IV is: ' + str(iv))
# AES
scheme = AES.new(key, AES.MODE_ECB, iv)
msg = scheme.encrypt(im.tobytes())

# Create new image in ECB
im2 = Image.new(im.mode, im.size)
im2.frombytes(msg[::-1])
im2.save("copy1_in_ECB.png")


# Create new image in CTR
counter = Counter.new(128)
scheme2 = AES.new(key, AES.MODE_CTR, iv, counter)
msg2 = scheme2.encrypt(im.tobytes())

im3 = Image.new(im.mode, im.size)
im3.frombytes(msg2[::-1])
im3.save("copy1_in_CTR.png")

# help from https://www.programcreek.com/python/?code=StorjOld%2Ffile-encryptor%2Ffile-encryptor-master%2Ffile_encryptor%2Fconvergence.py