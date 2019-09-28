def solution(A):
  n = len(A)
  size = 0
  for i in range(n):
    if size == 0:
      size += 1
      value = A[i]
      index = i
    else:
      if value != A[i]:
        size -= 1
      else:
        index = i
        size += 1
  candidate = -1
  if size > 0:
    candidate = value
  count = 0
  for i in range(n):
    if A[i] == candidate:
      count += 1
  if count <= n // 2:
    index = -1
  return index
