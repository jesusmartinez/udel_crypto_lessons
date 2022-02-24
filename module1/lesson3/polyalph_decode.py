# Decode what polyalph produces
# Solution call decode, decode_with_spaces

def shiftBackBy(c, n):
    return chr(((ord(c) - ord('a') - n) % 26) + ord('a'))

def decode(code, key):
    return "".join([shiftBackBy(code[i], key[i % len(key)]) for i in range(len(code))])

def decode_with_spaces(code, key):
    return decode(code.replace(' ', ''), key)

raw = decode("tvcrqrmpdzzdtbdlb", [19, 8, 25])
print("Raw 1 is: ", raw)

raw = decode_with_spaces("ytgwo vrnhe xhyzh qz", [24, 6, 3])
print("Raw without spaces is: ", raw)