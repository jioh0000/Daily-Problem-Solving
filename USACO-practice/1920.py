import sys

N = int(sys.stdin.readline())
nrr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
mrr = list(map(int, sys.stdin.readline().split()))
nrr.sort()

def f(pivot, i):
    if nrr[pivot] < mrr[i]:
        return False
    elif nrr[pivot] >= mrr[i]:
        return True

for i in range(M):
    begin = 0
    end = N - 1
    while begin < end:
        pivot = (begin + end) // 2
        if f(pivot, i) == True:
            end = pivot
        else:
            begin = pivot + 1
    
    if mrr[i] == nrr[begin]:
        print(1)
    else:
        print(0)
