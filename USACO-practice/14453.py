import sys

N = int(input())
arrH = [0]
arrP = [0]
arrS = [0]

for i in range(N):
    a = str(sys.stdin.readline())
    a.split("\n", 1)
    arrH.append(arrH[-1] + (a[0]=="H"))
    arrP.append(arrP[-1] + (a[0]=="P"))
    arrS.append(arrS[-1] + (a[0]=="S"))

ans = 0
for i in range(1, N):
    # change in i-th game
    # 1~ith/ i+1~Nth game
    a = max([arrH[i], arrP[i], arrS[i]]) + max([arrH[N] - arrH[i], arrP[N] -  arrP[i], arrS[N] - arrS[i]])
    if a > ans:
        ans = a

print(ans)
