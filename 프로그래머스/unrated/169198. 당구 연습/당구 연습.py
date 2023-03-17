def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball in balls:
        tmp = []
        a, b = ball
        mirror_arr = [[a, -b], [-a, b], [a, 2*n - b], [2*m - a, b]]
        
        if startX == a:
            if startY < b:
                del mirror_arr[2]
            else:
                del mirror_arr[0]
        if startY == b:
            if startX < a:
                del mirror_arr[3]
            else:
                del mirror_arr[1]
        
        for i in range(len(mirror_arr)):
            m1, m2 = mirror_arr[i]
            tmp.append((startX - m1)**2 + (startY - m2)**2)
            
        answer.append(min(tmp))
        
    return answer