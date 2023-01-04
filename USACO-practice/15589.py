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
    x, y = map(int, sys.stdin.readline().split(" "))
    arr.append(Pair(x, y))

arr.sort()

curX = 0
curY = 0
cnt = 0
index = 0
for i in arr:
    if i.x >= curY:
        cnt += curY-curX
        curX = i.x
        curY = i.y
    elif i.x < curY and i.y > curY:
        curY = i.y
cnt += curY - curX

brr = [0]
pref_maxY = [-1]
for i in range(N):
    # i th pair가 나머지들과 얼마나 겹쳐있는지.
    # left yellow : max(arr[1].y,..., arr[i-1].y) = prefix max
    # right yellow : min(arr[i+1].x,...,arr[n].x) = arr[i + 1].x
    if i == N - 1:
        right = 1e+9 + 1
    else:
        right = arr[i+1].x
    left = pref_maxY[i]
    pref_maxY.append(max(arr[i].y, pref_maxY[i]))

    if right > arr[i].y:
        right = arr[i].y
    if left < arr[i].x:
        left = arr[i].x
    if left >= right:
        right = left

    brr.append(right - left)

cnt -= min(brr)
print(cnt)
print(brr)
