def mult():
    for i in range(len(a)):
        if a[i] == '*':
            a[i] = a[i-1]
            a[i-1] = '*'
            si(i)
            break

def plusminus():
    for i in range(len(a)):
        if a[i] == '+':
            a[i] = a[i-1]
            a[i-1] = '+'
            si(i)
            break
        elif a[i] == '-':
            a[i] = a[i-1]
            a[i-1] = '-'
            si(i)
            break

def si(i):
    tmp = ''.join(a[i-1 : i+2])
    a.insert(i+2, tmp)
    del a[i-1:i+2]
    




for _ in range(5):
    a = list(map(str, input().strip()))
    operNum = (len(a)-1)//2
    multNum = a.count('*')
    pmNum = operNum - multNum

    for _ in range(multNum):
        mult()

    print(pmNum)
    for _ in range(pmNum):
        print(a)
        plusminus()

    print(''.join(a))
