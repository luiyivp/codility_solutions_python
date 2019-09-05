# Task Score  88%
# Correctness 100%
# Performance 80%
# TIMEOUT ERROR,  Killed. Hard limit reached: 7.000 sec.

def solution(N, A):
    counter = [0] * N
    max_counter = 0
    
    for num in A:
      if num > N:
        counter = [max_counter] * N
      else:
        counter[num - 1] += 1        
        if counter[num - 1] > max_counter:
          max_counter = counter[num - 1]   

    return counter
