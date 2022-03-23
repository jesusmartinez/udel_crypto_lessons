from tinyec import registry
import secrets


def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]


'''
DHKE with ECC
- ECC Curve is received 
- Bob generates public and private Key
- Bob replies with its public key
'''
def bob_ecc(rsa, curve, alice_public_key):
    # Verify RSA signature first
    # For Curve
    hash_from_signature = pow(curve['signature'], rsa.e, rsa.n)
    # If mismatch, am exception will be thrown
    if curve['hash'] != hash_from_signature:
        raise Exception("ERR: RSA Signature not valid!!")

    # From curve
    # Generate Bob's private and public keys
    bob_private_key = secrets.randbelow(curve['curve'].field.n)
    bob_public_key = bob_private_key * curve['curve'].g

    shared_key = alice_public_key * bob_private_key
    print("Shared Key (Bob):  ", compress(shared_key))

    return bob_public_key
