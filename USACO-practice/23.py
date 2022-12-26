import sys
N, Q = map(int, sys.stdin.readline().split(" "))
arr1 = [0]# arr1[i] : 1~i까지 1의 개수
arr2 = [0]
arr3 = [0]
for i in range(N):
    a = int(sys.stdin.readline())
    arr1.append(arr1[-1] + a==1)
    arr2.append(arr2[-1] + a==2)
    arr3.append(arr3[-1] + a==3)

for _ in range(Q):
    a, b = map(int, sys.stdin.readline().split(" "))
    print(arr1[b] - arr1[a-1], arr2[b] - arr2[a-1], arr3[b] - arr3[a-1])