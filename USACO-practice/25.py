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