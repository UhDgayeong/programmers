def solution(s, n):
    answer = ''
    for a in s:
        c = ord(a)
        if a == ' ':
            answer += ' '
        elif c <= 90:
            answer += chr(c + n) if c + n <= 90 else chr(c + n - 26)
        else:
            answer += chr(c + n) if c + n <= 122 else chr(c + n - 26)
    return answer