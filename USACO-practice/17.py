N, K = map(int, input().split())
arr = []
counter = {}
count = 0
"""
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(K-1):
        for k in range(j+1, K):
            arr.append(a[j]*10 + a[k])
print(arr)

arr1 = set(arr)

for i in arr1:
    if arr.count(i) == N:
        count += 1

print(count)
"""