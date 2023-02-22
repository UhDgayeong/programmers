import math

def solution(number, limit, power):
    div_arr = []
    
    for n in range(1, number + 1):
        tmp = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                tmp.append(i)
                if n // i != i:
                    tmp.append(n / i)
        div_arr.append(len(tmp))

    div_arr = [i if i <= limit else power for i in div_arr]
        
    return sum(div_arr)