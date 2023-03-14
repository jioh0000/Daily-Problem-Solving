N = int(input())
nrr = list(map(int, input().split()))
M = int(input())
mrr = list(map(int, input().split()))
nrr.sort()
nrr2 = []
for i in range(N):
    nrr2.append(nrr[N - i - 1])
arr = []

def f(pivot, i):
    if nrr[pivot] < mrr[i]:
        return False
    else:
        return True
    
def rf(pivot, i):
    if nrr2[pivot] <= mrr[i]:
        return True
    else:
        return False

for i in range(M):
    begin = 0
    end = N - 1
    while begin < end:
        pivot = (begin + end) // 2
        if f(pivot, i) == True:
            end = pivot
        else:
            begin = pivot + 1
    a = begin

    begin = 0
    end = N - 1
    while begin < end:
        pivot = (begin + end) // 2
        if rf(pivot, i) == True:
            end = pivot
        else:
            begin = pivot + 1
    b = begin
    print(N - b - a, end=" ")




"""
10 10 10 7 6 3 3 2 -10 -10
find 10
b = 0 e = 9
b = 0 e = 3 p = 1
b = 0 e = 0
find 9 
b = 0 e = 9
b = 0 e = 3 p = 1
b = 1 e = 2 p = 1
b = 1 e = 2
"""
