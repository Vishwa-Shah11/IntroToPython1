def linear(P, Q, k):

    if len(P) != len(Q):
        return False
    if P[0] != k*Q[0]:
        return False
    return linear(P[:-1], Q[:-1], k)


print(linear([2, 4, 6, 8], [1, 2, 3, 4], 2))
                