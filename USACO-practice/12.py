cows = list(map(int,input().split()))
maximum = max(cows[1] - cows[0], cows[2] - cows[1]) - 1

if cows[1] - cows[0] == 2 or cows[2] - cows[1] == 2:
    minimum = 1
elif cows[1] - cows[0] == 1 and cows[2] - cows[1] == 1:
    minimum = 0
else:
    minimum = 2

print(minimum)
print(maximum)