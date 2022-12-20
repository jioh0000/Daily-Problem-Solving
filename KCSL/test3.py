T = int(input())
T1 = []
T2 = []
ans = []
for i in range(T):
    T1.append(list(map(int, input().split(" "))))
    T2.append(input())
    ans.append("." * T1[i][0])


for k in range(T):
    Gcur = -100005
    for i in range(0, T1[k][0]):
        d = T1[k][1]
        if T2[k][i] == 'G':
            if i - Gcur > d:
                Gcur = i + d
                if Gcur >= len(T2[k]) and T2[k][T1[k][0]-1] == "H":
                    Gcur = len(T2[k]) - 2
                elif Gcur >= len(T2[k]) and T2[k][T1[k][0]-1] == "G":
                    Gcur = len(T2[k]) - 1
                a = list(ans[k])
                a[Gcur] = "G"
                a = ''.join(a)
                ans[k] = a

for k in range(T):
    Hcur = -10005
    for i in range(0, T1[k][0]):
        d = T1[k][1]
        if T2[k][i] == 'H':
            if i - Hcur > d:
                Hcur = i + d
                if Hcur >= len(T2[k]) and T2[k][T1[k][0]-1] == "G":
                    Hcur = len(T2[k]) - 2
                elif Hcur >= len(T2[k]) and T2[k][T1[k][0]-1] == "H":
                    Hcur = len(T2[k]) - 1
                a = list(ans[k])
                a[Hcur] = "H"
                a = ''.join(a)
                ans[k] = a

dot = []
for i in ans:
    count = 0
    for j in i:
        if j == '.':
            count +=1
    dot.append(count)

ans2 = []
for i in range(0, len(dot)):
    ans2.append(T1[i][0] - dot[i])

for i in range(0, T):
    print(ans2[i])
    print(ans[i])