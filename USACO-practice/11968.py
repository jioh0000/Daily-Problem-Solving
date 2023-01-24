import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

brr = []
j = 0
for i in range(1,N * 2 + 1):
    if j < N and i == arr[j]:
        j += 1
    else:
        brr.append(i)

j = 0; cnt = 0
for i in range(N):
    while j < N and arr[i] > brr[j]:
        j+=1
    if j == N:# I cannot beat arr[i]
        break
    else:
        cnt += 1
        j += 1

print(cnt)






'''
1 2 3 4 5 6

1 4 6
2 3 5
'''