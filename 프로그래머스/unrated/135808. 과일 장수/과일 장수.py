def solution(k, m, score):
    answer = 0
    len_score = len(score)
    score = sorted(score, reverse = True)
    
    i = 0
    while len(score) - i >= m:
        tmp = score[i:i+m]
        answer += min(tmp) * m
        i += m

    return answer