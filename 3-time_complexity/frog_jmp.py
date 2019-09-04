def solution(X, Y, D):
  distance = Y - X

  if distance % D == 0:
    return distance // D
  else:
    return distance // D + 1
