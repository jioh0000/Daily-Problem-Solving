import sys

G, N = map(int, sys.stdin.readline().split())
grr = []
for _ in range(G):
    x, y, t = map(int, sys.stdin.readline().split())
    grr.append([x,y,t])
nrr = []
for _ in range(N):
    x, y, t = map(int, sys.stdin.readline().split())
    nrr.append([x,y,t])

cnt = 0
for i in range(N):
    innocent = False
    for j in range(G):
        time = (abs(nrr[i][2] - grr[j][2])) ** 2
        distance = (nrr[i][0] - grr[j][0]) ** 2 + (nrr[i][1] - grr[j][1]) ** 2
        if time < distance:
            innocent = True
    
    if(innocent == False):
        cnt += 1

print(cnt)