def solution(A):
    diff = 0
    length = len(A)
    left_sum = A[0]
    right_sum = sum(A) - A[0]
    diff = abs(left_sum - right_sum)

    for i in range(1, length):
        if abs(left_sum - right_sum) < diff:
          diff = abs(left_sum - right_sum)
        right_sum -= A[i]
        left_sum += A[i]

    return diff
