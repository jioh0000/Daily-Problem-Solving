import sys

N, K = map(int, sys.stdin.readline().split(" "))
# Find sequence p such that p has prefix sum sequence which is identical to arr
arr = [0]*N

for _ in range(K):
    a, b = map(int, sys.stdin.readline().split(" "))
    for i in range(a-1, b):
        arr[i] += 1

sort(arr)
print(arr[(N-1)/2])