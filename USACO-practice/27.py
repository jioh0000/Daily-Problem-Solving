import sys

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append(Pair(a, b))
arr.sort()

cnt = 0
i = 0
end = -1
for i in range(N):
    if end <= arr[i].x:
        end = arr[i].y
        cnt += 1
print(cnt)



'''
7
1 2
1 3
4 6
5 6
7 10
8 8
9 9
Solution : 일찍 끝나는 것부터 보기
Solution : (a1, b1), (a2, b2),...,(an, bn)

(ak-1,bk-1)까지 보고 (ak,bk)를 관람
bk-1이후에 시작해서 bk보다 일찍 끝나는 게 있다면?? 걔를 보면 된다.

그렇다면 매순간, 볼수 있는 영화중, 가장 일찍 끝나는 것을 보면 된다. -> greeedy algorithm.
'''