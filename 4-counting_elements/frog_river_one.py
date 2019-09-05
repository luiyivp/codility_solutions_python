def solution(X, A):
    i = 0
    sec = 0
    counter = [0] * X  
    n = len(counter)
    total = n * (n + 1) // 2
    aux = 0

    for i in range(n):
      counter[i] = i + 1

    for num in A:
      aux += counter[num - 1]
      counter[num - 1] = 0

      if aux == total:
        return sec
      sec += 1      
    
    return -1
