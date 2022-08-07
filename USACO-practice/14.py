N = 4
log = [-1,-1,-1,1]
log[0] = 0

for i in range(len(log)):
    if log[i] != -1:
        for j in range(log[i]):
            log[i-j-1] = log[i]-j-1

min = log.count(0)
if len(log) >= 3:
    for i in range(len(log)-2):
        if log[i] == 0 and log[i+2] == 0:
            log[i+1] = 0
max = log.count(0)

print(min, max)