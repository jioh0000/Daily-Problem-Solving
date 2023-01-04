import sys

N, K = map(int, sys.stdin.readline().split(" "))
# Find sequence p such that p has prefix sum sequence which is identical to arr
arr = [0]*(N + 10)
brr = [0]*(N + 10)

for _ in range(K):
    a, b = map(int, sys.stdin.readline().split(" "))
    brr[a] += 1
    brr[b+1] -= 1

for i in range(1,N+1):
    arr[i] = arr[i - 1] + brr[i]

print(sorted(arr[0:N])[(N - 1)//2])