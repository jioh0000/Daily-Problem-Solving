import sys

K, N = map(int, sys.stdin.readline().split())
krr = []
for _ in range(K):
    krr.append(int(sys.stdin.readline()))
krr.sort()

def f(pivot):
    cnt = 0
    for i in range(K):
        cnt += krr[i] // pivot
    
    if cnt < N:
        return True
    return False


begin = 1
end = krr[-1]
while begin < end:
    pivot = (begin + end + 1) // 2
    if f(pivot) == True:
        end = pivot - 1
    else:
        begin = pivot

print(begin)
