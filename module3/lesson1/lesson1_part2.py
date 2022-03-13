from crand import crand
import binascii

# Write your own encryption/decryption which takes in the
# message/ciphertext and a seed and spits out the ciphertext/message
# using this style stream cipher.
# If your message length is not a multiple of 3 then you'll want to
# cutoff the last bytes of your random values or pad the message.
def encrypt(msg, seed):
    mygen = crand(seed)
    rands = [next(mygen) for i in range(len(str(seed)))]

    hexplain = binascii.hexlify(msg.encode("utf-8"))
    hexkey = "".join(map(lambda x: format(x, 'x')[-6:], rands))

    cipher_as_int = int(hexplain, 16) ^ int(hexkey, 16)
    cipher_as_hex = format(cipher_as_int, 'x')

    evenpad = ('0' * (len(cipher_as_hex) % 3)) + cipher_as_hex
    return evenpad

def decrypt(cipher_text, seed):
    mygen = crand(seed)
    rands = [next(mygen) for i in range(len(str(seed)))]
    hexkey = "".join(map(lambda x: format(x, 'x')[-6:], rands))

    cipher_as_int = int(cipher_text, 16) ^ int(hexkey, 16)
    cipher_as_hex = format(cipher_as_int, 'x')

    plain = binascii.unhexlify(cipher_as_hex)

    return plain.decode("utf-8")

def test(msg):
    seed = 9913142
    enc = encrypt(msg, seed)
    # print("Encrypted: " + str(enc))
    dec = decrypt(enc, seed)
    # print("Decrypted: " + dec)
    if msg == dec:
        print("OK")
    else:
        print("ERR!", msg, dec)


# test("No one's above")
# test("Cogito ergo sum")
# test("Per omnia secula seculorum")
# test("Python is so much fun")