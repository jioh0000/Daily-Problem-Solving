N = int(input())
G = []
L = []
for i in range(N):
    l, k = map(str, input().split(' '))
    if l == 'G': G.append(int(k))
    else: L.append(int(k))

G.sort(reverse = True)
L.sort()
count = 0
while(max(G) > min(L)):
    if len(G) == 1 or len(L) == 1:
        count += 1
        break
    else:
        if G[1] - G[0] > L[1] - L[0]:
            G.pop(0)
        else:
            L.pop(0)
        count += 1

print(count)