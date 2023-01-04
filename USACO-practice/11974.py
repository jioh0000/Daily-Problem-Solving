import sys
N = int(sys.stdin.readline())
#arr = [0]
pf_r = [0]
for _ in range(N):
    a = int(sys.stdin.readline())
    #arr.append(a)
    pf_r.append((pf_r[-1] + a) % 7)


ans = 0

for i in range(7):
    first = -1
    last = -1
    for j in range(N + 1):
        if pf_r[j] == i and first == -1:
            first = j
        if pf_r[j] == i:
            last = j
    if first != -1 and last - first > ans:
            ans = last - first

print(ans)

#   3 5 1 6 2 14 10
# 0 3 8 9 15 17 31 41
# pf_r: 0 3 1 2 1 3 3 6