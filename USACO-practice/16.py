N = int(input())
L = []
G = []
count = 0
for i in range(N):
    a, b = map(str, input().split())
    if a == 'G':
        G.append(int(b))
    elif a == 'L':
        L.append(int(b))

L.sort()
G.sort()


while(G[-1] > L[0]):
    if len(G) == 1 or len(L) == 1:
        count += 1
        break
    c = G[-1] - G[-2]
    d = L[1] - L[0]

    if c>d:
        del G[-1]
    elif c<=d:
        del L[0]
    count += 1

print(count)