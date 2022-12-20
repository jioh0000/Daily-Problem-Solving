"""
id: jopark
lang: python 3
task: Cow_College
"""

N = int(input())
arr = list(map(int, input().split(" ")))
arr2 = []
arr.sort()
cnt = len(arr)
prev = arr[0]
 
 # 1 4 6 6

for i in range(0, len(arr)):
    arr2.append([arr[i] * cnt, arr[i]])
    cnt -= 1

ans = [-1, -1]

for i in arr2:
    if i[0] > ans[0]:
        ans = i
    elif i[0] == ans[0]:
        if i[1] < ans[1]:
            ans = i

print("%d %d" %(ans[0], ans[1]))