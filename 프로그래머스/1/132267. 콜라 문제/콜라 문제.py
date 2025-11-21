def solution(a, b, n):
    answer = 0
    while(n >= a):
        tmp = (n // a) * b
        answer += tmp
        remain = n % a
        n = tmp + remain
    return answer
# 10 10 0 10
# 5 5 0 5
# 2 2 1 3
# 1 1 1 2
# 1 1 0 1