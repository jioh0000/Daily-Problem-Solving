class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        if self.x +self.y == other.x + other.y:
            return self.x < self.y
        return self.x + self.y < other.x + other.y


x = []; y = []
points = []
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    x.append(a); y.append(b)
    points.append(Pair(a, b))

points.sort()
for i in range(M):
    print([points[i].x, points[i].y])