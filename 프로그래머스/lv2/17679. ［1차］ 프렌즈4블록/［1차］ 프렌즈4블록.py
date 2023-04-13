def solution(m, n, board):
    answer = 0
    board.reverse()    
    board_arr = [[] for _ in range(n)]
    #print(board_arr)
    for b in board:
        for idx, val in enumerate(b):
            board_arr[idx].append(val)
            
    #print(board_arr)
    while True:
        del_idx = []
        for idx1, b in enumerate(board_arr[:-1]):
            for idx2, val in enumerate(b[:-1]):
                tmp = [(idx1, idx2+1), (idx1, idx2), (idx1+1, idx2+1), (idx1+1, idx2)]
                if val != 0 and val == board_arr[idx1][idx2+1] and val == board_arr[idx1+1][idx2] and val == board_arr[idx1+1][idx2+1]:
                    del_idx.extend(tmp)

        if not del_idx:
            break
        del_idx = list(set(del_idx))
        answer += len(del_idx)
        print(del_idx)
        del_idx = sorted(del_idx, reverse = True)
        print(del_idx)
        for di in del_idx:
            print(di)
            print(board_arr[di[0]][di[1]])
            del board_arr[di[0]][di[1]]
            board_arr[di[0]].append(0)
        del_idx = []
        #print(del_idx)
            
    print(board_arr)
    return answer