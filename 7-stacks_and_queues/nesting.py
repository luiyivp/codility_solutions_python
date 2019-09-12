def solution(S):
  S = list(S)
  stack = []

  if len(S) == 0:
    return 1

  for i in range(len(S)):
    if S[i] == ')' and stack == []:
      return 0
      
    if S[i] == '(':
      stack.append(S[i])
    else:
      if S[i] == ')' and stack[-1] == '(':
        stack.pop()
      else:
        return 0

  if stack != []:
    return 0
  else:
    return 1
