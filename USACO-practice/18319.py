import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)

ans = []
for i in range(1, arr[0] + 1):
    brr = []
    for j in range(len(arr)):
        n = 1
        while arr[j] - i * n > 0:
            brr.append(i)
            n += 1
        brr.append(arr[j] - i * (n - 1))
    brr.sort(reverse = True)
    ans.append(sum(brr[K//2:K]))

print(max(ans))

