import sys

N,C = map(int, sys.stdin.readline().split())
nrr = []
for _ in range(N):
    nrr.append(int(sys.stdin.readline()))
nrr.sort()

def f(pivot):
    # True if ans >= pivot
    cur = -pivot
    cnt = 0
    for i in nrr:
        if i - cur >= pivot:
            cur = i
            cnt += 1
    
    if C > cnt:
        return False
    elif C <= cnt:
        return True
        


begin = 1
end = 1000000000
while begin < end:
    pivot = (begin + end + 1) // 2
    if f(pivot) == True:
        begin = pivot
    else:
        end = pivot - 1

print(begin)


