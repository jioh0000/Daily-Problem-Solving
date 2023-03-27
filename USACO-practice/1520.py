import sys


N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().split()))

cnt = [[-1] * M for _ in range(N)]
stack = []
    
def dfs(now, end):
    cnt[now[0]][now[1]] = 0
    if now[0] == end[0] and now[1] == end[1]:
        return 1
    for i in [[now[0] + 1, now[1]],[now[0], now[1] + 1],[now[0] - 1, now[1]],[now[0], now[1] - 1]]:
        if (i[0] >= 0 and i[0] <= N - 1 and i[1] >= 0 and i[1] <= M - 1) and arr[i[0]][i[1]] < arr[now[0]][now[1]]:
            cnt[now[0]][now[1]] += dfs(i, end)
    return cnt[now[0]][now[1]]

print(dfs([0,0], [N-1,M-1]))