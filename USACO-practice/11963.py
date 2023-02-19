import sys

N = int(sys.stdin.readline())
arr1 = []; arr2 = []
for _ in range(N//2):
    arr1.append(int(sys.stdin.readline()))
for _ in range(N//2):
    arr2.append(int(sys.stdin.readline()))
arr1.sort()
arr2.sort()

brr = []; brr1 = []; brr2 = []
j = 0
k = 0
for i in range(1,N * 2 + 1):
    if j < N//2 and (i == arr1[j]):
        j += 1
    elif k < N//2 and (i == arr2[k]):
        k += 1
    else:
        brr.append(i)

brr1 = brr[:N//2]
brr2 = brr[N//2:]

cnt = 0; l = 0
for i in range(N//2):
    while l < N//2 and arr1[i] > brr2[l]:
        l += 1
    if l == N//2:
        break
    cnt += 1
    l += 1

brr1.sort(reverse=True)
arr2.sort(reverse=True)
l = 0
for i in range(N//2):
    while l < N//2 and arr2[i] < brr1[l]:
        l += 1
    if l == N//2:
        break
    cnt += 1
    l += 1

print(cnt)

