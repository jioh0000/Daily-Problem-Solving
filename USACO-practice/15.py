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

    if max(diffN+diffE, diffE+diffS, diffS+diffW, diffW+diffN) == diffN+diffE:
        x1, x2, y1, y2 = arr[i][0][0]

print(arr)