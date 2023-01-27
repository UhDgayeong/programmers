import math

def solution(n):
    if math.sqrt(n).is_integer():
        return (int(math.sqrt(n)) + 1)**2
    return -1