def smaller_even_number(target):
  if target == 2:
    print(target)
    return target
  else:
    if target % 2 == 0:
      print(target)
    return smaller_even_number(target-1)

smaller_even_number(50)