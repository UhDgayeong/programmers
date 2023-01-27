def solution(d, budget):
    d.sort()
    cnt = 0
    for idx, val in enumerate(d):
        cnt += val
        if cnt > budget:
            return idx
    else:
        return len(d)