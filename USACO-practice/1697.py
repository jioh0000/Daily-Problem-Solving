import sys

x, y = map(int, sys.stdin.readline().split())

def bfs(start, end):
    ans = [start]
    dist = [-1 for _ in range(200001)]
    dist[start] = 0
    begin = 0
    while dist[end] == -1:
        now = ans[begin]
        for i in [now - 1, now + 1, now * 2]:
            if i < 200001 and 0 <= i and dist[i] == -1:
                ans.append(i)
                dist[i] = dist[now] + 1
        begin += 1
    return dist[end]

print(bfs(x, y))