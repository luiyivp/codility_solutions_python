def solution(A):
    n = len(A)
    validator = [False] * n

    for num in A:
      if 0 < num <= n:
        validator[num - 1] = True

    for i in range(len(validator)):
      if validator[i] == False:
        return i + 1
    
    return n + 1
