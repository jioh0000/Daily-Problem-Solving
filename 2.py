import sys

N, M = map(int, sys.stdin.readline().split())
arr = []; brr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
for _ in range(M):
    brr.append(list(map(int, sys.stdin.readline().split())))

ans = []
crr0 = [0] * 101; crr = [0]*101
for i in range(N):
    for j in range(arr[i][0], arr[i][1] + 1):
        crr[j] += arr[i][2]

a = 0
drr = [False] * M
for k in range(pow(2, M)):
    t = k
    for i in range(M):
        drr[i] = (t % 2 == 1)
        t = (int)(t/2)

    for i in range(101):
        crr0[i] = crr[i]
    cost = 0
    for i in range(M):
        if drr[i] == True:
            for j in range(brr[i][0], brr[i][1] + 1):
                crr[j] -= brr[i][2]
            cost += brr[i][3] 
    t = True
    for i in crr:
        if i > 0:
            t = False
    if t:
        ans.append(cost)
    for i in range(101):
        crr[i] = crr0[i]

print(min(ans))
        
'''
10개의 에어컨을 끄거나 키거나
= 1024개의 setting을 확인해보면 된다.
= 그중에 되는 것들중에 최소 금액이 정답.
'''