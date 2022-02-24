from binascii import unhexlify

# m = "Hi there"
m = "Andy"
print(m)

# hexstr = m.encode('hex')
hexstr = m.encode('utf-8').hex()
print(hexstr)

integer_m = int(hexstr, 16)
print(integer_m)

back2hex = format(integer_m, 'x')
print(back2hex)

evenpad = ('0' * (len(back2hex) % 2)) + back2hex
# plaintext = evenpad.decode('hex')
plaintext = unhexlify(evenpad)
print(plaintext)

# Convert to an integer: Convert the message "Andy" into an integer
# (by first going to hex then hex to an integer like in the above snippet).
# XOR that number with the random number 320945240 and
# convert the result back into plaintext (the second half of that snippet).
print(' ---- ')
xored = integer_m ^ 320945240
back2hex = format(xored, 'x')
print(back2hex)

evenpad = ('0' * (len(back2hex) % 2)) + back2hex
plaintext = unhexlify(evenpad)
print(plaintext)