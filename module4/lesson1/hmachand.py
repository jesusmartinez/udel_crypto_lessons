import binascii, hashlib

k = b'secretkey'
msg = b'forge this punks'

kplus = k + b'\x00'*(64-len(k))
ipad = b'\x36'*64
opad = b'\x5C'*64


def XOR(raw1, raw2):
  return binascii.unhexlify(format(int(binascii.hexlify(raw1), 16) ^ int(binascii.hexlify(raw2), 16), 'x'))


xor_kplus_ipad = XOR(kplus, ipad)
xor_kplus_opad = XOR(kplus, opad)
tag = hashlib.sha256(xor_kplus_opad + hashlib.sha256(xor_kplus_ipad + msg).digest()).digest()

print(binascii.hexlify(tag))


key = b'82f3b69a1bff4de15c33'
msg = b'fcd6d98bef45ed6850806e96f255fa0c8114b72873abe8f43c10bea7c1df706f10458e6d4e1c9201f057b8492fa10fe4b541d0fc9d41ef839acff1bc76e3fdfebf2235b5bd0347a9a6303e83152f9f8db941b1b94a8a1ce5c273b55dc94d99a171377969234134e7dad1ab4c8e46d18df4dc016764cf95a11ac4b491a2646be1'
tag = hashlib.sha256(XOR(key, msg)).digest()
print(binascii.hexlify(tag))