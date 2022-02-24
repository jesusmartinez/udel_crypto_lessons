# Conversion: Compute a SHA256 hexdigest by hashing any phrase (e.g. "I rule").
# Now convert that string from "562877fbc677d2" style to raw characters like "V(w\xfb\xc6w\xd2" and back (use binascii).

import binascii,hashlib

# Step 1: get the hash
p = b"I rule"
hexascii = hashlib.sha256(p).hexdigest()
# Hash in HEX
print("Hash of: '" + str(p) + "' in HEX is:")
print(hexascii)

# Step 2: convert HEX to ASCII
hexInAscii = bytes.fromhex(hexascii)
print("Hash in ASCII is:")
print(hexInAscii)
# Prove it
realhex = hashlib.sha256(p).digest()
print(realhex)

#Step 3: convert back ASCII to HEX (IMPORTAN STEP HERE)
hexAgain = binascii.b2a_hex(hexInAscii)
print("Hash in HEX again is:")
print(hexAgain)

