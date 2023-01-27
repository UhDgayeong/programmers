from collections import Counter

def solution(k, tangerine):
    answer = 1
    
    cnt = dict(Counter(tangerine))
    sorted_cnt = sorted(cnt.items(), key = lambda item: item[1], reverse = True)
    
    temp = 0
    for s in sorted_cnt:
        temp += s[1]
        if temp >= k:
            return answer
        else :
            answer += 1
    return answer