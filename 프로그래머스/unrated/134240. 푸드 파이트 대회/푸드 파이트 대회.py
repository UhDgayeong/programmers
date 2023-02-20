def solution(food):
    answer = ''
    for idx, val in enumerate(food[1:]):
        answer += str(idx + 1) * (val // 2)
    
    reverse = ''.join([i for i in answer[::-1]])
    return answer + '0' + reverse