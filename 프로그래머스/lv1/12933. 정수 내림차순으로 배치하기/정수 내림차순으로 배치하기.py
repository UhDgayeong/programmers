def solution(n):
    answer = [i for i in str(n)]
    answer.sort(reverse=True)
    return int(''.join(answer))