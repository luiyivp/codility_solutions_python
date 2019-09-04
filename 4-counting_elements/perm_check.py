def solution(A):
    n = len(A)
    A = set(A)
    expected_sum = n*(n+1)//2
    real_sum = sum(A)
    
    if(expected_sum - real_sum == 0):
      return 1
    else:
      return 0
