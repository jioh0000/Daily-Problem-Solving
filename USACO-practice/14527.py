import sys

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        if self.y == other.y:
            return self.x > other.x
        return self.y > other.y

N = int(input())
M = 0
arr = []
for _ in range(N):
    a,b = map(int, sys.stdin.readline().split(" "))
    arr.append(Pair(a,b))
arr.sort()

ans = 0
i = 0; j = N - 1
while i <= j:
    now = arr[i].y + arr[j].y
    if ans < now:
        ans = now
    if i == j:
        break
    temp = min(arr[i].x, arr[j].x)
    arr[i].x -= temp
    arr[j].x -= temp
    if arr[i].x == 0:
        i += 1
    if arr[j].x == 0:
        j -= 1
print(ans)

