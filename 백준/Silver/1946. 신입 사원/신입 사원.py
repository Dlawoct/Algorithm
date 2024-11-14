# 서류심사 성적 또는 면접 시험 성적 중 적어도 하나가 다른 지원자보다 뛰어나야함
# A의 성적이 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어지면 선발 x

# 1 4 0 
# 2 3 0
# 3 2 0 
# 4 1 0
# 5 5


# 1 4 0 / 5 7
# 2 5   / 3 6
# 3 6   / 2 5
# 4 2 0 / 1 4
# 5 7   / 7 3
# 6 1 0 / 4 2
# 7 3   / 6 1

# 1차로 정렬하고 1차 1등보다 등수가 높은 애들만 선정
import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    N = int(input())
    ranking = [list(map(int, input().split())) for _ in range(N)]  
    ranking = sorted(ranking, key= lambda x : x[0]) # 서류 성적을 기준으로 정렬
    
    top = ranking[0][1]
    cnt = 1 # 서류 1등은 무조건 합격

    for j in range(1,N):
        if top > ranking[j][1]:  # 서류 1등부터 비교해 면접이 높은 것들 비교
            top = ranking[j][1]    # 계속 갱신하며 그 다음으로 면접이 높은 사람 할당
            cnt +=1
    print(cnt)