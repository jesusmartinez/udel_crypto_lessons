from hashlib import sha512
from Crypto.PublicKey import RSA


# RSA sign the message
msg = b'A message for signing'
keyPair = RSA.generate(bits=1024)
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print("Signature:", hex(signature))

# RSA verify signature
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hash == hashFromSignature)