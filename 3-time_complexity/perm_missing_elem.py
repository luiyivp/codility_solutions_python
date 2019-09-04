def solution(A):
    n = A.__len__() + 1
    seq = n * (n + 1) // 2

    return seq - sum(A)
