import sys

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        if self.y == other.y:
            return self.x > other.x
        return self.y > other.y

N, M, R = map(int, sys.stdin.readline().split(" "))
arr = []
brr = []
crr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    brr.append(Pair(a,b))
for _ in range(R):
    crr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)
brr.sort()
crr.sort(reverse=True)

ps_brr = [0]# <- j
ps_crr = [0]

ans = -1
j = 0
cnt = 0
for i in range(R):
    ps_crr.append(ps_crr[-1] + crr[i])
for i in range(N):
    num = arr[i]
    
    while j < M:
        if num > brr[j].x:
            cnt += brr[j].x * brr[j].y
            num -= brr[j].x
            brr[j].x = 0
            j+=1
        else:
            cnt += num * brr[j].y
            brr[j].x -= num
            break
        
    # cnt : ith cow까지는 milk를 팔고, 그 수익금
    # N - i cows는 rent.
    if N - i - 1 < R:
        if cnt + ps_crr[N - i - 1] > ans:
            ans = cnt + ps_crr[N - i - 1]
    else:
        if cnt + ps_crr[R] > ans:
            ans = cnt + ps_crr[R]

print(ans)