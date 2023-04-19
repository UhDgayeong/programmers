from collections import defaultdict
import heapq

def dijkstra(graph, start, K, N):
    distances = {node:float('inf') for node in range(1, N + 1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [start, distances[start]]) # (시작점, 잰 거리) 쌍으로

    while queue:
        current_destination, current_distance = heapq.heappop(queue)

        if distances[current_destination] < current_distance: 
            continue
        
        if current_destination not in graph:
            continue

        for new_destination in graph[current_destination]:
            distance = current_distance + 1
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                if distance <= K:
                    heapq.heappush(queue, [new_destination, distance])

    return distances

def main():
    N, M, K, X = map(int, input().split())

    road_dict = defaultdict(list)

    for _ in range(M):
        A, B = map(int, input().split())
        road_dict[A].append(B)

    road_dict = dict(road_dict)
    distances = dijkstra(road_dict, X, K, N)
    my_dict = defaultdict(list)
    for d in distances.items():
        key, val = d
        my_dict[val].append(key)
    my_dict = dict(my_dict)

    answer = []
    if K in my_dict:
        for n in my_dict[K]:  
            answer.append(n)
    else:
        print(-1)
        return
    
    answer.sort()
    for a in answer:
        print(a)


if __name__ == "__main__":
    main()