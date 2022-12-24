N, Q = map(int, input().split(" "))
arr = [0]
arr1 = [0]# arr1[i] : 1~i까지 1의 개수
arr2 = [0]
arr3 = [0]
for i in range(N):
    a = int(input())
    arr.append(a)
    
    if a == 1:
        arr1.append(arr1[i] + 1)
        arr2.append(arr2[i] + 0)
        arr3.append(arr3[i] + 0)
    elif a == 2:
        arr1.append(arr1[i] + 0)
        arr2.append(arr2[i] + 1)
        arr3.append(arr3[i] + 0)
    elif a == 3:
        arr1.append(arr1[i] + 0)
        arr2.append(arr2[i] + 0)
        arr3.append(arr3[i] + 1)

for _ in range(Q):
    a, b = map(int, input().split(" "))
    print(arr1[b] - arr1[a-1], arr2[b] - arr2[a-1], arr3[b] - arr3[a-1])