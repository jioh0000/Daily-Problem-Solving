import sys

N, M, C = map(int, sys.stdin.readline().split())
nrr = list(map(int, sys.stdin.readline().split()))
nrr.sort()

def f(pivot):
    cnt = 0
    start = -pivot - 1
    human = 0
    for i in nrr:
        # waiting time, capacity
        if i - start > pivot or human >= C:
            # new bus
            cnt += 1
            start = i
            human = 1
        else:
            human += 1
    if cnt <= M: 
        return True
    else:
        return False

begin = 0
end = 100000000
while begin < end:
    pivot = (begin + end) // 2
    if f(pivot) == True:
        end = pivot
    else:
        begin = pivot + 1

print(begin)