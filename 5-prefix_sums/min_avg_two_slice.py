def solution(A):
    min_index = 0
    min_value = 10001

    for i in range(0, len(A) - 1):
        if (A[i] + A[i + 1]) / 2 < min_value:
            min_index = i
            min_value = (A[i] + A[i + 1]) / 2.0
        if i < len(A) - 2 and (A[i] + A[i + 1] + A[i + 2]) / 3 < min_value:
            min_index = i
            min_value = (A[i] + A[i + 1] + A[i + 2]) / 3

    return min_index
