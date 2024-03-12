# is a better way to create a list(iterator) from a function
# generators dont store its values on memory

#normal version
def factors_normal(n):
  result = []
  for k in range(1,n+1):
    if n % k == 0:
      result.append(k)
  return result

factor_normal_arr = factors_normal(100)
print(factor_normal_arr)

#generator version
def factor_generator(n):
  for k in range(1,n+1):
    if n % k == 0:
      yield k

factor_generator_arr = list(factor_generator(200)) 
print(factor_generator_arr)
