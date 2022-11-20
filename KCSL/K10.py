a, b, k = map(int, input().split(', '))
ans = []
num = 99999
maxN, maxM = 0, 0
while num >= 1:
    num /= a
    maxN += 1
num = 99999
while num >= 1:
    num /= b
    maxM += 1

for i in range(maxN):
    for j in range(maxM):
        num = (a**i)*(b**j)
        if num <= 99999 and num >= 10000:
            ans.append(str(num))

cnt = 0
for i in ans:
    cnt += i.count(str(k))

print(cnt)