import sys

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split(" "))
    arr.append(Pair(a,b))

arr.sort()

maxY = 0
minY = 1000000001
for i in range(N):
    if arr[i].y > maxY:
        maxY = arr[i].y
    if arr[i].y < minY:
        minY = arr[i].y

onefence = (arr[N-1].x - arr[0].x) * (maxY - minY)

sum1 = [0]
for i in range(N):
    sum1.append()