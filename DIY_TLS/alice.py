from bob import *
from tinyec import registry
import secrets
from hashlib import sha512
from Crypto.PublicKey import RSA


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
    # Generate ECC curve
    ecc_curve = registry.get_curve('brainpoolP256r1')
    # Generate Alice's private and public keys
    alice_private_key = secrets.randbelow(ecc_curve.field.n)
    alice_public_key = alice_private_key * ecc_curve.g

    # RSA signature of curve
    rsa, curve_hash, curve_signature = rsa_signature(ecc_curve)
    curve = {
        'curve': ecc_curve,
        'signature': curve_signature,
        'hash': curve_hash
    }

    # Send to Bob: RSA, ECC curve and Alice's public Key
    # If it's RSA signature is validated correctly,
    # Alice receives Bob's public key
    bob_public_key = bob_ecc(rsa, curve, alice_public_key)

    shared_key = alice_private_key * bob_public_key
    print("Shared Key (Alice):", compress(shared_key))



if __name__ == '__main__':
    # Start
    # Initiate Key Swap
    ecc()

    # alice_key = pick_ecc_secret_key()
    # # Send Alice's Key to Bob
    # bob_key = bob_getKey(alice_key)
    # # Receive Bob's Key
    # shared_key = alice_key * bob_key
    # print("Shared Key (Alice):", shared_key)