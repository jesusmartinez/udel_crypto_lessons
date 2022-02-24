with open('encrypted_mobydick.txt', 'r') as f:
    mobytext = f.read()
f.close()

mobytext = mobytext.lower()

onlyletters = filter(lambda x: x.isalpha(), mobytext)
loweronly = list(onlyletters)

frequency = {}
for ascii in range(ord('a'), ord('a')+26):
    frequency[chr(ascii)] = float(loweronly.count(chr(ascii)))/len(loweronly)

sum_freqs_squared = 0.0
for ltr in frequency:
    sum_freqs_squared += frequency[ltr]*frequency[ltr]

print ("Should be near .065 if plain: " + str(sum_freqs_squared))
# Mobydick  Should be near .065 if plain: 0.06253047816880557
# Encrypted Should be near .065 if plain: 0.04013000028606218