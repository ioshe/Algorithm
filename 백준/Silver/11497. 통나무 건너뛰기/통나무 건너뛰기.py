from sys import stdin


t = int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    nums = list(map(int,stdin.readline().split()))
    nums.sort()
    a = max(abs(nums[i] - nums[i-2]) for i in range(2, len(nums), 2))
    b = max(abs(nums[i]-nums[i-2]) for i in range(3,len(nums),2))
    # print("TEST")
    # print(nums)
    # print(abs(nums[-1]-nums[-2]))
    # print(list(abs(nums[i] - nums[i-2]) for i in range(2, len(nums), 2)))
    print(max(a,b,abs(nums[0]-nums[1]),abs(nums[-1]-nums[-2])))