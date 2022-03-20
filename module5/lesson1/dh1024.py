'''
By hand using Base64:
now that prime is stored in .pem format
we can get access to it by reading base64.
Import base64 and run base64.standard_b64decode on the parts that matter.
This gives you raw bytes.
Your prime is at raw[6:6+129].
Get these bytes, convert to hex then an integer.
The generator is probably the last byte (normally 2).
'''
import base64
import binascii
from Crypto.Util.number import bytes_to_long
from safe_prime_generator import is_prime

s = 'MIGHAoGBALXvbMAfD240s+fAg14d8vFP79Ltgf7GQW+2VhBnJxNhmJ5brV/2DMhW9czraDMr9P0ST6JW7JE7AdIFKkXBjai0OpxZx0qBisfVChtDid3QAUY86qSfLWy9NnjzEf2hNQOjzIdznqgC1IFPhi7sON2k5AUOKOqIqNTuY23nQVuDAgEC'
e = base64.standard_b64decode(s)
prime = binascii.hexlify(e[6:6+129])
print(prime)
# It is too large to proove it
# print(is_prime(prime))