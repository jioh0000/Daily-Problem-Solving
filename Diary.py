"""
N = int(input())
mommu = []
kee = []

for _ in range(N):
    a, b = map(int, input().split())
    mommu.append(a)
    kee.append(b)

for i in range(0,N):
    ranking = 1
    for j in range(0,N):
        if mommu[i] < mommu[j] and kee[i] < kee[j]:
            ranking += 1
    print(ranking, end=" ")
"""

N = int(input())
count = 0
sixsixsix = 666

while N is not count:
    if "666" in str(sixsixsix):
        count += 1
    sixsixsix += 1

print(sixsixsix-1)