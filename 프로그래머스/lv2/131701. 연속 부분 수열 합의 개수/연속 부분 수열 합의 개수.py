from collections import Counter
from itertools import combinations

def solution(elements):
    arr = []
    arr.extend(elements)
    len_e = len(elements)
    
    elements.extend(elements)
    for i in range(1, len_e):
        for j in range(0, len(elements)):
            arr.append(sum(elements[j:j+i+1]))

    return len(set(arr))