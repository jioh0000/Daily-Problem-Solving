arr = list(map(int, input().split(",")))
brr = []

for i in arr:
    temp = i
    a = []
    while temp>1:
        a.insert(0,str(temp%2))
        temp = temp // 2
    if i != 0:
        a.insert(0,'1')
    brr.append(a)

for i in range(len(brr)):
    if len(brr[i]) == 2:
        brr[i].insert(0,'0')
    elif len(brr[i]) == 1:
        for _ in range(2):
            brr[i].insert(0,'0')
    elif len(brr[i]) == 0:
        brr[i].append('000')
    
    brr[i] = ''.join(brr[i])

crr = []
for i in brr:
    a = ['-'] * 3
    for j in range(len(i)):
        if i[j] == '1' and j == 0:
            a[j] = 'r'
        elif i[j] == '1' and j == 1:
            a[j] = 'w'
        elif i[j] == '1' and j == 2:
            a[j] = 'x'
    crr.append(''.join(a))

print("%s %s %s and %s %s %s" %(brr[0], brr[1], brr[2], crr[0], crr[1], crr[2]))