from collections import Counter

def solution(s):
    counter = Counter(s)
    return True if counter['p'] + counter['P'] == counter['y'] + counter['Y'] else False