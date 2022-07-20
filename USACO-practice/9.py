a = ['C','O','W','X','X','O','A','B','C']
solutions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
singleAns = 0
doubleAns = 0

for i in solutions:
    if len({a[i[0]], a[i[1]], a[i[2]]}) == 2:
        doubleAns += 1
    elif len({a[i[0]], a[i[1]], a[i[2]]}) == 1:
        doubleAns += 1
        singleAns += 1

print(singleAns)
print(doubleAns)