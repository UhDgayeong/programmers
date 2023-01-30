from itertools import combinations

def solution(number):
    answer = 0
    combs = list(combinations(number, 3))
    
    for c in combs:
        if sum(list(c)) == 0:
            answer += 1

    return answer