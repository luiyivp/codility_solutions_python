def solution(N):
  bin_n = "{0:b}".format(N)
  current_gap = 0
  max_gap = 0

  for n in bin_n:
    if(n == '0'):
      current_gap += 1
    
    if(n == '1'):
      if(current_gap > max_gap):
        max_gap = current_gap
      current_gap = 0
  
  return max_gap
