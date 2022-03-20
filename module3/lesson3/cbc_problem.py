from Crypto.Cipher import AES
import binascii

# KEY= '--2HusJqWSbaFomc'
KEY = b'002HusJqWSbaFomc'
IV = b'0123456789abcdef'
# 32-bytes length
message = "Encrypt this message wit AES plz"

def encrypt(thesecret):
    cipher = AES.new(thesecret, AES.MODE_CBC, IV)
    return cipher.encrypt(message)

# res = binascii.hexlify(encrypt(KEY))
# print("encrypted data: " + str(res))

# d8a53f0660c3f8c434a26841d2dc61a53f0660c3f8c434a26841d2dc93d62632 --> 32-bytes
# d8--------------------------61a53f0660c3f8c434a26841d2dc93d62632 --> 19-bytes
# 13-bytes missing
# cipher 1 --> d8--------------------------61a5
# cipher 2 --> 3f0660c3f8c434a26841d2dc93d62632


# l = [str(n) for n in range(0,10)] + [chr(x) for x in range(ord('A'), ord('Z')+1)] + [chr(x) for x in range(ord('a'), ord('z')+1)]
# l = [str(n) for n in range(0,10)]
l = [chr(x) for x in range(ord(' '), ord('~')+1)]
# print(l)
k_1 = '2HusJqWSbaFomc'
#INCOMPLETE!!!
for i in l:
    for j in l:
        key = i +j + k_1
        # print(key)
        scheme = AES.new(key.encode('utf-8'))
        block = scheme.decrypt(b'3f0660c3f8c434a26841d2dc93d62632')
        block_hex = binascii.hexlify(block).decode('utf-8')
        if block_hex[:2] == 'd8' or block_hex[4:] == '61a5':
        # if block_hex[2:] == 'a5':
            print(key, block_hex)
            break
