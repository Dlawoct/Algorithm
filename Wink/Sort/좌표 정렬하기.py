import sys
input = sys.stdin.readline

N = int(input())
coor = [list(map(int, input().split())) for i in range(N)]

# for i in range(N):  #0, 1, 2, 3, 4
#     for j in range(0, N-i-1):   #(0,4), (0,3), (0,2).....
#         if coor[j][0] > coor[j+1][0]:
#             coor[j][0], coor[j+1][0] = coor[j+1][0], coor[j][0]
#             coor[j][1], coor[j+1][1] = coor[j+1][1], coor[j][1]
#         elif coor[j][0] == coor[j+1][0]:
#             if coor[j][1] > coor[j+1][1]:
#                 coor[j][0], coor[j+1][0] = coor[j+1][0], coor[j][0]
#                 coor[j][1], coor[j+1][1] = coor[j+1][1], coor[j][1]

# for k in range(N):
#     print(coor[k][0], coor[k][1])

coor.sort(key=lambda x: (x[0], x[1]))

for x, y in coor:
    print(x,y)