def solution(n):
    answer = [0, 1]
    for _ in range(n - 1):
        answer.append(answer[-2] + answer[-1])

    return answer[-1] % 1234567