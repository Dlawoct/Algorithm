def solution(n):
    answer = 0
    text = ""
    while n > 0:
        text = text + str(n % 3)
        n //= 3
        
    return int(text,3)

# 3진법 ... + x*3^2 + x*3^1 + x*3^0