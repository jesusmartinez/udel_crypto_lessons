import random
from Crypto.Util.number import GCD

common = 2
paint = 257

print("We try to achieve Alice's secret with GCD=1...")
alice_secret = random.randint(2, 256)
while GCD(alice_secret, paint-1) != 1:
    alice_secret = random.randint(2, 256)

alice_public = pow(common, alice_secret, paint)
print("Alice's public: " + str(alice_public))
print("Alice's triplet (paint, common, Alice's public): ", paint, common, alice_public)

print("We try to achieve Bob's secret with GCD=1...")
bob_secret = random.randint(2, 256)
while GCD(bob_secret, paint-1) != 1:
    bob_secret = random.randint(2, 256)
bob_public = pow(common, bob_secret, paint)
print("Bob's public: " + str(bob_public))
print("Bob's triplet (paint, common, Bob's public): ", paint, common, bob_public)

shared = pow(bob_public, alice_secret, paint)
shared2 = pow(alice_public, bob_secret, paint)
print("Alice's computes same result as Bob", shared, shared2, shared2 == shared)
