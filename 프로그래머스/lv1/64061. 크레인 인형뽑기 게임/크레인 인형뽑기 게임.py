import numpy as np

def solution(board, moves):
    board = list((np.array(board)).T)
    board = [[n for n in row if n != 0] for row in board]
    basket = []
    answer = 0
    
    for move in moves:
        try:
            doll = board[move-1].pop(0)
            basket.append(doll)
            if basket[-1:] == basket[-2:-1]:
                del basket[-2:]
                answer += 1
        except:
            continue

    return answer * 2