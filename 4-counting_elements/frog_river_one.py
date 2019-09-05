def solution(X, A):
    i = 0
    sec = 0
    counter = [0] * X
    B = [0] * X    
    n = len(B)
    b_sum = n * (n + 1) // 2
    aux = 0

    for i in range(n):
      B[i] = i + 1

    for num in A:
      counter[num - 1] += 1
      aux += B[num - 1]
      B[num - 1] = 0

      if aux == b_sum:
        return sec
      sec += 1      
    
    return -1
