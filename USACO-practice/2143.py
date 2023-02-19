import sys

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
brr = list(map(int, sys.stdin.readline().split()))

crr1 = []; crr2 = []
pref_sum = [0]
for i in range(n):
    # arr : 1 3 1 2
    # pre : 0 1 4 5 7
    pref_sum.append(pref_sum[-1] + arr[i])#   1 4 5 7
for i in range(n):
    for j in range(i, n):
        crr1.append(pref_sum[j + 1] - pref_sum[i])
        # arr[i]+arr[i + 1]+...+arr[j] = (arr[0]+...+arr[j]) - (arr[0]+...+arr[i - 1]) = pref_sum[j] - pref_sum[i - 1]

pref_sum = [0]
for i in range(m):
    # arr : 1 3 1 2
    # pre : 0 1 4 5 7
    pref_sum.append(pref_sum[-1] + brr[i])#   1 4 5 7

for i in range(m):
    for j in range(i, m):
        crr2.append(pref_sum[j + 1] - pref_sum[i])

crr1.sort(); crr2.sort()
# Binary search : O(log N)
def find(x, arr):
    begin = 0; end = len(arr) - 1
    while begin < end:
        pivot = (begin + end) // 2
        if x <= arr[pivot]:
            end = pivot
        else:
            begin = pivot + 1
    if arr[begin] != x:
        return -1
    return begin

def rfind(x, arr):
    begin = 0; end = len(arr) - 1
    while begin < end:
        pivot = (begin + end + 1) // 2
        if x < arr[pivot]:
            end = pivot - 1
        else:
            begin = pivot
    if arr[begin] != x:
        return -1
    return begin

cnt = 0
for i in crr1:# O(N^2)
    left = find(T - i, crr2)
    right = rfind(T - i, crr2)
    if left != -1:
        cnt += right - left + 1
    
print(cnt)
'''
6
4
1 3 1 2
5
1 1 1 1 1
'''
