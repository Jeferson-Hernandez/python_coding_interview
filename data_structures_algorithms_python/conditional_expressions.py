# is a way to compound an expression to make it simplier

def foo(param):
  print(param)

# conditional expressions
# long version
n = 10
if n >= 0:
  param = n
else:
  param = -n
result = foo(param)

# compound version
param = n if n <= 0 else -n
foo(param)

#comprehension sintax 
#list comprehension

# [ expression for value in iterable if condition ] (if is optional)

squares_normal = []
for k in range(1, n+1):
  squares_normal.append(k*k)

squares_comprehension = [k*k for k in range(n,n+1)]

factors_comprehension = [k for k in range(1,n+1) if n % k == 0]

# [k*k for k in range(n,n+1)] list comprehension
# {k*k for k in range(n,n+1)} set comprehension
# (k*k for k in range(n,n+1)) generator comprehension
# {k : k*k for k in range(n,n+1)} dictionary comprehension