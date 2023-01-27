def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2)) + 1):
        if yellow % i == 0:
            a = i + 2
            b = yellow / i + 2
            if a * b == brown + yellow:
                return [max(a, b), min(a, b)]
    return 0