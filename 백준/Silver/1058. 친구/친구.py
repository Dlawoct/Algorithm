 # A B C D E
#A N Y N N N    A - B와 친구
#B Y N Y N N    B - A와 친구, C와 친구
#C N Y N Y N    C - B와 친구, D와 친구
#D N N Y N Y    D - C와 친구, E와 친구
#E N N N Y N    E - D와 친구
# i == j 인 경우는 친구가 안됨 (자기자신)
# friend[i][j] == Y면 friend[j][i]도 Y이기 때문에 친구
# friend[i][j] == Y 이고 friend[j][k] == Y 이면 friend[i][k] == Y
# connect 에 A와 친구인 배열 1로 바꾸고, 그 행 다 더하고 젤 큰 값 출력
import sys

N = int(sys.stdin.readline())
friend = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
connect = [[0] * N for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if friend[i][j] == 'Y' or (friend[i][k] == 'Y' and friend[k][j] == 'Y'):
                connect[i][j] = 1
answer = 0
for low in connect:           
    answer = max(answer, sum(low))
print(answer)