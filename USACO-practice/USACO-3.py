import sys

N, M = map(int, sys.stdin.readline().split())
mrr = []
for _ in range(M):
    c, r, d, s = map(int, sys.stdin.readline().split())
    mrr.append([c,r,d,s])
arr = list(map(int, sys.stdin.readline().split()))
arr[0] = 0
ans = [-1] * N
ans[0] = 0

query = [[1,0]]
i = 0
while i < len(query):
    nowPort = query[i][0]
    nowTime = query[i][1]
    for j in range(M):
        if mrr[j][0] == nowPort and nowTime + arr[nowPort - 1] <= mrr[j][1]:
            if ans[mrr[j][2] - 1] == -1 or ans[mrr[j][2] - 1] > mrr[j][3]:
                ans[mrr[j][2] - 1] = mrr[j][3]
                query.append([mrr[j][2], mrr[j][3]])
    i += 1

for i in ans:
    print(i)