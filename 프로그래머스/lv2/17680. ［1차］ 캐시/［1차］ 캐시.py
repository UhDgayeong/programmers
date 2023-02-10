def solution(cacheSize, cities):
    answer = 0
    cities = [c.lower() for c in cities]
    cach_arr = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for c in cities:
        for idx, val in enumerate(cach_arr):
            if val == c:
                del cach_arr[idx]
                answer += 1
                break
        else:
            answer += 5
        
        cach_arr.append(c)
        if len(cach_arr) > cacheSize :
            del cach_arr[0]
        
    return answer