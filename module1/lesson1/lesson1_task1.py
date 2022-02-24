import hashlib

with open('../dictionary.txt', 'r') as f:
    words = [word.strip() for word in f]
f.close()

secret = 'f2a1f8ef23ed53623438ba6bfa9c51dd150237b9a5da38e5d457bbbebdd58a1436b92f270cd34bd24b06eb21dcddaf3dfddc2b2e386f21a55a9fa63b8d7c5c74'
# Solution: 'boulders'

for word in words:
    w = word.encode('utf-8')
    hash = hashlib.sha512(w)
    # hash.digest()
    if hash.hexdigest() == secret:
        print('Word is: ' + word)
        break

print('...end')