def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    answer = [s for s in my_string if s not in vowel]
    return ("").join(answer)