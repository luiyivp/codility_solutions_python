def solution(A):
    A = sorted(A)
    length = len(A)-1
    i = 0

    if(length == 0):
      return A[0]

    if(A[length] != A[length-1]):
      return A[length]

    while(i < length):
      if(A[i] != A[i+1]):
        return A[i]
      i += 2
