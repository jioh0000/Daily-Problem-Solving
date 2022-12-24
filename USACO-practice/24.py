import sys
N = int(sys.stdin.readline())
arr = [0]
raa = [0]
for _ in range(N):
    a = int(sys.stdin.readline())
    arr.append(a)
    raa.append(raa[-1] + a)

ans = 0
print(raa)
for i in range(1,N+1):
    for j in range(i,N+1):
        a = raa[j] - raa[i - 1] 
        if a%7==0 and j-i+1 > ans:
            ans = j-i+1

print(ans)