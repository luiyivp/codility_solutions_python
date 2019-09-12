def solution(A, B):
  fishes = 0
  stack = []

  for i in range(len(A)):
    if B[i] == 0:
      while len(stack) != 0:
        if stack[-1] > A[i]:
          break
        else:
          stack.pop()
      else:
        fishes += 1
    else:
      stack.append(A[i])
  
  fishes += len(stack)
     
  return fishes
