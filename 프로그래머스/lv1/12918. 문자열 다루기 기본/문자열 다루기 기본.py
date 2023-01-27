def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
        return answer
    for a in s:
        if ord(a) < 48 or ord(a) > 57:
            answer = False
            break
    return answer