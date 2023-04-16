def solution(cipher, code):
    answer = ''
    for idx, val in enumerate(cipher):
        if idx % code == code - 1:
            answer += val
    return answer