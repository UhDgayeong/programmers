from collections import defaultdict
import heapq

def dijkstra(graph, start):
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [start, distances[start]])
    
    while queue:
        current_destination, current_distance = heapq.heappop(queue)
        
        if distances[current_destination] < current_distance:
            continue
        
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [new_destination, distance])
                 
    return distances

def solution(N, road, K):
    answer = 0
    
    graph = defaultdict(dict)

    for r in road:
        a, b, c = r
        if b in graph[a] and graph[a][b] < c:
            continue
        else:
            graph[a][b] = c
            
    for r in road:
        a, b, c = r
        if a in graph[b] and graph[b][a] < c:
            continue
        else:
            graph[b][a] = c
        
    graph = dict(graph)
    print(graph)
    distances = dijkstra(graph, 1)
    for d in distances:
        if distances[d] <= K:
            answer += 1

    return answer