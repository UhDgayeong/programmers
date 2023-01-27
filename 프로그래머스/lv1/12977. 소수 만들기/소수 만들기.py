import math
from itertools import combinations

def solution(nums):
    answer = 0
    nums.sort()
    max_num = sum(nums[-3:])
    prime_list = [True] * (max_num + 1)
    
    for i in range(2, int(math.sqrt(max_num)) + 1):
        if prime_list[i]:
            j = 2
            while i * j <= max_num:
                prime_list[i * j] = False
                j += 1
    prime_list = [i for i in range(2, max_num + 1) if prime_list[i]]
    
    comb = list(combinations(nums, 3))
    for c in comb:
        if sum(c) in prime_list:
            answer += 1
    
    return answer