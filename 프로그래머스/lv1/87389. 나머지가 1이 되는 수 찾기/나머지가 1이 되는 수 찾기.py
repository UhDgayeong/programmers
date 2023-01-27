def solution(n):
    if n % 2 == 1: # 홀수 => 2
        return 2
    else: # 짝수
        for i in range(3, n):
            if n % i == 1:
                return i