def solution(my_string, letter):
    answer = [s for s in my_string if s != letter]
    return ''.join(answer)