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
    num = []
    for j in range(N + 1):
        if pf_r[j] == i:
            num.append(j)
    if len(num) > 0:
        if num[-1] - num[0] > ans:
            ans = num[-1] - num[0]

print(ans)

#   3 5 1 6 2 14 10
# 0 3 8 9 15 17 31 41
# pf_r: 0 3 1 2 1 3 3 6