import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

j = 0
num = []
for i in range(N):
    num.append(0)
    while j < N and arr[j] <= arr[i] + N - 1:
        j += 1
    num[i] = j - i

minimum = N - max(num)

if arr[N - 2] - arr[0] == N - 2 and arr[N - 1] > arr[N - 2] + 2 :
    minimum = 2
if arr[N - 1] - arr[1] == N - 2 and arr[1] > arr[0] + 2:
    minimum = 2

print(minimum)

r = arr[-1] - arr[0]
maximum = r - min(arr[1] - arr[0], arr[-1] - arr[-2]) - (N - 1) + 1

print(maximum)

'''
1, 10, 11, 20, 23
1~5 4 
2~6 5
3~7 5
4~8 5
5~9 5
6~10 4
7~11 3
8~12 3
9~13 3

1 2 10 11 20 r 19
2 10 11 19 20 r 18
2 3 10 11 19 r 17
3 10 11 18 19 r 16
...
r 4

19 - 4 + 1
'''