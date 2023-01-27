import math

def solution(n):
    prime_list = [True] * (n + 1)
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime_list[i] == True:
            j = 2
            while i * j <= n:
                prime_list[i * j] = False
                j += 1
    
    answer = [i for i in range(2, n + 1) if prime_list[i]]
    return len(answer)