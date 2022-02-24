import hashlib

with open('../dictionary.txt', 'r') as f:
    words = [word.strip() for word in f]
f.close()

# mix = 'intercellular pargos'
# secret = 'ca704c712e7e3c6af5550aac55eccd2c7512b987c1e10e1a85bd946589071aa26e8f6954d89715222e1bb2b6ad5a6ea3feb58cb168ea5bbd3d51080525994e12'
# It takes too much time

mix = 'ab aahing'
secret = '08b69552656cd07400840cbbec16e6a7ea914d4e563477ff0ee1dec01ca817cd2043f25df80f7bd2ff9769dc1413ebbaae04b6978c3a93d0d0a0ffe2c81da0e4'
h1 = hashlib.sha512(mix.encode('utf-8'))
print(h1.hexdigest())


def checkDictionary():
    for word1 in words:
        for word2 in words:
            combination = word1 + " " + word2
            if hashlib.sha512(combination.encode('utf-8')).hexdigest() == secret:
                return 'Answer: ' + combination
    return "... not found"

print(checkDictionary())