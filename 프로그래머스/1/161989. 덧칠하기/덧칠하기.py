def solution(n, m, section):
    answer = 0
    until = 0
    
    for s in section:
        if s > until:
            answer += 1
            until = s + m -1
    
    return answer

# n: 벽의 길이
# m: 한번에 칠할 수 있는 범위
# sectioin: 빵구난 곳