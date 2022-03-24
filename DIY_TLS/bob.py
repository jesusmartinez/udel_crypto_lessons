import json
import secrets
from base64 import b64decode
from Crypto.Cipher import AES
import binascii
import time


def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]


'''
DHKE with ECC
- ECC Curve is received 
- Bob generates public and private Key
- Bob replies with its public key
'''
shared_key = 0
def bob_ecc(rsa, curve, alice_public_key):
    print("Bob  : ...verifying RSA DS")
    # Verify RSA signature first
    # For Curve
    hash_from_signature = pow(curve['signature'], rsa.e, rsa.n)
    # If mismatch, am exception will be thrown
    if curve['hash'] != hash_from_signature:
        raise Exception("ERR: RSA Signature not valid!!")
    print("Bob  : ...ECC curve")
    # From curve
    # Generate Bob's private and public keys
    print("Bob  : ...generating private and public keys")
    bob_private_key = secrets.randbelow(curve['curve'].field.n)
    bob_public_key = bob_private_key * curve['curve'].g

    global shared_key
    shared_key = compress(alice_public_key * bob_private_key)
    print("Bob  : Shared Key --> ", shared_key)

    return bob_public_key


def decrypt(stream):
    print("Bob  : ...decrypting data")
    json_k = ['nonce', 'header', 'ciphertext', 'tag']
    try:
        b64 = json.loads(stream)
        jv = {k: b64decode(b64[k]) for k in json_k}

        key = binascii.unhexlify(shared_key[2:34])
        cipher = AES.new(key, AES.MODE_GCM, nonce=jv['nonce'])
        cipher.update(jv['header'])

        return cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])
    except (ValueError, KeyError):
        print("ERR: Incorrect decryption!!")


def bob_receive(stream):
    print("Bob  : ...receiving data")
    data = decrypt(stream)

    file_name = 'received_file_' + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    f = open(file_name, "x")
    f.write(data.decode('utf-8'))
    f.close()
    print("Bob  : File '" + file_name + "' was created")
