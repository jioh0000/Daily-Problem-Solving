N = list(map(str, input().split(' ')))
totalNum = len(N)
Lword = []

c = -1
for i in N:
    if len(i) > c:
        c = len(i)
        Lword.clear()
        Lword.append(i)
    elif len(i) == c:
        Lword.append(i)

s = ''.join(N)
arr = list(s)

c = -1
for i in range(ord('A'), ord('Z')+1):
    char = chr(i)
    count = arr.count(char)
    if count > c:
        c = count
        frqLetter = char

c = -1
for i in set(N):
    count = N.count(i)
    if count > c and i != 'THE':
        c = count
        frqWord = i


print(totalNum)
print(','.join(Lword))
print(len(set(arr)))
print(frqLetter)
print(frqWord)
