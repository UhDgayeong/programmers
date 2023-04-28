from collections import defaultdict

def solution(plans):
    answer = []
    stack = []
    pause = []
    
    for plan in plans:
        name, start, playtime = plan
        h, m = map(int, start.split(":"))
        mins = h * 60 + m
        stack.append([name, mins, int(playtime)])
        
    stack = sorted(stack, key = lambda x : x[1], reverse = True)
    
    while stack:
        name, start, playtime = stack.pop()
        if stack: # 예정 계획이 남아있는 경우
            next_start = stack[-1][1]
            if start + playtime > next_start: # 현재 계획을 다 끝마치지 못할 때
                pause.append([name, playtime - (next_start - start)])
            else:
                answer.append(name)
                if start + playtime < next_start and pause: # 현재 계획 끝내고 다음 계획까지 시간 남을 때
                    now = start + playtime
                    while pause:
                        until_next = next_start - now
                        pause_name, pause_playtime = pause.pop()
                        
                        if pause_playtime <= until_next:
                            answer.append(pause_name)
                            if pause_playtime == until_next:
                                break
                            now += pause_playtime
                        else:
                            pause.append([pause_name, pause_playtime - until_next])
                            break
        else:
            answer.append(name)
        
    while pause:
        name, _ = pause.pop()
        answer.append(name)
        
    return answer