N = list(input())
a = max(N)
index = N.index(a)

if int(a)%2 == 1:
    N[index] = "0"
else:
    N[index] = str((int(a) + 4) % 10)

if N[0] == '0':
    N.pop(0)

for i in N:
    print(i, end="")
