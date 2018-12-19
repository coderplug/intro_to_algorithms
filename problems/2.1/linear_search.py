def linear_search(A, v):
    for i in range(len(A)):
        if v == A[i]:
            return i
    return "NIL"