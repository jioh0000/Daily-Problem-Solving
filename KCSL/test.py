"""
import sys
sys.stdin = open("wormsort.in", "r")
sys.stdout = open("wormsort.out", "w")
"""

N, B = map(int, input().split(" "))
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split(" "))))

lineX = []
lineY = []
for i in range(N):
    lineX.append(arr[i][0] + 1)
    lineY.append(arr[i][1] + 1)

lineX = set(lineX)
lineY = set(lineY)

M = 101
for i in lineX:
    for j in lineY:
        cnt = [0, 0, 0, 0]
        for coor in arr:
            if coor[0] < i and coor[1] > j:
                cnt[0] += 1
            elif coor[0] > i and coor[1] > j:
                cnt[1] += 1
            elif coor[0] < i and coor[1] < j:
                cnt[2] += 1
            elif coor[0] > i and coor[1] < j:
                cnt[3] += 1 

        if max(cnt) < M:
            M = max(cnt)

print(M)