import random

def shiftBy(c, n):
    return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))

def encode(raw, keyLength):
    key = [random.randint(1,25) for i in range(keyLength)]
    s1 = []
    for i in range(len(raw)):
        y = shiftBy(raw[i], key[i % keyLength])
        s1.append(y)

    secret = "".join(s1)
    withSpaces = ''
    for i in range(len(secret)):
        if i % 5 == 4:
            withSpaces = withSpaces + secret[i] + ' '
        else:
            withSpaces = withSpaces + secret[i]
    return withSpaces, key

code,key = encode("andyisthegreatest", 3)
print (code, key)
# szcif kfgod jqzdb kf

