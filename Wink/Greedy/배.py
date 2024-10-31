import sys

N = int(sys.stdin.readline())
crain = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
M = int(sys.stdin.readline())
box = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
cnt = 0

# while len(box) > 0:
#     for i in range(N): # 9 8 6
#         for j in range(len(box)): # 7 5 4 2 2
#             if crain[i] >= box[j]:
#                 del box[j]
#                 break
#             else:
#                 continue
#     cnt += 1
# print(cnt)

if crain[0] < box[0]:
    print(-1)
else:
    while len(box) > 0 :
        for i in crain:
            if box and i < box[-1]: # 박스가 남아있지만 박스들 중 가장 가벼운 박스를 못들면 생략
                continue
            for j in box:
                if i >= j:
                    box.remove(j)
                    break
        cnt +=1
    print(cnt)