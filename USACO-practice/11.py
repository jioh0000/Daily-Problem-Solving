"""
input:
MIAMI FL
DALLAS TX
FLINT MI
CLEMSON SC
BOSTON MA
ORLANDO FL
"""
N = 6
count = 0
array = []

for i in range(N):
    a,b = input().split()
    array.append([a[:2],b])
for i in range(N-1):
    for j in range(i+1,N):
        if array[i][0] == array[j][1] and array[i][1] == array[j][0]:
            count += 1

print(count)