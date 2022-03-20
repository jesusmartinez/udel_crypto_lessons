import hmac, hashlib

# print(hmac.new(b'secretkey', b'forge this punks', hashlib.sha256).hexdigest())

key = b'82f3b69a1bff4de15c33'
msg = b'fcd6d98bef45ed6850806e96f255fa0c8114b72873abe8f43c10bea7c1df706f10458e6d4e1c9201f057b8492fa10fe4b541d0fc9d41ef839acff1bc76e3fdfebf2235b5bd0347a9a6303e83152f9f8db941b1b94a8a1ce5c273b55dc94d99a171377969234134e7dad1ab4c8e46d18df4dc016764cf95a11ac4b491a2646be1'
print(hmac.new(key, msg, hashlib.sha256).hexdigest())