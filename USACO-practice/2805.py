import sys

N, M = map(int, sys.stdin.readline().split())
nrr = list(map(int, sys.stdin.readline().split()))

def f(pivot):
    cnt = 0
    for i in range(N):
        if nrr[i] > pivot:
            cnt += nrr[i] - pivot
    if cnt < M:
        return True
    return False

begin = 0
end = max(nrr)
while begin < end:
    pivot = (1 + begin + end) // 2
    if f(pivot) == True:
        end = pivot - 1
    else:
        begin = pivot

print(begin)