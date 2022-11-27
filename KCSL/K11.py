N, K = map(int, input().split())
N *= 10 ** (K - (len(str(N))%K))

count = 0
N = str(N)
for i in range(len(N)//K):
    count += int(N[K*i:K*(i+1)])

print(count)
