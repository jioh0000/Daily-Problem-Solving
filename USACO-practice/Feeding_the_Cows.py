T = int(input())
T1 = []
T2 = []
ans = []
for i in range(T):
    T1.append(list(map(int, input().split(" "))))
    T2.append(input())
    ans.append(["."] * T1[i][0])




for k in range(T):
    N = T1[k][0]
    d = T1[k][1]
    Hcur = -100005
    Gcur = -100005
    for i in range(0, N):
        if T2[k][i] == 'G':
            if i - Gcur > d:
                Gcur = i + d
                if Gcur >= N:
                    Gcur = T1[k][0]-1
                    if ans[k][len(T2[k]) - 1] == ".":
                        ans[k][len(T2[k]) - 1] = "G"
                    else:
                        ans[k][len(T2[k]) - 2] = "G"
                else:
                    if ans[k][Gcur] != ".":
                        Gcur -= 1
                        ans[k][Gcur] = "G"
                    else:
                        ans[k][Gcur] = "G"
        elif T2[k][i] == 'H':
            if i - Hcur > d:
                Hcur = i + d
                if Hcur >= N:
                    Hcur = T1[k][0]-1
                    
                    if ans[k][len(T2[k]) - 1] == ".":
                        ans[k][len(T2[k]) - 1] = "H"
                    else:
                        ans[k][len(T2[k]) - 2] = "H"
                else:
                    if ans[k][Hcur] != ".":
                        Hcur -= 1
                        ans[k][Hcur] = "H"
                    else:
                        ans[k][Hcur] = "H"        

ans2 = [''.join(ans[i]) for i in range(T)]


for i in range(0, T):
    print(T1[i][0] - ans2[i].count('.'))
    print(ans2[i]) 