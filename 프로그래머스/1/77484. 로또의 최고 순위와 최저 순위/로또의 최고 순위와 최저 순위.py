def solution(lottos, win_nums):
    answer = []
    rank = {6:1, 5:2, 4:3, 3:4, 2:5}
    correct_cnt = len(set(lottos) & set(win_nums)) # 로또 맞춘 갯수
    zero_cnt = lottos.count(0) # 로또 0 갯수
    max_rank = correct_cnt + zero_cnt
    min_rank = correct_cnt
    
    if max_rank > 1:
        answer.append(rank[max_rank])
    else:
        answer.append(6)
    
    if min_rank > 1:
        answer.append(rank[min_rank])
    else:
        answer.append(6)
    
    
    return answer

# 이 번호가 안지워졌다면 몇등이였을까?(최고 순위와 최저 순위)
# 최고 순위는 남은 0이 모두 정답일 경우
# 최저 순위는 남은 0이 모두 오답일 경우

