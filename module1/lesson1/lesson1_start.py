import hashlib

h1 = hashlib.sha512(b"andy rocks your face off")
print(h1.hexdigest())
b = hashlib.sha512(b"boulders")
print(b.hexdigest())