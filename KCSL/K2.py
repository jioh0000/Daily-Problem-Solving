N = list(map(int,input().split(',')))
count = 0


while(len(N) != 0):
    if min(N) == 0:
        remove = 0
        for i in range(len(N)-1, -1, -1):
            if N[i] == 0:
                remove = 1
            if remove == 1:
                N.pop(i)
    else:
        max = N[0]
        for i in range(0, len(N)):
            if N[i] >= max:
                max = N[i]
                index = i
        if N[index]%2 == 0:
            N[index] -= 2
        else:
            N[index] -= 1
    count += 1

print(count)
  
