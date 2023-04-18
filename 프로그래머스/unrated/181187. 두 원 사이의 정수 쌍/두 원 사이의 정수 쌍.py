import math

def solution(r1, r2):
    answer = 0
    for y in range(1, r2):
        if y <= r1:
            x_min = math.ceil(math.sqrt((r1**2 - y**2)))
        else:
            x_min = 0
        x_max = math.floor(math.sqrt((r2**2 - y**2)))
        answer += x_max - x_min + 1
        
    answer *= 4
    return answer + 4