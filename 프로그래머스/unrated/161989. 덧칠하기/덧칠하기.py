def solution(n, m, section):
    answer = 1
    
    start = section[0]
    for s in section[1:]:
        if s - start >= m: # 시작점에서 같이 칠할 수 없는 경우
            answer += 1
            start = s
            
    return answer