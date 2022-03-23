# Lesson 5
from param_reader import read_ecc
import random
import hashlib

params = read_ecc()
A = params.get('A')
B = params.get('B')
p = params.get('Prime')
generator = params.get('Gener')
order = params.get('Order')

x = generator[0]
y = generator[1]

# ECC DHE
a = random.randint(2, order-1)
aP = a * p

b = random.randint(2, order-1)
bP = b * p

print('baP = ', b * aP)
print('abP = ', a * bP)
print(b * aP == a * bP)

# AES with x-coordinate
x_hex = format(x, 'x')
print('x(HEX) = ', x_hex)
x_hash = hashlib.sha256(x_hex.encode('utf-8')).hexdigest()
print(x_hash)