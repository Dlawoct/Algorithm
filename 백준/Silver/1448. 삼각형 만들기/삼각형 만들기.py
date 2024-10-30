# 삼각형 변의 조건: 가장 긴 변 < 나머지 두 변의 합
# i < i +1, i+ 2
# N -2
import sys
N = int(sys.stdin.readline())
lenght = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)
answer = -1

for i in range(N-2):
    if lenght[i] < lenght[i+1] + lenght[i+2]:
        answer = lenght[i] + lenght[i+1] + lenght[i+2]
        break
print(answer)
