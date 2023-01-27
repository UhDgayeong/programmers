def solution(numbers, hand):
    answer = ''
    cur_L = [3, 0]
    cur_R = [3, 2]
    
    for num in numbers:
        if num == 0:
            row = 3
            col = 1
        else:
            row = (num - 1) // 3
            col = (num - 1) % 3
            
        if col == 0:
            answer += "L"
            cur_L = [row, col]
        elif col == 2:
            answer += "R"
            cur_R = [row, col]
        else:
            dist_L = abs(row - cur_L[0]) + abs(col - cur_L[1])
            dist_R = abs(row - cur_R[0]) + abs(col - cur_R[1])
            if dist_L < dist_R:
                answer += "L"
                cur_L = [row, col]
            elif dist_R < dist_L:
                answer += "R"
                cur_R = [row, col]
            else:
                if hand == "left":
                    answer += "L"
                    cur_L = [row, col]
                else:
                    answer += "R"
                    cur_R = [row, col]
                          
    return answer