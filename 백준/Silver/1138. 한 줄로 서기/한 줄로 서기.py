# 해시 함수랑 비슷함
# 숫자 1부터 시작해 자기 보다 앞에 있는 숫자의 갯수 만큼 인덱스 이동
# 만약 같은 숫자라면 해당 인덱스에서 0이 나올때까지 이동
N = int(input())
people = list(map(int, input().split()))
ans = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == people[i] and ans[j] == 0:
            ans[j] = i + 1
            break
        elif ans[j] == 0:
            cnt += 1

for k in ans:
    print(k, end=" ")