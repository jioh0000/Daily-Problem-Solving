N = 4 #can be changed
count = N-1
array = [1,2,4,3] #can be changed

for i in range(N-2,-1, -1):
    if array[i] < array[i+1]:
        count = i
    else:
        break

print(count)