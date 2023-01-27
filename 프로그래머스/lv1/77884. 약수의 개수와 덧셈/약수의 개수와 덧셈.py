import math

def solution(left, right):
    return sum([-i if math.sqrt(i).is_integer() else i for i in range(left, right + 1) ])