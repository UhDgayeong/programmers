def solution(numbers, target):
    answer = 0
    
    def dfs(num, level):
        nonlocal answer
        
        if level == len(numbers): # 최하단 depth 노드
            if num == target:
                answer += 1
            return
        
        if level == 1: # 최상단 노드일 경우
            nums = [num, -num]
            for i in range(2):
                dfs(nums[i] + numbers[level], level + 1)
                dfs(nums[i] - numbers[level], level + 1)
                
        else: # 중간 depth
            dfs(num + numbers[level], level + 1)
            dfs(num - numbers[level], level + 1)
    
    dfs(numbers[0], 1)
    
    return answer