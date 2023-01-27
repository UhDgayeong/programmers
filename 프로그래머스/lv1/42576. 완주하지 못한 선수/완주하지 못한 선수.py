def solution(participant, completion):
    participant.sort()
    completion.sort()

    answer = ""
    for idx, val in enumerate(participant):
        if val not in completion[idx:idx+1]:
            answer = val
            break
    return answer