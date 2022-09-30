X, Y, M = map(int, input().split())
a = M//X
answer = 0
sum = 0

for i in range(1,a+1):
    sum = X*i
    while sum < M:
        sum += Y
    if (sum-Y) > answer:
        answer = (sum-Y)

print(answer)