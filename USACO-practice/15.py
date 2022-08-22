"""
5
8 5
2 1 7 4
4 2
5 4
2 2 5 4
3 3
1 8
0 3 1 6
1 5
8 1
3 0 6 1
5 1
8 10
4 5 7 8
8 5
"""
x1,y1,x2,y2,h,l,movableX,movableY = 0,0,0,0,0,0,0,0
N = int(input())
arr = []
for i in range(N):
    arr.append([list(map(int, input().split())) for _ in range(3)])

for i in range(N):
    answer = -1
    diffN = arr[i][0][1] - arr[i][1][3]
    diffS = arr[i][1][1]
    diffE = arr[i][0][0] - arr[i][1][2]
    diffW = arr[i][1][0]
    a = max(diffN+diffE, diffE+diffS, diffS+diffW, diffW+diffN)

    if a == diffN + diffE:
        x1, y1, x2, y2 = arr[i][0][0]-arr[i][2][0], arr[i][0][1]-arr[i][2][1], arr[i][0][0], arr[i][0][1]
        h = min(arr[i][1][3], y2) - max(arr[i][1][1], y1)
        l = min(arr[i][1][2], x2) - max(arr[i][1][0], x1)
        movableX = diffW
        movableY = diffS
    elif a == diffE + diffS:
        x1, y1, x2, y2 = arr[i][0][0]-arr[i][2][0], 0, arr[i][0][0], arr[i][2][1]
        h = min(arr[i][1][3], y2) - max(arr[i][1][1], y1)
        l = min(arr[i][1][2], x2) - max(arr[i][1][0], x1)
        movableX = diffW
        movableY = diffN
    elif a == diffS + diffW:
        x1, y1, x2, y2 = 0, 0, arr[i][2][0], arr[i][2][1]
        h = min(arr[i][1][3], y2) - max(arr[i][1][1], y1)
        l = min(arr[i][1][2], x2) - max(arr[i][1][0], x1)
        movableX = diffE
        movableY = diffN
    elif a == diffW + diffN:
        x1, y1, x2, y2 = 0, arr[i][0][1]-arr[i][2][1], arr[i][2][0], arr[i][0][1]
        h = min(arr[i][1][3], y2) - max(arr[i][1][1], y1)
        l = min(arr[i][1][2], x2) - max(arr[i][1][0], x1)
        movableX = diffE
        movableY = diffS
    
    if h > movableY and l > movableX:
        print(answer)
    elif h <= movableY and l > movableX:
        print(h)
    elif h > movableY and l <= movableX:
        print(l)
    else:
        print(min(h,l))