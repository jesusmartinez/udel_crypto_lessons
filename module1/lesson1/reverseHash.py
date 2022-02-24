import hashlib, cProfile

with open('../dictionary.txt', 'r') as f:
    words = [word.strip() for word in f]
f.close()

secretHash = hashlib.sha512(b"banana").hexdigest()

def checkDictionary(secret):
    return [word for word in words if hashlib.sha512(word.encode('utf-8')).hexdigest() == secret]

cProfile.run('checkDictionary(secretHash)')