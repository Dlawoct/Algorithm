def solution(price, money, count):
    cal = sum([price * i for i in range(1,count+1)])
    if cal > money: 
        return cal - money
    else:
        return 0
