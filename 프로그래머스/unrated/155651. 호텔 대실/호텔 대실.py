def solution(book_time):
    answer = 0
    now_booking = []
    times = []
    for b in book_time:
        start, end = b
        start_h, start_m = map(int, start.split(":"))
        s = start_h * 60 + start_m
        end_h, end_m = map(int, end.split(":"))
        e = end_h * 60 + end_m + 10
        times.append((s, e))
        
    times = sorted(times, key = lambda x : x[0])
    
    for t in times:
        start, end = t
        now_booking.append(end)
        if now_booking: # 배열이 비어있지 x
            now_booking.sort()
            if now_booking[0] <= start: # 빈 방이 생길 경우
                del now_booking[0]
            else: # 빈 방이 생기지 않은 경우
                answer += 1
        else:
            answer += 1
    
    return answer