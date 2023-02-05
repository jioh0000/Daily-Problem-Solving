import sys

Q = int(sys.stdin.readline())
arr = []
for _ in range(Q):
    arr.append(list(input()))
ans = []

for i in arr:
    num = 0
    if len(i) <= 2:
        ans.append(-1)
    elif len(i) == 3:
        if i[1] == 'M':
            ans.append(-1)
        else:
            if i[0] == 'O':
                num += 1
            if i[2] == 'M':
                num += 1
            ans.append(num)
    else:
        brr = []
        a = 0
        b = len(i) - 3 + 1
        for j in range(a, b):
            num = len(i) - 3
            if i[j+1] == 'M':
                brr.append(-1)
            else:
                if i[j] == 'O':
                    num += 1
                if i[j+2] == 'M':
                    num += 1
                brr.append(num)

        anss = 105
        for i in brr:
            if i != -1 and i<anss:
                anss = i
        if anss == 105:
            ans.append(-1)
        else:
            ans.append(anss)
            
for i in ans:
    print(i)