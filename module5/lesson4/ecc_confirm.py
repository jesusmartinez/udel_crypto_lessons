from param_reader import read_ecc

params = read_ecc()
# print(params)
a = params.get('A')
b = params.get('B')
prime = params.get('Prime')
generator = params.get('Gener')
order = params.get('Order')
print('A', a)
print('b', b)
print('generator', generator)
print('prime', prime)
print('order', order)

x = generator[0]
y = generator[1]

res = ((x * x * x) + (a * x) + b) % prime
print('((x * x * x) + (a * x) + b %) p = ', res)
res2 = (y * y) % prime
print('(y * y) % p                     = ', res2)
print('Match?', res == res2)
