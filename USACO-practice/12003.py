import sys

N, K = map(int, sys.stdin.readline().split(" "))
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

p

index = 0
num = []
for i in range(N):
    num[i].append(num[i - 1] - 1)
    while index < N and arr[index] - arr[i] <= K:
        num[i] = index - i + 1
        index += 1

suffix_max = [] # suffix_max[i] : max(num[i],num[i + 1],...,num[N - 1])
  
ans = 0
for i in range(N):
    ans = num[i] + suffix_max[index[i]] 


# num[i] : length of longest interval begins with i

# suffix_max[i] : max(num[i],num[i + 1],...,num[N - 1])

# ans : sum of two longest interval length, not overlaps each other

'''
8 4
1 5
2 5
3 4
4 3
5 2
6 1
20 2
21 2
'''
