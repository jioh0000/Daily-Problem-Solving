import sys
from itertools import combinations
ch = [False for _ in range(2 ** 18)]
C, N = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    s = sys.stdin.readline()
    a = 0
    for i in range(C):
        a *= 2
        if s[i] == 'H':
            a += 1
    arr.append(a)
    ch[a] = True

L = 2 ** C - 1


for i in range(len(arr)):
    # 10100 ^ 00010 = 10110
    # 00100/11100/10000/10110/10101 -> C = 1

    for n in range(C):
        if n == 0:
            if ch[L ^ arr[i]] == True :
                print(C)
                break
        for x in combinations(range(N), n):
            M = 0
            for y in list(x):
                M += 2 ** y
            if ch[L ^ (arr[i] ^ M)] == True:
                print(C - n)
                break

