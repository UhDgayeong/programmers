def solution(arr, query):
    for idx, val in enumerate(query):
        if idx % 2 == 0:
            arr = arr[:val + 1]
        elif idx % 2 == 1:
            arr = arr[val:]
    return arr