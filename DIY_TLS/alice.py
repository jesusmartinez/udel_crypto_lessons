from bob import *
from tinyec import registry
import secrets
import json
from hashlib import sha512
from base64 import b64encode
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
import binascii


'''
Receives a message and generates:
- RSA key pair
- Hash of the message
- Digital signature
'''
def rsa_signature(msg):
    key_pair = RSA.generate(bits=1024)
    hash = int.from_bytes(sha512(str(msg).encode('utf-8')).digest(), byteorder='big')
    # msg = b'A message for signing'
    # hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
    signature = pow(hash, key_pair.d, key_pair.n)
    # hashFromSignature = pow(signature, keyPair.e, keyPair.n)
    # print("Signature valid:", hash == hashFromSignature)

    return key_pair, hash, signature


def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]


'''
DHKE with ECC
- ECC Curve is created
- Alice shares it with Bob 
- Alice generates public and private Key
- Alice receives for Bob's public key
'''
def ecc():
    print("Alice: ...generating ECC curve")
    # Generate ECC curve
    ecc_curve = registry.get_curve('brainpoolP256r1')
    # Generate Alice's private and public keys
    print("Alice: ...generating private and public keys")
    alice_private_key = secrets.randbelow(ecc_curve.field.n)
    alice_public_key = alice_private_key * ecc_curve.g

    # RSA signature of curve
    print("Alice: ...signing with RSA DS")
    rsa, curve_hash, curve_signature = rsa_signature(ecc_curve)
    curve = {
        'curve': ecc_curve,
        'signature': curve_signature,
        'hash': curve_hash
    }

    # Send to Bob: RSA, ECC curve and Alice's public Key
    # If it's RSA signature is validated correctly,
    # Alice receives Bob's public key
    print("Alice: ...sending ECC curve")
    bob_public_key = bob_ecc(rsa, curve, alice_public_key)

    shared_key = alice_private_key * bob_public_key
    print("Alice: Shared Key --> ", compress(shared_key))

    return compress(shared_key)


def read_file():
    print("Alice: File 'quotesOrig.txt'")
    f = open("quotesOrig.txt", 'rb')
    txt = f.read()
    f.close()

    return txt


def encrypt(key):
    print("Alice: ...reading data to send")
    data = read_file()

    print("Alice: ...encrypting data with AES GCM mode")
    header = b'andy'
    key = binascii.unhexlify(key[2:34])
    cipher = AES.new(key, AES.MODE_GCM)
    cipher.update(header)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    json_k = ['nonce', 'header', 'ciphertext', 'tag']
    json_v = [b64encode(x).decode('utf-8') for x in [cipher.nonce, header, ciphertext, tag]]

    return json.dumps(dict(zip(json_k, json_v)))

if __name__ == '__main__':
    # Start
    print("Alice: ...start")

    # Initiate Key Swap
    shared_key = ecc()

    # Encrypt
    stream = encrypt(shared_key)

    # Send file
    print("Alice: ...sending data")
    bob_receive(stream)
