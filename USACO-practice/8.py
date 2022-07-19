n = int(input())
char = input()
k = ''

for i in range(n):
    k += char[i]
    if n >= len(k)*2:
        if char[i+1 : i+len(k)+1] in k:
            print(len(k))
            break
    else:
        if char[i+1 :] in k:
            print(len(k))
            break