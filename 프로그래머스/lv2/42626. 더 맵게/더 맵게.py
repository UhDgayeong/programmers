from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    scoville.sort()
    heapify(scoville)
    
    while len(scoville) >= 2:
        first = heappop(scoville)
        if first >= K:
            return answer
        second = heappop(scoville)
        mix = first + second * 2
        answer += 1
        heappush(scoville, mix)
        
    if len(scoville) == 1 and scoville[0] >= K:
        return answer
    
    return -1