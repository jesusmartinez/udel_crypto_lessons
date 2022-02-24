import binascii

mes = "Andy ROX!"
# key = '6016f1fdcc7bedd9e0'
key = b'\x16\xf1\xfd\xcc{\xed\xd9\xe0'
print(mes)

mes_hex = mes.encode('utf-8').hex()
mes_int = int(mes_hex, 16)


key_hex = binascii.b2a_hex(key)
key_int = int(key_hex, 16)

# XOR
enc_xored = mes_int ^ key_int
enc_hex = format(enc_xored, 'x')

# Encode in Hex
evenpad = ('0' * (len(enc_hex) % 2)) + enc_hex
print("Encoded HEX: " + str(evenpad))
enc = binascii.unhexlify(evenpad)
print("Encoded: " + str(enc))
print(" ")


# Decrypt
dec_int = int(evenpad, 16)
dec_xored = dec_int ^ key_int
dec_hex = format(dec_xored, 'x')
dec_pad = ('0' * (len(dec_hex) % 2)) + dec_hex
dec = binascii.unhexlify(dec_pad)
print("Decoded: " + str(dec))