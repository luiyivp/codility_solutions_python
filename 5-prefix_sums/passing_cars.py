def solution(A):
  pairs = 0
  cars = 0

  for num in A:
    if cars > 1000000000:
      return -1
    if num == 0:
      pairs += 1
    else:
      cars += pairs
  return cars
