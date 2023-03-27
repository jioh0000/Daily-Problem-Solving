import sys

N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(sys.stdin.readline())

def bfs(start, end):
    ans = [start]
    dist = [[-1] * (M) for _ in range(N)]
    dist[start[0]][start[1]] = 0
    begin = 0
    while dist[N-1][M-1] == -1:
        now = ans[begin]
        for i in [[now[0] + 1, now[1]],[now[0], now[1] + 1],[now[0] - 1, now[1]],[now[0], now[1] - 1]]:
            if (i[0] >= 0 and i[0] <= N - 1 and i[1] >= 0 and i[1] <= M - 1) and dist[i[0]][i[1]] == -1 and arr[i[0]][i[1]] == '1':
                ans.append(i)
                dist[i[0]][i[1]] = dist[now[0]][now[1]] + 1
        begin += 1
    return dist[N-1][M-1] + 1


print(bfs([0 ,0], [N - 1, M -1]))
