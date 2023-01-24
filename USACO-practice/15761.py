import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)

cnt = 0
for i in range(N):
    if arr[i] >= i:
        cnt += 1

print(cnt)