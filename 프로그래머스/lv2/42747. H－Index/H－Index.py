from collections import Counter

def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    
    for idx, val in enumerate(citations):
        if val < idx + 1:
            break
        answer = idx + 1
        
    return answer