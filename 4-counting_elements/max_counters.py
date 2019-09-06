def solution(N, A):
    counter = [0] * N
    pre_max = 0
    max_counter = 0

    for num in A:
      if num > N:
        if max_counter != pre_max:
          counter = [max_counter] * N
      else:
        counter[num - 1] += 1        
        if counter[num - 1] > max_counter:
          pre_max = max_counter
          max_counter = counter[num - 1]   

    return counter
