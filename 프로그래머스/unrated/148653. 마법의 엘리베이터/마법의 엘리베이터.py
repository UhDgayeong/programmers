def solution(storey):
    answer = float('inf')
    
    need_visit = [(storey, 0, 1)]
    while need_visit:
        floor, cnt, cipher = need_visit.pop()
        break_point = False
        if floor == 0:
            if answer > cnt:
                answer = cnt
            continue
        if str(floor)[0] == '1':
            for i in range(1, len(str(storey))+1):
                if floor == 10 ** i:
                    if answer > cnt + 1:
                        answer = cnt + 1
                    break_point = True
                    break

        if break_point:
            continue

        val = int(str(floor)[-cipher])
        need_visit.append((floor - val*(10**(cipher - 1)), cnt + val, cipher + 1))
        need_visit.append((floor + (10 - val)*(10**(cipher - 1)), cnt + 10 - val, cipher + 1))
        
    return answer