from collections import deque

def solution(maps):
    answer_list = []
    max_x = len(maps) - 1
    max_y = len(maps[0]) - 1
    
    def bfs(x, y):
        q = deque()
        q.append((x, y, 1))
        
        while q:
            x, y, cnt = q.popleft()
            
            if x == max_x and y == max_y: # 상대 팀 진영 도착
                answer_list.append(cnt)
                return
            if maps[x][y] == 0: # 이미 지나온 곳이거나 벽인 경우
                continue
            maps[x][y] = 0 # 이미 지나간 곳은 다시 가지 않도록

            if y != max_y:
                q.append((x, y + 1, cnt + 1)) # 동쪽
            if y != 0:
                q.append((x, y - 1, cnt + 1)) # 서쪽
            if x != max_x:
                q.append((x + 1, y, cnt + 1)) # 남쪽
            if x != 0:
                q.append((x - 1, y, cnt + 1)) # 북쪽
        
    bfs(0, 0)
    
    return min(answer_list) if len(answer_list) != 0 else -1