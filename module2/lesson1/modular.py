# Greatest Common Divisor
x = 0
def gcd(a, b):
    if b == 0:
        return a
    else:
        global x
        x = x + 1
        return gcd(b, a % b)

# test it and use a global variable to show the number of times gcd calls itself
print(gcd(56, 42), x)
x = 0
print(gcd(8, 13), x)
x = 0
print(gcd(1071, 462), x)
x = 0
print(gcd(3000, 197), x)

# Grab a couple of fibonacci numbers from the internet and see that those make for the worst-case performance.
print()
x = 0
print(gcd(34, 9), x)
print(gcd(4181, 233), x)
print(gcd(196418, 46368), x)