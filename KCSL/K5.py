N, K = map(int, input().split(', '))
sum = 0


for i in range(0, len(str(N)) - K + 1):
    tenth = 10**(K-1)
    count = 0
    temp = 0
    for j in range(K):
        temp += int((str(N))[i+count])*tenth
        count += 1
        tenth /= 10
    sum += temp

print(int(sum))