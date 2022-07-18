n, x = map(int,input().split())
nums = list(map(int,input().split()))

for i in nums:
    if x-i in nums:
        print(nums.index(i)+1, nums.index(x-i)+1)
        break