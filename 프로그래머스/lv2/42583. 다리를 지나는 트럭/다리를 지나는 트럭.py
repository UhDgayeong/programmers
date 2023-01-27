def solution(bridge_length, weight, truck_weights):
    answer = 0   
    on_bridge = [0] * bridge_length # 다리 위에 있는 트럭들
    sum_bridge = 0 # 현재 다리 위의 트럭들 무게 합 sum(on_bridge[:-1])
    
    while len(truck_weights) > 0:  
        answer += 1
        last_truck = on_bridge.pop()
        sum_bridge -= last_truck
        
        if (sum_bridge + truck_weights[0]) <= weight: # 트럭이 새로 다리 위로 올라갈 수 있는 경우
            new_truck = truck_weights.pop(0)
            on_bridge.insert(0, new_truck)
            sum_bridge += new_truck
        else : # 새로운 트럭이 올라올 수 없는 경우 -> 위에 있던 트럭들이 한 칸씩 앞으로 이동
            on_bridge.insert(0, 0)
        
    return answer + bridge_length