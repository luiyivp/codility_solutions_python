def solution(S, P, Q):
  factors = []
  
  for i in range(len(P)):
    substring = S[P[i]:Q[i] + 1]

    if 'A' in substring:
      factors.append(1)
    elif 'C' in substring:
      factors.append(2)
    elif 'G' in substring:
      factors.append(3)
    else:
      factors.append(4)

  return factors
