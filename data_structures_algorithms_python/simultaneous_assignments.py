# all expressions of the right side are
# evaluated before assigning them in the left side
x, y, z = 6, 2, 5

# this is great for swaping values
x, z = z, x

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a+b