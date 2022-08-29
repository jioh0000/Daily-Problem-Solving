N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()