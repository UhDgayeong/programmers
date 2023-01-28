from collections import defaultdict

def dfs_recursive(tree, start, cut, visited = []):
    visited.append(start) # 시작 노드로 지정한 노드 방문 처리
    
    # 해당 노드의 자식 노드들을 방문
    for node in tree[start]:
        if node not in visited and node != cut: # 자식 노드가 방문한 적이 없는 노드라면
            dfs_recursive(tree, node, cut, visited) # 해당 노드의 자식 노드들을 방문(재귀)
        
    return visited

def solution(n, wires):
    answer_list = []
    wires_dict = defaultdict(list) # 트리 구조 저장용 딕셔너리
    
    for key, val in enumerate(wires):
        v1, v2 = val
        wires_dict[v1].append(v2)
        wires_dict[v2].append(v1)
    
    wires_dict = dict(wires_dict)
    
    for w in wires:
        v1, v2 = w
        v1_child = len(dfs_recursive(wires_dict, v1, v2, []))
        v2_child = len(dfs_recursive(wires_dict, v2, v1, []))
        answer = v1_child - v2_child if v1_child >= v2_child else v2_child - v1_child
        if answer == 0:
            return answer
        else:
            answer_list.append(answer)
            
    return min(answer_list)