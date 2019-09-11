def solution(A):
    A = sorted(A)

    for i in reversed(range(2, len(A))):
        if A[i - 2] + A[i - 1] > A[i]:
            return 1
            
    return 0
