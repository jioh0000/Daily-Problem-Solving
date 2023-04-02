import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
Q = int(sys.stdin.readline())
arr0 = []
for i in range(N):
    arr0.append(arr[i])

arr.sort()
ans = 0
for i in range(N):
    ans += (i + 1) * arr[i]

for _ in range(Q):
    i, j = map(int, sys.stdin.readline().split())
    x = N - 1
    while x >= 0:
        if arr[x] == arr0[i - 1]:
            break
        x -= 1
    y = N - 1
    while y > 0:
        if arr[y - 1] <= j:
            break
        y -= 1

    if x < y:
        print(ans - sum(arr[(x + 1):y]) - (x + 1) * arr0[i - 1] + y * j)
    if x == y:
        print(ans - (arr[x] - j) * (y + 1))
    if y < x:
        print(ans + sum(arr[y:x]) - (x + 1) * arr0[i - 1] + (y + 1) * j)



# 1 2 4 6 10 - > 1 * 1 + 2 * 2 + 4 * 3 + 6 * 4 + 10 * 5 = 91
# 4 7 -> x = 1, y = 4
# 1 4 6 7 10 -> 91 - (4 + 6) - 2 * 2 + 7 * 4 = 105

# 1 2 4 6 10
# 1 1 2 4 6 -> 91 + (2+4+6) - 10 * 5 + 1 * 2