"""
4
bird 2 flies eatsworms
cow 4 eatsgrass isawesome makesmilk goesmoo
sheep 1 eatsgrass
goat 2 makesmilk eatsgrass """

N = int(input())
charic = []
overlapped = 0
for i in range(N):
    inp = list(map(str, input().split()))
    moment = []
    for j in range(2, len(inp)):
        moment.append(inp[j])
    charic.append(moment)
"""
[['flies', 'eatsworms'], ['eatsgrass', 'isawesome', 'makesmilk', 'goesmoo'], ['eatsgrass'], ['makesmilk', 'eatsgrass']]
"""
for i in range(0, len(charic) - 1):
    for j in range(i+1, len(charic)):
        add = []
        add.extend(charic[i])
        add.extend(charic[j])
        if (len(add) - len(set(add))) > overlapped:
            overlapped = len(add) - len(set(add))

print(overlapped + 1)
