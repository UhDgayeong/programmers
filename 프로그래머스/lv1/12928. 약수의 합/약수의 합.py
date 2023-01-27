def solution(n):
    mid = int(n ** (1/2))
    divisor = []
    for i in range(1, mid + 1):
        if n % i == 0:
            divisor.append(i)
            divisor.append(n/i)
            
    
    answer = sum(divisor)
    return answer - mid if (n ** (1/2)).is_integer() else answer