T = int(input())
for _ in range(T):
    input()
    N, M = map(int, input().split(" "))
    arr = []
    for _ in range(M):
        arr.append(list(map(str, input().split(" "))))

    # 1. answers are consistent?
    cnt = 0
    for i in range(M-1):
        for j in range(i+1,M):
            if arr[i][1] != arr[j][1] and arr[i][0] == arr[j][0]:
                cnt+=1
    if cnt > 0:
        print("LIE")
    elif N == 1:
        print("OK")
    elif N == 2:
        ans00 = -1
        ans01 = -1
        ans10 = -1
        ans11 = -1
        for i in range(M):
            if arr[i][0] == "00":
                ans00 = int(arr[i][1])
            if arr[i][0] == "01":
                ans01 = int(arr[i][1])
            if arr[i][0] == "10":
                ans10 = int(arr[i][1])
            if arr[i][0] == "11":
                ans11 = int(arr[i][1])
        if ans00 == -1 or ans01 == -1 or ans10 == -1 or ans11 == -1:
            print("OK")
        elif ans00 + ans01 + ans10 + ans11 == 2 and ans01 == ans10:
            print("LIE")
        else:
            print("OK")
    elif M <= 2:
        print("OK")
    else:
        print("OK")
