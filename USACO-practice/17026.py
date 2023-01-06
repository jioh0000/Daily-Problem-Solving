import sys

class Pair:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
    def __lt__(self, other):
        if self.x1 == other.x1:
            return self.x2 > other.x2
        return self.x1 < other.x1

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split(" "))
    x1 = x - y
    x2 = x + y
    arr.append(Pair(x1, x2))

arr.sort()
cnt = N
prefix_max2 = [arr[0].x2]
for i in range(1, N):
    if prefix_max2[-1] >= arr[i].x2:
        cnt -= 1
    prefix_max2.append(max(prefix_max2[-1], arr[i].x2))

print(cnt)