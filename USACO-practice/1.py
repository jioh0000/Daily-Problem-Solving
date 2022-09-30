N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
answer = 0

for i in range(0, len(x)-1):
    for j in range(i, len(x)-1):
        a = (x[i]-x[j+1])**2+ (y[i]-y[j+1])**2
        if a>answer:
            answer = a
   
print(answer)