# A가 B를 신뢰하면, B를 해킹하면 A도 해킹할 수 있음
# 한 번에 가장 많이 해킹할 수 있는 컴퓨터 번호

# 3이 1을 신뢰 -> 1해킹하면 3 해킹 가능
# 1 해킹 하면 3해킹, 2,4,5 해킹 가능
# 4, 5 해킹 불가
from collections import deque

# N: 컴퓨터 갯수, M: 신뢰관계 갯수
N, M = map(int, input().split())
truth = [[] for i in range(N+1)]    # 컴퓨터의 숫자에 맞춰 인덱스 생성
for i in range(M):
    A, B = map(int, input().split())
    truth[B].append(A) # truth의 컴퓨터 숫자에 해당하는 리스트의 숫자는 자식 노드
    
def bfs(idx):
    dq = deque()
    dq.append(idx)
    cnt = 0
    
    visited = [False] * (N+1)   # 노드에 방문한 것을 확인
    visited[idx] = True # 시작노드 방문
    
    while dq:
        now = dq.popleft()  # 제일 앞을 꺼내 현재로 설정 (1번 노드)
        for next in truth[now]: # now 노드의 자식 노드를 next로
            if not visited[next]: # 방문 안했다면 
                visited[next] = True
                dq.append(next) # 방문 표시와 자식 노드를 deque에 넣음 (3번 노드 방문 & 3번 노드를 덱에 넣음)
                cnt += 1
    return cnt           


result = []
for idx in range(1, len(truth)):    # 1~N까지 컴퓨터 번호
    result.append(bfs(idx))
    
    
# 가장 큰 숫자가 맞는 지 확인하고 해당 인덱스 + 1 출력
for j in range(len(result)): 
    if max(result) == result[j]:
        print(j+1)
