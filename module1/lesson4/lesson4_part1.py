# XOR produces the difference of AND, OR

a = [8, 11, 15]
b = [10, 12, 14]

for x in a:
    for y in b:
        print(str(x) + " AND " + str(y) + " = " + str(x & y))
        print(str(x) + " OR " + str(y) + " = " + str(x | y))
        print(str(x) + " XOR " + str(y) + " = " + str(x ^ y))
        print(" ")

# For a given number 240
# Choose a random one like 90
# Now:
# 240 ^ 90 = 170
# 240 ^ 170 = 90
# 170 ^ 90 = 240