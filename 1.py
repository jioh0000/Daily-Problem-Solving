import sys

N = int(sys.stdin.readline())
s = input()
arr = list(map(int, sys.stdin.readline().split()))

indexG = s.find('G'); is_G_leader = True
indexH = s.find('H'); is_H_leader = True

for i in range(arr[indexG], N):
    if s[i] == 'G':
        is_G_leader = False
for i in range(arr[indexH], N):
    if s[i] == 'H':
        is_H_leader = False

ans = 0
if is_G_leader and is_H_leader:
    ans = 1 

if is_H_leader:
    for i in range(indexH - 1, -1, -1):
        if arr[i] - 1 >= indexH:
            if i != indexG or is_G_leader == False:
                ans += 1

if is_G_leader:
    for i in range(indexG - 1, -1, -1):
        if arr[i] - 1 >= indexG:
            if i != indexH or is_H_leader == False:
                ans += 1

print(ans)

'''
Leader Type
1. 자신의 breed를 모두 포함 -> 최대 breed별 하나.
2. 상대 leader를 포함 -> 둘다 여기에 속할수는 없음.

Case1. Type1이 두명

Case2. Type1이 한명, 2가 한명
'''