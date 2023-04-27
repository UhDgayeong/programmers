import math

def compareAB(arrayA, arrayB):
    a1_divisors = []
    gcd_list = []
    answer = 0
    arrayA.sort()
    for i in range(1, int(math.sqrt(arrayA[0])) + 1):
        if arrayA[0] % i == 0:
            a1_divisors.append(i)
            a1_divisors.append(arrayA[0] // i)

    a1_divisors = list(set(a1_divisors))
    len_A = len(arrayA)
    
    if len_A >= 2:
        for d in a1_divisors[1:]:
            for a in arrayA[1:]:
                if a % d != 0:
                    break
            else:
                gcd_list.append(d)
        
    elif len_A == 1:
        gcd_list = a1_divisors[1:]

    len_b = len(arrayB)
    for a in gcd_list:
        for idx, b in enumerate(arrayB):
            if b % a == 0:
                break
            if idx == len_b - 1:
                if a > answer: answer = a
    
    return answer

def solution(arrayA, arrayB):
    ab = compareAB(arrayA, arrayB)
    ba = compareAB(arrayB, arrayA)
    return ab if ab > ba else ba
    