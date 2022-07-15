N = int(input())
numbers =  sorted(list(map(int,input().split())))
count = 1

length = len(numbers) - 1
for i in range(length):
    if numbers[i] != numbers[i+1]:
        count += 1

print(count)