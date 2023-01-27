def solution(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        for i in numbers[idx + 1:]:
            answer.append(val + i)

    return sorted(list(set(answer)))