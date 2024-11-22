# 두 사람의 이름을 받고 친구 관계가 있는 지 확인한다
# 둘 밖에 없으면 2, 나왔던 이름이 또 나오면 친구가 1명 증가
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기

# a, b의 루트 노드를 찾음
# a, b 중 하나를 다른 노드의 루트 노드로 설정
def union(a, b):
    
    # 각 친구의 부모 노드 찾기
    a = find(a) 
    b = find(b)
    
    if a == b:  # 부모 노드가 같으면 이미 union 됨
        return
    else:   # 부모 노드가 다르면 a를 부모 노드로 만든다
        parent[b] = a
        visited[a] += visited[b]    # b에 연결된 횟수도 a에 더해줌
    

def find(x):
    if x == parent[x]:  # 부모 노드가 자기 자신 일때
        return x    # 결국엔 부모 노드를 리턴

    parent[x] = find(parent[x])
    return parent[x]    # 부모 노드가 다른 노드이면 다시 find

T = int(input())

for i in range(T):
    F = int(input())
    
    parent = dict()
    visited = dict()
    
    for j in range(F):
        a, b = input().split()
        
        # 친구 관계에 없을 경우 추가 (첫 등장 시)
        if a not in parent:
            parent[a] = a   # 부모 노드에 자기 자신 입력
            visited[a] = 1  # 이 이름은 넣었다는 것을 표시
        
        if b not in parent:
            parent[b] = b
            visited[b] = 1
            
        union(a, b)
        
        print(visited[find(a)])