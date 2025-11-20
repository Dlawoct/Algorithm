def solution(sizes):
    max_h = 0
    max_w = 0
    
    for h, w in sizes:
        small = min(h,w)
        big = max(h,w)
        max_h = max(max_h, big)
        max_w = max(max_w, small)
        
    return max_h * max_w
    

# 그냥 제일 큰 가로와 세로 길이를 구하는 것이 아니라
# 카드의 가로, 세로를 돌릴 수 있음
# 큰거는 큰거로, 작은거는 작은거로
# h가 긴쪽, w가 짧은쪽