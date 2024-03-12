arr = [ 3, 5, 6, 7, 8, 9, 23, 55, 66, 76, 223, 456, 500, 1230]

def binary_search_ite(arr, target):
  left = 0
  right = len(arr) - 1

  while(left <= right):
    mid = (right + left) // 2

    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1

index_ite = binary_search_ite(arr, 3333)
print(arr[index_ite])

def binary_search_rec(arr, left, right, target):
  if right >= left:
    mid = (right + left) // 2

    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      return binary_search_rec(arr, left, mid - 1, target)
    else:
      return binary_search_rec(arr, mid + 1, right, target)
  else:
    return -1

index_rec = binary_search_rec(arr, 0, len(arr)-1, 8)
print(arr[index_rec])