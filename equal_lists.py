def equality(P, Q):
    if len(P) != len(Q):
        return False
    if len(P) == 0:
        return True
    if P[-1] != Q[-1]:
        return False
    return equality(P[: -1], Q[: -1])
print(equality([1,2,3], [3,2,1]))
print(equality([], []))