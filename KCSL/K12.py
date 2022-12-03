dic = {'A': [2, 3], 'B': [11, 6], 'C': [7, 11], 'D': [1, 10], 'E': [5, 16], 'F': [5, 6], 'G': [0, 40], 'H': [9, 9], 'I': [7, 0]}
N, K, x, y = map(str, input().split(", "))
cor1 = dic[N]
cor2 = dic[K]
cor3 = [int(x), int(y)]

diffX = cor1[0] - cor2[0]
diffY = cor1[1] - cor2[1]