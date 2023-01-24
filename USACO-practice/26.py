import sys
'''
6 15
4 3 8 4 7 3
'''

N, X = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

cnt = 0
while X >= 0 and cnt != N:
    X -= arr[cnt]
    cnt += 1

print(cnt - 1)
