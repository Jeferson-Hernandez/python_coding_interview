#packing values separated with colon will end up in a tupla
#automatic packing of a tuple
data = 2, 5, 7, 8, 4, 35, 55
print(data, type(data))

#unpacking the sequence must be equal to the amount of variables
a, b, c, d = range(7, 11)

#unpacking the result of a function
quotient, remainder = divmod(50, 3)

#for loop
for x, y in [(7,2), (5,8), (6,4)]:
  pass

#dict
mapping = { 1: 'a', 2: 'b', 3: 'c'}
for k, v in mapping.items():
  pass