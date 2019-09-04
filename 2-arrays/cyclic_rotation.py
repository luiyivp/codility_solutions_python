def solution(A, K):
  if K == A.__len__() or A == []:
    return A
  while K > 0: 
    A.insert(0,A.pop())
    K -= 1
  return A
