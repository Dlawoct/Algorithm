import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

N, M = map(int, input().split())
num = [i for i in range(N+1)]

def find(x):
    if num[x] != x:
        num[x] = find(num[x])
    return num[x]

def union (a, b):
    a = find(a)
    b = find(b)
    if a < b:
        num[b] = a
    else:
        num[a] = b

for i in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")