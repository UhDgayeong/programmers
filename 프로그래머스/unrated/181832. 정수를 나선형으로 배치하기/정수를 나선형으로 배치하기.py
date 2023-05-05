def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    x, y = 0, 0
    min_x, min_y = 0, 0
    max_x , max_y = n-1, n-1
    
    for i in range(1, n**2 + 1):
        answer[x][y] = i
        if x == min_x:
            if y < max_y: # 오른쪽 방향
                y += 1
                if y == max_y:
                    min_x += 1
                    continue

        if y == max_y:
            if x < max_x: # 아래 방향
                x += 1
                if x == max_x:
                    max_y -= 1
                    continue
        
        if x == max_x:
            if y > min_y: # 왼쪽 방향
                y -= 1
                if y == min_y:
                    max_x -= 1
                    continue
                    
        if y == min_y:
            if x > min_x: # 위 방향
                x -= 1
                if x == min_x:
                    min_y += 1
                    continue
                
    return answer