import math

def solution(w,h):
    answer = w * h
    if w < h:
        w, h = h, w
    gcd = math.gcd(w, h)
    tmp = 0
    if gcd != 1:
        w, h = w // gcd, h // gcd
    tmp += w + h - 1

    return answer - tmp * gcd