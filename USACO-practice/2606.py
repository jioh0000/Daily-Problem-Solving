import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adj = [[0] * (N+1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a][b] = adj[b][a] = 1

def dfs(start):
    stack = [start]
    visited = [False for _ in range(N+1)]
    ans = [start]
    visited[start] = True
    while len(stack) > 0:
        now = stack[-1]
        sw = False
        for i in range(1,N+1):
            if adj[now][i] == True and visited[i] == False:
                ans.append(i)
                stack.append(i)
                visited[i] = True
                sw = True
                break
        if sw == False:
            stack.pop()
    return ans

def bfs(start):
    ans = [start]
    visited = [False for _ in range(N+1)]
    visited[start] = True
    begin = 0
    while begin < len(ans):
        now = ans[begin]
        for i in range(1, N+1):
            if adj[now][i] == True and visited[i] == False:
                ans.append(i)
                visited[i] = True
        begin += 1
    return ans

print(len(bfs(1)) - 1)