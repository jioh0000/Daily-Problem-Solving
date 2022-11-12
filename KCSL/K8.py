N, K = map(str, input().split(', '))
arr = N.split('/')

if K[0] == '/':
    index = 0
    count = 0
    for i in N:  
        if i == '/':
            count += 1
        if count == 3:
            break
        index += 1
    print(N[:index] + K)
elif K[:4] == "http":
    print(K + "default.htm")
elif K[:2] == "..":
    dotdotNum = K.count('..')
    count = 0
    for i in range(len(N)-1, -1, -1):
        if N[i] == '/':
            count += 1
        if count == dotdotNum + 1:
            index = i
            break
    print(N[:index+1] + K[3*dotdotNum:])
else:
    print(N.replace(arr[-1],K),end="")
    if K[-1] == '/':
        print("default.htm")