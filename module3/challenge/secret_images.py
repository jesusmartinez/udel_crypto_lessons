from Crypto.Cipher import AES
from Crypto.Util import Counter
from PIL import Image
import hashlib
import os
import binascii


def encrypt(file, key, mode):
    im = Image.open(file, mode='r', formats=['PNG'])
    # IV
    iv = os.urandom(16)
    # print(str(iv))
    iv_hex = binascii.hexlify(iv)
    new_file = iv_hex.decode('utf-8') + '.png'

    # AES
    if mode == AES.MODE_CTR:
        counter = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
        scheme = AES.new(key, AES.MODE_CTR, counter=counter)
    else:
        scheme = AES.new(key, mode, iv)
    msg = scheme.encrypt(im.tobytes())

    # Create new image
    im2 = Image.new(im.mode, im.size)
    im2.frombytes(msg)
    im2.save(new_file)

    return new_file


def decrypt(file, key, mode):
    im = Image.open(file, mode='r', formats=['PNG'])
    # IV
    iv_hex = file[0:-4]
    iv = binascii.unhexlify(iv_hex.encode('utf-8'))
    # print(str(iv))

    # AES
    if mode == AES.MODE_CTR:
        counter = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
        scheme = AES.new(key, AES.MODE_CTR, counter=counter)
    else:
        scheme = AES.new(key, mode, iv)
    msg = scheme.decrypt(im.tobytes())

    # Create new image
    im2 = Image.new(im.mode, im.size)
    im2.frombytes(msg)
    im2.save("DEC_" + file)


password = b'password12345678'

new_file = encrypt(file='super-man.png', key=password, mode=AES.MODE_CTR)
print('MODE_CTR file created: ' + new_file)
decrypt(file=new_file, key=password, mode=AES.MODE_CTR)
#
# new_file = encrypt(file='super-man.png', key=password, mode=AES.MODE_ECB)
# print('MODE_ECB file created: ' + new_file)
# decrypt(file=new_file, key=password, mode=AES.MODE_ECB)

# new_file = encrypt(file='super-man.png', key=password, mode=AES.MODE_CBC)
# print('MODE_CBC file created: ' + new_file)
# decrypt(file=new_file, key=password, mode=AES.MODE_CBC)

