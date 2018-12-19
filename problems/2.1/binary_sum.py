def binary_sum(A, B):
    carry = 0
    C = []
    for i in range((len(A)-1), -1, -1):
        i_sum = A[i] + B[i] + carry
        if i_sum > 1:
            i_sum -= 2
            carry = 1
        else:
            carry = 0
        C.append(i_sum)
    C.append(carry)
    C.reverse()
    return C