import numpy as np

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    arr_1 = np.array(A)
    arr_2 = np.array(B)
    return sum((arr_1 * arr_2).tolist())