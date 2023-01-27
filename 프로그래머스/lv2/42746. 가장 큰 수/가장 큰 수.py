def solution(numbers):
    if max(numbers) == 0:
        return '0'
    numbers = list(map(lambda x:str(x)*3,numbers))
    numbers.sort(reverse=True)
    numbers = list(map(lambda x:x[0:int(len(x)/3)], numbers))
    
    return ''.join(numbers)