def solution(k, d):
    answer = 0
    square_d = d**2

    for x in range(0, d + 1, k):
        answer += int((square_d - x ** 2) ** 0.5) // k + 1
        
    return answer