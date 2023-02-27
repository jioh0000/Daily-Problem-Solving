import sys

T = int(sys.stdin.readline())
for _ in range(T):
    a = sys.stdin.readline()
    N, tc, tm = map(int, sys.stdin.readline().split())
    arr = []
    for i in range(N):
        a, b, c = map(int, sys.stdin.readline().split())
        arr.append([a,b,c])
    
    brr = []

    for A in range(tc):
        for B in range(tm):
            cnt = 0
            for i in range(N):
                if (tc - A) * arr[i][0] + (tm - B) * arr[i][1] <= arr[i][2]:
                    cnt += 1
            if cnt == N:
                brr.append(A + B)
    
    print(min(brr))

    