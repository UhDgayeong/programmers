def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
            
    a = [1, 2, 3]
    b = [4, 5, 6, 7, 8, 9]

    return True