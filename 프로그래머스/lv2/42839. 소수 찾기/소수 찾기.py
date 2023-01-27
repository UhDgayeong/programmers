import itertools
import math

def solution(numbers):
    answer = 0
    n_list = [n for n in numbers]
    per_list = []
    arr = []
    
    for i in range(1, len(n_list) + 1):
        per = list(itertools.permutations(n_list, i))
        per_list.append(per)
    
    for idx, val in enumerate(per_list):
        for v in val:
            arr.append(int(''.join(v)))
    
    arr = list(set(arr))
    
    for a in arr:
        if a <= 1:
            continue
        elif a == 2:
            answer += 1
            continue
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                break
        else :
            answer += 1
            
    return answer