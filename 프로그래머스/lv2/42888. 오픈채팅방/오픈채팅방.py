def solution(record):
    answer = []
    user_dict = {}
    
    for r in record:
        rec = r.split()
        if len(rec) > 2: # 유저 이름 저장
            cmd, uid, nickname = rec
            user_dict[uid] = nickname
            
    for r in record:
        rec = r.split()
        if len(rec) > 2: # Enter, Change
            cmd, uid, _ = rec
            if cmd == "Enter" :
                answer.append(f"{user_dict[uid]}님이 들어왔습니다.")
        else: # Leave
            uid = rec[1]
            answer.append(f"{user_dict[uid]}님이 나갔습니다.")
            
    return answer