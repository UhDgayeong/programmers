def solution(n, words):
    arr = [words[0][0]]

    for idx, val in enumerate(words):
        if val not in arr:
            if arr[-1][-1] != val[0]:
                return [idx % n + 1, idx // n + 1]
            arr.append(val)
        else:
            return [idx % n + 1, idx // n + 1]

    return [0, 0]