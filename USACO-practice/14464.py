import sys

C, N = map(int, sys.stdin.readline())
arr = []; brr = []
for _ in range(C):
    arr.append(int(sys.stdin.readline()))
for _ in range(N):
    brr.append(list(map(int, sys.stdin.readline().split())))