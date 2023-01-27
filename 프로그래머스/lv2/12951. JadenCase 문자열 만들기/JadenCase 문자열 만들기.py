def solution(s):
    s = s.split(" ")
    answer = []
    for a in s:
        answer.append(a.capitalize())
    return (" ").join(answer)