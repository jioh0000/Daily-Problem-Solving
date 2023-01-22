import sys

N, K = map(int, sys.stdin.readline().split(" "))
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

ans = 0

num = []
j = 0
for i in range(N):
    num.append(0)
    while j < N and arr[j] <= arr[i] + K:
        j += 1 
    num[i] = j - i
    # two pointer approach

suffix_max = [0]
for i in range(N - 1, -1, -1):
    suffix_max.insert(0, max(suffix_max[0], num[i]))

ans = 0
for i in range(N):
    if ans < num[i] + suffix_max[i + num[i]]:
        ans = num[i] + suffix_max[i + num[i]]

print(ans)