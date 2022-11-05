"""
5 3
1
6
4
3
1
"""

N, K = map(int, input().split(' '))
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()

count = 0
for i in range(len(arr)-1):
    if arr[i+1] - arr[i] <= K:
        count += 2
        arr[i+1] -= 1000
        arr[i] -= 1000

print(count)