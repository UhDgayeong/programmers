def solution(players, callings):
    players_dict = {val:idx for idx, val in enumerate(players)}
    
    for calling in callings:
        idx = players_dict[calling]
        front = players[idx - 1]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        players_dict[front] = idx
        players_dict[calling] = idx - 1
        
    return players