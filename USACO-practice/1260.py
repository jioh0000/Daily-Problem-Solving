N, M, K = map(int, input().split())
adj = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 1

def dfs(start):
    ans = [start]
    stack = [start]
    visited = [False for _ in range(N + 1)]
    visited[start] = True
    while len(stack) > 0:
        now = stack[len(stack) - 1]
        sw = False
        for i in range(1, N + 1):
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
    visited = [False for _ in range(N + 1)]
    visited[start] = True
    begin = 0
    while begin < len(ans):
        now = ans[begin]
        for i in range(1, N + 1):
            if adj[now][i] == True and visited[i] == False:
                ans.append(i)
                visited[i] = True
        begin += 1
    return ans

print(' '.join(map(str, dfs(K))))
print(' '.join(map(str, bfs(K))))


'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''