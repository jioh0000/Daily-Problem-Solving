N, K = map(int, input().split())
diamonds = []
a = 0
count = 0

for _ in range(N):
    diamonds.append(int(input()))

for i in range(a,N-1):
    for j in range(i+1,N):
        if abs(diamonds[i] - diamonds[j]) == K:
           diamonds[i] = 1/2
           diamonds[j] = 1/2
           count += 2
print(count)